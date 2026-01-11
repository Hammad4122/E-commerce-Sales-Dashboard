import os
import pandas as pd

def read_csv():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "Dataset", "Sales_Data.csv")
    df = pd.read_csv(csv_path)
    return df