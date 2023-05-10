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
from df_text_cleaning import df_apply
from concurrent.futures import ProcessPoolExecutor
from nltk.corpus import stopwords
from load import Time
from load import load_years


def pool_executable(df_slice: pd.DataFrame):
    df_apply(df_slice, 'article', lambda x: lemmafier(x))
    df_slice.to_csv(
            f"../csv/{year}_02.csv",
            mode='a',
            header=not os.path.exists(f'../csv/{year}_02.csv'),
            index=False)


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


def df_slice_gen(seq, chunk: int):
    slices = [(i, seq[i: i + chunk][-1]) for i in range(0, len(seq), chunk)]
    return [df[i[0]:i[1]] for i in slices]


if __name__ == "__main__":
    t = Time()
    print(t.start())
    filler: list[str] = stopwords.words('english')

    years = ['test']
    # years: list[int] = load_years("years.txt")
    for year in years:
        with open('progress_tracker.txt', 'a+') as file:
            progress = [marked.strip('\n') for marked in file]

        if year in progress:
            print(f'{year}_01.csv already completed, skipping...')
            continue

        print(f'Loading {year}_01.csv...')
        df: pd.DataFrame = pd.read_csv(f'../csv/{year}_01.csv')
        print(f'File loaded. {t.elapsed()}\n{t.line()}')

        print('Lemmifying text...')
        chunk = 1000
        row: int = file_pointer('_02')
        while row < df.shape[0]:
            with ProcessPoolExecutor() as exe:
                exe.map(pool_executable, df_slice_gen([i for i in range(row, df.shape[0])], chunk))

            print(
                f'{row}/{df.shape[0]} '
                f'{math.floor(row / df.shape[0] * 100)}% '
                f'{t.runtime()}',
                end='\r')
            row += chunk

        print(t.collection())

        with open('progress_tracker.txt', 'a') as file:
            file.write(f'{year}\n')
    print("Succes!")
