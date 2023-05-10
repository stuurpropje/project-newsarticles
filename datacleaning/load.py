"""Split large CSV file into smaller files based on the year column.

Additionally contains:
Time: A class for keeping processing time.
load: A function for loading a CSV.
load_years: A function for loading years from a text file.
write: A function for writing the smaller CSV files.

Requires: all-the-news-2-1.csv in ../csv/all-the-news-2-1.csv.
"""
import time
import pandas as pd


class Time():
    """Utility class for measuring time intervals.

    This class provides methods for measuring elapsed time intervals,
    formatting time in the Hours:Minutes:Seconds format,
    and generating separator lines.

    Attributes:
        _start_time: Start time of the timer in float seconds.
        _split: Time since last reported split in float seconds.
    """

    def __init__(self) -> None:
        """Initialize the TimeSeries."""
        self._start_time: float = time.time()
        self._split: float = 0

    def _formatter(self, unformatted_time: float) -> str:
        """Format the time as Hours:Minutes:Seconds and returns it."""
        return time.strftime("%H:%M:%S", time.gmtime(unformatted_time))

    def start(self) -> str:
        """Return a string of start time (H:M:S)."""
        return f'Start time: {self._formatter(self._start_time)}'

    def runtime(self) -> str:
        """Return a string (H:M:S) of total runtime."""
        total_runtime: float = time.time() - self._start_time
        return f'Total runtime: {self._formatter(total_runtime)}'

    def elapsed(self) -> str:
        """Return a string (H:M:S) of time since last elapsed time."""
        elapsed_time: float = (time.time() - self._start_time if self._split
                               == 0 else time.time() - self._split)
        self._split = time.time()
        return f'Time since last update: {self._formatter(elapsed_time)}'

    def line(self) -> str:
        """Return a seperator line."""
        return '--------------------------------------'

    def collection(self) -> str:
        """Return a string combining total runtime and split time."""
        return (f"{self.elapsed()}\n"
                f"{self.runtime()}\n"
                f"{self.line()}")


def load_years(dates: str) -> list[int]:
    """Loads years from a file.

    Args:
        dates (string): location of file containing list of dates to read.
            Dates in file are to be seperated by newlines.

    Returns:
        list[int]: containing dates from the file.
    """
    with open(dates, 'r') as file:
        years: list[int] = [int(year.strip('\n')) for year in file]
    return years


def load(file: str) -> pd.DataFrame:
    """Loads a CSV file into a pandas DataFrame.

    Args:
        file (str): location of file to be loaded into Dataframe.

    Returns:
        pd.DataFrame: Dataframe from csv file.
    """
    df: pd.DataFrame = pd.read_csv(file)
    df = df.set_index('year')
    return df


def write(t: Time, df: pd.DataFrame) -> None:
    """Split main csv into smaller csvs based on published article dates.

    Args:
        t (Time): Utility to keep track of loading time.
        df (pd.DataFrame): main df to be split up according to year column.
    """
    years: list[int] = load_years("years.txt")
    for year in years:
        df_year = df.loc[year]
        df_year.to_csv(f"../csv/{year}.csv")
        print(f'All articles of {year} written to {year}.csv!')
        print(t.collection())


if __name__ == "__main__":
    t = Time()
    print(t.start())

    df: pd.DataFrame = load("../csv/all-the-news-2-1.csv")
    print(f'Dataframe loaded into memory. {t.elapsed()}')

    write(t, df)
    print("Successfully split all-the-news-2-1 into seperate years.")
