"""Vectorizes articles in dataframes.

Additionally performs a LDA over the vectorized articles.
"""
from __future__ import annotations
import pandas as pd
import joblib
import sys
import os
import time
import threading
from nltk.corpus import stopwords
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

sys.path.append("../datacleaning")
from load import Time, load_years


def running_time():
    """Prints time to screen every 0. 1 second, stops when finished is set."""
    start_time = time.time()
    # This function is called by the main loop to check if the job is finished.
    while finished is False:
        clock = time.strftime(
            "%H:%M:%S", time.gmtime(time.time() - start_time)
        )
        print(f"Elapsed: {clock}", end="\r")
        time.sleep(0.1)


if __name__ == "__main__":
    t = Time()
    print(t.start())
    filler: list[str] = stopwords.words("english")

    lda = LatentDirichletAllocation(
        n_components=50, random_state=0, verbose=True
    )

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

        # Create a directory if one is not available.
        if not os.path.isdir("./csv"):
            os.mkdir("./csv")

        # Write finished vectorized text to file.
        joblib.dump(vectorizer, f"./csv/vectorizer_{year}.csv")
        joblib.dump(data_vectorized, f"./csv/data_vectorized_{year}.csv")

        print(f"Fitting LDA for {year}...")
        finished = False
        # finished alongside thread starts a runtime clock which displays
        #   the current running time to fit the data to the LDA,
        #   normalize the topic distribution and write them to a file.
        thread = threading.Thread(target=running_time)
        thread.start()
        lda.fit(data_vectorized)
        joblib.dump(lda, f"./csv/lda_{year}.csv")

        print("Normalising topic distributions...")
        doc_topic_dist = pd.DataFrame(lda.transform(data_vectorized))
        joblib.dump(doc_topic_dist, f"./csv/doc_topic_dist_{year}.csv")
        finished = True

    print(f"Succes! {t.collection()}")
