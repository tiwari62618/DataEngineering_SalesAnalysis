import pandas as pd
def extract_data(file_path):
    print("Extracting data...")

    df=pd.read_csv(file_path)

    print(f"Records extracted: {len(df)}")

    return df