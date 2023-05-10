import pandas as pd
import spacy
import os
import subprocess
import math
from concurrent.futures import ProcessPoolExecutor
from nltk.corpus import stopwords
from load import Time
from load import load_years


def lemmafier(text: str) -> str:
    nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
    doc = nlp(text)
    return " ".join([word.lemma_ for word in doc])


def file_pointer(ver: str) -> int:
    return int(
        subprocess.check_output(['wc', '-l', f'{year}{ver}.csv']).decode(
            "utf-8").split(' ')[0]) if os.path.exists(f'{year}{ver}.csv') else 0


if __name__ == "__main__":
    t = Time()
    print(t.start())
    filler: list[str] = stopwords.words('english')

    years: list[int] = load_years("years.txt")
    for year in years:
        with open('progress_tracker.txt', 'a+') as file:
            progress = [marked.strip('\n') for marked in file]

        if year in progress:
            print(f'{year}_01.csv already completed, skipping...')
            continue

        print(f'Loading {year}_01.csv...')
        df: pd.DataFrame = pd.read_csv(f'{year}_01.csv')
        print(f'File loaded. {t.elapsed()}\n{t.line()}')

        print('Lemmifying text...')
        chunk = 10000
        row: int = file_pointer('_02')
        while row < df.shape[0]:
            with ProcessPoolExecutor() as exe:
                article: str = df.iloc[row]['article']
                article = exe.map(lemmafier(article),
                                  [i for i in range(row, row + chunk)])

            df.iloc[row:row + chunk].to_csv(
                f"{year}_02.csv",
                mode='a',
                header=not os.path.exists(f'{year}_02.csv'),
                index=False)

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
