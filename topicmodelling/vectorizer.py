"""Vectorizes articles in dataframes.

Additionally performs a LDA over the vectorized articles.
"""
from __future__ import annotations
import pandas as pd
import joblib
import sys
import os
from nltk.corpus import stopwords
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

sys.path.append("../datacleaning")
from load import Time, load_years


if __name__ == "__main__":
    t = Time()
    print(t.start())
    filler: list[str] = stopwords.words("english")

    years: list[int] = load_years("../years.txt")
    for year in years:
        print(f"Loading {year}_03.csv...", end="\r")
        df: pd.DataFrame = pd.read_csv(
            f"../csv/{year}_03.csv", encoding="UTF-8"
        )
        print(f"{year}_03.csv loaded. {t.elapsed()}\n{t.line()}")

        print(f"Vectorizing articles in {year}_03.csv")
        vectorizer = CountVectorizer(min_df=2)
        data_vectorized = ""
        data_vectorized = vectorizer.fit_transform(tqdm(df["article"]))
        print(len(vectorizer.get_feature_names_out()))

        print(f"\n{t.collection()}")

        # Write finished vectorized text to file.
        if not os.path.isdir('./csv'):
            os.mkdir('./csv')

        joblib.dump(vectorizer, f"./csv/vectorizer_{year}.csv")
        joblib.dump(data_vectorized, f"./csv/data_vectorized_{year}.csv")

        lda = LatentDirichletAllocation(
            n_components=50, random_state=0, verbose=True
        )
        lda.fit(data_vectorized)
        joblib.dump(lda, f"./csv/lda_{year}.csv")

    print("Succes!")
