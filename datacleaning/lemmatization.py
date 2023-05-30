"""Lemmatizes articles in dataframes.

Additionally contains:
lemmafier: A function that converts a text to its lemmatized form.
file_pointer: A function that returns the highest index in a csv file.
"""
import pandas as pd
import spacy
import os
import subprocess
import math
from concurrent.futures import ProcessPoolExecutor
from nltk.corpus import stopwords
from load import Time, load_years


def pool_executable(df_slice: pd.DataFrame):
    """Convert a group of articles in a dataframe to its lemmatized form.

    This function is designed to be run over multiple cores concurrently.
    This function gives each core a task. Each core writes to the same output file.
    As each core writes asynchronously to the file, the order of the original file is lost.

    Args:
        df_slice: The slice of the dataframe.
    """

    df_slice["article"] = df_slice["article"].apply(lambda x: lemmatizer(x))
    df_slice.to_csv(
        f"../csv/{year}_03.csv",
        mode="a",
        header=not os.path.exists(f"../csv/{year}_03.csv"),
        index=False,
        encoding="UTF-8",
    )
    sli: int = pd.to_numeric(df_slice.index[0])
    # Print function specifies task performed, progress, percentual progress, current runtime.
    print(
        f"Wrote slice [{df_slice.index[0]}:{sli + 9}] to ../csv/{year}_03.csv."
        f" {sli + 9} out of {df.shape[0]} articles lemmatized. "
        f"{math.floor(int(sli) / df.shape[0] * 100)}% done. "
        f"{t.runtime()}              ",
        end="\r",
    )


def lemmatizer(text: str) -> str:
    """Return a given string in its lemmatized form."""
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    doc = nlp(text)
    return " ".join([word.lemma_ for word in doc])


def file_pointer(ver: str) -> int:
    """Return the highest index value of the active data file to write to.

    Will return 0 if no file exists. This function allows for intermittent
        execution of lemmatization of data files. Due to the large size of
        each file and the long processing times, progress is not lost upon
        program termination. This function finds the highest index value, and
        assigns that as the point to read and lemmatize out of from its source
        file. This allows for a varying starting index based on previous
        progress.

    Args:
        ver (str): Version of file to read.
    """
    if os.path.exists(f"../csv/{year}{ver}.csv"):
        return int(
            subprocess.check_output(["wc", "-l", f"../csv/{year}{ver}.csv"])
            .decode("utf-8")
            .split(" ")[0]
        )
    else:
        return 0


def df_slice_gen(full_seq, chunk: int):
    """Slice a dataframe into equal parts.

    This function slices a dataframe into equal parts which can be divided
        amongst the available cores. If the dataframe is not sliced,
        only a singular core can process the dataframe. If the dataframe
        is divided amongst all available cores, progress cannot be tracked.
        Each core would have to finish their lemmatization progress before
        writing their work. This means that intermittent work is not possible.

    Args:
        full_seq: The unprocessed part of the dataframe to slice.
        chunk: The size of each slice.

    Returns:
        A list of dataframe slices.
    """
    remaining_seq = range(row, df.shape[0], chunk)
    slice = [
        (i, full_seq[i - row : i + chunk - row][-1]) for i in remaining_seq
    ]
    return [df.iloc[i[0] : i[1]] for i in slice]


if __name__ == "__main__":
    t = Time()
    print(t.start())
    filler: list[str] = stopwords.words("english")

    years: list[int] = load_years("../years.txt")
    for year in years:
        # Skip finished files.
        progress: list[str] = []
        if os.path.exists("progress_tracker.txt"):
            with open("progress_tracker.txt", "r") as file:
                progress = [date.strip("\n") for date in file]

        if year in progress:
            print(f"{year}_02.csv already completed, skipping...")
            continue

        print(f"Loading {year}_02.csv...", end="\r")
        df: pd.DataFrame = pd.read_csv(
            f"../csv/{year}_02.csv", encoding="UTF-8"
        )
        print(f"{year}_02.csv loaded. {t.elapsed()}\n{t.line()}")

        print(f"Lemmifying articles in {year}_02.csv")

        chunk = 10  # Number of articles passed to each core at a time.
        # Varying starting index allows for the program to be turned off
        # and starting where it was stopped.
        row: int = file_pointer("_03")
        seq: list[int] = [i for i in range(row, df.shape[0])]
        slice_indexes = df_slice_gen(seq, chunk)

        # Divide the lemmatizer function over all available cores.
        # Cores write their work to a file when finished.
        with ProcessPoolExecutor() as exe:
            exe.map(pool_executable, slice_indexes)

        print(f"\n{t.collection()}")

        # Save finished years so that
        # they can be skipped on later program activation.
        with open("progress_tracker.txt", "a+") as file:
            file.write(f"{year}\n")

    print("Succes!")
