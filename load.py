import pandas as pd
import time
dates: list[int] = [2016, 2017, 2018, 2019, 2020]


class Time(object):
    def __init__(self) -> None:
        self.start_time = time.time()
        self.split = 0

    def start(self) -> str:
        format = time.strftime("%H:%M:%S", time.gmtime(self.start_time))
        return f'Start time: {format}'

    def runtime(self) -> str:
        total_runtime = time.time() - self.start_time
        formatted_rt = time.strftime("%H:%M:%S", time.gmtime(total_runtime))
        return f'Total runtime: {formatted_rt}'

    def elapsed(self) -> str:
        elapsed_time = 0 if self.split == 0 else time.time() - self.split
        formatted_et = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        self.split = time.time()
        return f'Elapsed: {formatted_et}'


def load(file) -> pd.DataFrame:
    df = pd.read_csv(file)
    df = df.set_index('year')
    return df


def write(df, t) -> None:
    for year in dates:
        df_year = df.loc[year]
        df_year.to_csv(f"{year}.csv")
        print(f'All articles of {year} written to {year}.csv!')

        print(t.runtime())
        print(t.elapsed())
        print("")


if __name__ == "__main__":
    t = Time()
    print(t.start())

    df = load("all-the-news-2-1.csv")
    print("Dataframe loaded into memory.")
    print(t.runtime())
    print(t.elapsed())
    print("")

    write(df, t)
    print("Success!")
