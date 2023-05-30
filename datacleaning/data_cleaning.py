"""Remove superfluous information from loaded dataframes.

Converts articles to consist of only lowercase characters.
Removes commas in names and titles as this causes problems in a csv.
Removes stop words from articles, other extraenous punctuation.

Additionally contains:
df_apply: Function for inplace dataframe modification.
remove_stopwords: Function that removes stopwords from a text.
remove_punctuation: Function that removes punctuation from a text.
"""
import pandas as pd
import string
from tqdm import tqdm
from nltk.corpus import stopwords
from load import Time
from load import load_years


def df_apply(df: pd.DataFrame, column: str, function) -> None:
    """Wrapper for in-place applying on a DataFrame.

    Allows for a shorter representation of applying a function on a dataframe
    with a progress bar. tqdm.progress_apply does not support
    in-place modification. By wrapping it, the code becomes more readable.

    Args:
        df (pd.DataFrame): DataFrame to be modified
        column (str): Column to be modified.
        function (str): Function to apply to column.
    """
    tqdm.pandas()
    df[column] = df[column].progress_apply(function)


def remove_stopwords(text: str) -> str:
    """Return a text with all stopwords removed.

    Args:
        article (str): Text to remove stopwords from.
    """
    filler: list[str] = stopwords.words("english")
    return " ".join([word for word in text.split() if word not in filler])


def remove_punctuation(text: str) -> str:
    """Return a text with all punctuation removed.

    Args:
        text (str): Text to remove punctuation from.
    """
    additional_punct: str = string.punctuation + '"“‘—’”"'
    return text.translate(str.maketrans("", "", additional_punct))


if __name__ == "__main__":
    t = Time()
    print(t.start())

    years = load_years("../years.txt")
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
