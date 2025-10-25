import os, json
import pandas as pd
from pathlib import Path

def extract_metadata_local(file_path, sample_rows=10):
    ext = Path(file_path).suffix.lower().lstrip('.')
    if ext == 'csv':
        df = pd.read_csv(file_path)
    elif ext == 'json':
        df = pd.read_json(file_path, lines=False)
    else:
        # treat as text
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        return {'type': 'text', 'num_lines': len(lines), 'samples': lines[:sample_rows]}

    metadata = {
        'file_name': os.path.basename(file_path),
        'columns': list(df.columns),
        'dtypes': {c: str(dt) for c, dt in zip(df.columns, df.dtypes)},
        'num_rows': len(df),
        'missing_values': df.isnull().sum().to_dict(),
        'sample_rows': df.head(sample_rows).to_dict(orient='records')
    }
    return metadata

def write_metadata_json(metadata, out_path):
    with open(out_path, 'w') as f:
        json.dump(metadata, f, indent=2)
