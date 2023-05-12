"""Lemmatizes articles in dataframes.

Additionally contains:
lemmafier: A function that converts a text to its lemmatized form.
file_pointer: A function that returns the highest index in a csv file.
"""
import pandas as pd
import spacy
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor
from nltk.corpus import stopwords
from load import Time, load_years


def pool_executable(df_slice: pd.DataFrame):
    df_slice['article'] = df_slice['article'].apply(lambda x: lemmafier(x))
    df_slice.to_csv(f"../csv/{year}_03.csv",
                    mode='a',
                    header=not os.path.exists(f'../csv/{year}_03.csv'),
                    index=False,
                    encoding='UTF-8')
    sli = pd.to_numeric(df_slice.index[0])
    print(f"Wrote {df_slice.index} to ../csv/{year}_03.csv.\n"
          f'{df_slice.index[0]} / {df.shape[0]} '
          f'{sli // df.shape[0] * 100}% '
          f'{t.runtime()}              ')
    print("\033[F"*3)


def lemmafier(text: str) -> str:
    """Returns a given string in its lemmatized form."""
    nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
    doc = nlp(text)
    return " ".join([word.lemma_ for word in doc])


def file_pointer(ver: str) -> int:
    """Returns the highest index value of the file.

    Args:
        ver (str): Version of file to read.
    """
    return int(
        subprocess.check_output(['wc', '-l', f'../csv/{year}{ver}.csv'
                                 ]).decode("utf-8").split(' ')
        [0]) if os.path.exists(f'../csv/{year}{ver}.csv') else 0


def df_slice_gen(full_seq, chunk: int):
    remaining_seq = range(row, df.shape[0], chunk)
    slice = [(i, full_seq[i - row:i + chunk - row][-1]) for i in remaining_seq]
    return [df.iloc[i[0]:i[1]] for i in slice]


if __name__ == "__main__":
    t = Time()
    print(t.start())
    filler: list[str] = stopwords.words('english')

    # years = ['test']
    years: list[int] = load_years("years.txt")
    for year in years:
        # Skip finished files.
        progress: list[str] = []
        if os.path.exists('progress_tracker.txt'):
            with open('progress_tracker.txt', 'r') as file:
                progress = [date.strip('\n') for date in file]

        if year in progress:
            print(f'{year}_02.csv already completed, skipping...')
            continue

        print(f'Loading {year}_02.csv...', end='\r')
        df: pd.DataFrame = pd.read_csv(f'../csv/{year}_02.csv',
                                       encoding='UTF-8')
        print(f'{year}_02.csv loaded. {t.elapsed()}\n{t.line()}')

        print(f'Lemmifying articles in {year}_02.csv')
        chunk = 10
        row: int = file_pointer('_03')
        seq: list[int] = [i for i in range(row, df.shape[0])]
        slice_indexes = df_slice_gen(seq, chunk)
        with ProcessPoolExecutor() as exe:
            exe.map(pool_executable, slice_indexes)

        print(f"\n{t.collection()}")

        # Write finished csv year to text.
        with open('progress_tracker.txt', 'a+') as file:
            file.write(f'{year}\n')

    print("Succes!")
