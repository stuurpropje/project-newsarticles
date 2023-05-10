import pandas as pd
import string
from tqdm import tqdm
from nltk.corpus import stopwords
from load import Time
from load import load_years
from datacleaning import df_apply

from concurrent.futures import ProcessPoolExecutor

tqdm.pandas()
t = Time()
print(t.start())

years = load_years("years.txt")
for year in years:
    print(f'Loading {year}_01.csv...')
    df = pd.read_csv(f'{year}_01.csv')
    print(t.collection())

    print('Removing commas from authors...')
    df_apply(t, df, 'author', lambda x: x.translate(
            str.maketrans('', '', ',')) if type(x) == str else x)

    print(f'Writing dataframe to {year}_01.csv...')
    df.to_csv(f"{year}_01.csv")
    print(t.collection())
