"""Remove punctuation, stop words from dataframes.

Additionally contains:
df_apply; a wrapper function for inplace df modification.
remove_stopwords: a function that removes stopwords from a text.
remove_punctuation: a function that removes punctuation from a text.
"""
import pandas as pd
import string
from tqdm import tqdm
from nltk.corpus import stopwords
from load import Time
from load import load_years


def df_apply(df: pd.DataFrame, column: str, function) -> None:
    """Apply a function to a DataFrame.

    Args:
        t (Time): [description]
        df (pd.DataFrame): [description]
        column (str): [description]
        function (str): [description]
    """
    tqdm.pandas()
    df[column] = df[column].progress_apply(function)


def remove_stopwords(text: str) -> str:
    """Removes all stopwords from a text.

    Args:
        article (str): text to remove stopwords from.

    Returns:
        str: text without stopwords.
    """
    filler: list[str] = stopwords.words("english")
    return " ".join([word for word in text.split() if word not in filler])


def remove_punctuation(text: str) -> str:
    """Remove punctuation from a text.

    Args:
        text (str): text to remove punctuation from.

    Returns:
        str: text without punctuation.
    """
    additional_punct: str = string.punctuation + '"“‘—’”"'
    return text.translate(str.maketrans("", "", additional_punct))


if __name__ == "__main__":
    t = Time()
    print(t.start())

    years = load_years("years.txt")
    for year in years:
        print(f"Loading {year}.csv...", end='\r')
        df = pd.read_csv(f"../csv/{year}.csv", encoding="UTF-8")
        print(f"Loaded {year}.csv. {t.elapsed()}")

        df.dropna(subset=["article"], inplace=True)

        print("Casting articles to lowercase...")
        df_apply(df, "article", lambda x: x.lower())
        print(f"All articles cast to lowercase. {t.collection()}")

        print("Removing commas from titles...")
        df_apply(
            df,
            "title",
            lambda x: x.translate(str.maketrans("", "", ","))
            if isinstance(x, str)
            else x,
        )
        print(f"All commas removes from titles. {t.collection()}")

        print("Removing commas from author names...")
        df_apply(
            df,
            "author",
            lambda x: x.translate(str.maketrans("", "", ","))
            if isinstance(x, str)
            else x,
        )
        print(f"All commas removed from author names. {t.collection()}")

        print("Removing punctuation from articles...")
        df_apply(df, "article", lambda x: remove_punctuation(x))
        print(f"All punctuation removed. {t.collection()}", end="\r")

        print("Removing filler words from articles...")
        df_apply(df, "article", lambda x: remove_stopwords(x))
        print(f"All filler words removed from articles. {t.collection()}")

        print(f"Writing dataframe to {year}_01.csv...", end='\r')
        df.to_csv(f"../csv/{year}_01.csv", index=False, encoding='UTF-8')
        print(f"Cleaned dataframe written to {year}_01.csv. {t.collection()}")

    print("Succesfully cleaned all csv files!")
