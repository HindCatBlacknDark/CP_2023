import pandas as pd
import os

data_folder = 'data'

csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    print(f"Data from {file}:")
    print(df.head())
    print("\n")