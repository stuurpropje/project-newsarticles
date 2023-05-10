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
    filler: list[str] = stopwords.words('english')
    return (' '.join([word for word in text.split() if word not in filler]))


def remove_punctuation(text: str) -> str:
    """Remove punctuation from a text.

    Args:
        text (str): text to remove punctuation from.

    Returns:
        str: text without punctuation.
    """
    punctuation: str = string.punctuation
    punctuation += '“”—”’1234567890'
    return text.translate(str.maketrans('', '', punctuation))


if __name__ == "__main__":
    t = Time()
    print(t.start())

    years = load_years("years.txt")
    for year in years:
        print(f'Loading {year}.csv...')
        df = pd.read_csv(f'{year}.csv')
        print(t.elapsed())

        df.dropna(subset=['article'], inplace=True)

        print('Casting articles to lowercase...')
        df_apply(df, 'article', lambda x: x.lower())
        print(t.collection())

        print('Removing commas from titles...')
        df_apply(
            df, 'title', lambda x: x.translate(str.maketrans('', '', ','))
            if isinstance(x, str) else x)
        print(t.collection())

        print('Removing commas from author names...')
        df_apply(
            df, 'author', lambda x: x.translate(str.maketrans('', '', ','))
            if isinstance(x, str) else x)
        print(t.collection())

        print('Removing punctuation from articles...')
        df_apply(df, 'article', lambda x: remove_punctuation(x))
        print(t.collection())

        print('Removing filler words from articles...')
        df_apply(df, 'article', lambda x: remove_stopwords(x))
        print(t.collection())

        print(f'Writing dataframe to {year}_01.csv...')
        df.to_csv(f"{year}_01.csv", index=False)
        print(t.collection())

    print("Succesfully cleaned all csv files!")
