import pandas as pd

def run_basic_checks(df):
    results = {
        'missing_values': df.isnull().sum().to_dict(),
        'duplicate_rows': int(df.duplicated().sum()),
        'row_count': int(len(df)),
        'columns': list(df.columns)
    }
    return results
