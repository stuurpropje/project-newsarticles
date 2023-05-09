import pandas as pd
import time


class Time(object):
    def __init__(self) -> None:
        self._start_time = time.time()
        self._split = 0

    def start(self) -> str:
        format = time.strftime("%H:%M:%S", time.gmtime(self._start_time))
        return f'Start time: {format}'

    def runtime(self) -> str:
        total_runtime = time.time() - self._start_time
        formatted_rt = time.strftime("%H:%M:%S", time.gmtime(total_runtime))
        return f'Total runtime: {formatted_rt}'

    def elapsed(self) -> str:
        elapsed_time = (time.time() - self._start_time
                        if self._split == 0 else time.time() - self._split)
        formatted_et = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        self._split = time.time()
        return f'Time since last update: {formatted_et}'

    def line(self) -> str:
        return '--------------------------------------'

    def collection(self) -> str:
        return (
            f"{self.runtime()}\n"
            f"{self.elapsed()}\n"
            f"{self.line()}"
        )


def load_years(file) -> list[int]:
    with open("years.txt", 'r') as file:
        years = [int(year.strip('\n')) for year in file]
    return years


def load(file) -> pd.DataFrame:
    df = pd.read_csv(file)
    df = df.set_index('year')
    return df


def write(t, df) -> None:
    years = load_years("years.txt")
    for year in years:
        df_year = df.loc[year]
        df_year.to_csv(f"{year}.csv")
        print(f'All articles of {year} written to {year}.csv!')
        print(t.collection())


if __name__ == "__main__":
    t = Time()
    print(t.start())

    df = load("all-the-news-2-1.csv")
    print(f'Dataframe loaded into memory. {t.elapsed()}')

    write(t, df)
    print("Success!")
