import json, os
from src.s3_uploader import upload_to_s3
from src.metadata_extractor import extract_metadata_local, write_metadata_json
from src.data_quality import run_basic_checks

def main():
    # Load config if present (example file is config/aws_config.example.json)
    aws_cfg_path = 'config/aws_config.example.json'
    aws_cfg = None
    if os.path.exists(aws_cfg_path):
        with open(aws_cfg_path) as f:
            aws_cfg = json.load(f)

    data_dir = 'data/raw'
    out_meta_dir = 'data/metadata'
    os.makedirs(out_meta_dir, exist_ok=True)

    for fname in os.listdir(data_dir):
        fpath = os.path.join(data_dir, fname)
        try:
            meta = extract_metadata_local(fpath)
            meta_out = os.path.join(out_meta_dir, f"{os.path.basename(fname)}.metadata.json")
            write_metadata_json(meta, meta_out)
            print('Metadata written to', meta_out)
        except Exception as e:
            print('Metadata extraction failed for', fpath, e)

    # Example upload: uploads whole raw dir to S3 if aws_cfg provided
    if aws_cfg:
        upload_to_s3(data_dir, aws_cfg['s3_raw_bucket'], 'datasets/raw', aws_cfg)
    else:
        print('No AWS config found; skipping upload step.')

if __name__ == '__main__':
    main()
