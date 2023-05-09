import pandas as pd
import string
from tqdm import tqdm
from nltk.corpus import stopwords
from load import Time
from load import load_years


def df_apply(t, df: pd.DataFrame, column: str, function: str) -> None:
    tqdm.pandas()
    df[column] = df[column].progress_apply(function)
    if t is not None:
        print(t.collection())


def remove_stopwords(article: str) -> str:
    filler = stopwords.words('english')
    return (
        ' '.join([word for word in article.split() if word not in filler])
        )


def remove_punctuation(article) -> str:
    punctuation = string.punctuation
    punctuation += '“”—”’1234567890'
    return article.translate(str.maketrans('', '', punctuation))


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
        df_apply(t, df, 'article', lambda x: x.lower())

        print('Removing commas from titles...')
        df_apply(t, df, 'title', lambda x: x.translate(
                str.maketrans('', '', ',')) if type(x) == str else x)

        print('Removing commas from author names...')
        df_apply(t, df, 'author', lambda x: x.translate(
                str.maketrans('', '', ',')) if type(x) == str else x)

        print('Removing punctuation from articles...')
        df_apply(t, df, 'article', lambda x: remove_punctuation(x))

        print('Removing filler words from articles...')
        df_apply(t, df, 'article', lambda x: remove_stopwords(x))

        print(f'Writing dataframe to {year}_01.csv...')
        df.to_csv(f"{year}_01.csv", index=False)
        print(t.collection())

    print("Succesfully cleaned all csv files!")
