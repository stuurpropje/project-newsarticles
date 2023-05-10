import pandas as pd
import time
start_time = time.time()
split = 0

print(time.strftime("%H:%M:%S", time.gmtime(start_time)))

df = pd.read_csv("all-the-news-2-1.csv")

df = df.set_index('year')

print("loading of df done")

dates = [2016, 2017, 2018, 2019, 2020]

for year in dates:
    df_year = df.loc[year]
    df_year.to_csv(f"{year}.csv")

    print(f'{year} is done loading!')

    total_runtime = time.time() - start_time
    print(time.strftime("%H:%M:%S", time.gmtime(total_runtime)))

    elapsed_time = 0 if split == 0 else time.time() - split
    split = time.time()
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
