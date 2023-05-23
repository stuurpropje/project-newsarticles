import pandas as pd
from load import Time, load_years

if __name__ == "__main__":
    t = Time()
    print(t.start())

    years = load_years("../years.txt")

    for year in years:
        print(f"Loading {year}_1.csv...", end='\r')
        df = pd.read_csv(f"../csv/{year}_01.csv", encoding='UTF-8')
        print(f"Loaded {year}_1.csv. {t.elapsed()}")

        print("Sampling 10%...", end='\r')
        df = df.sample(frac=0.10, axis=0, ignore_index=True)
        print(f"Sampling completed. New df shape:{df.shape}. {t.elapsed()}")

        print(f"Writing sample to {year}_02.csv...", end='\r')
        df.to_csv(f"../csv/{year}_02.csv", index=False, encoding='UTF-8')
        print(f"Sample written to {year}_02.csv.    \n{t.collection()}")

    print("Succesfully reduced row count of CSV files by 90%.")
