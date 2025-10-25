import boto3, os
from pathlib import Path

def upload_to_s3(local_path, bucket, s3_prefix, aws_creds=None):
    """Upload a file or directory to S3 under s3://{bucket}/{s3_prefix}/..."""
    if aws_creds:
        s3 = boto3.client('s3',
                          aws_access_key_id=aws_creds.get('aws_access_key_id'),
                          aws_secret_access_key=aws_creds.get('aws_secret_access_key'),
                          region_name=aws_creds.get('region'))
    else:
        s3 = boto3.client('s3')
    p = Path(local_path)
    files = [p] if p.is_file() else [f for f in p.rglob('*') if f.is_file()]
    for f in files:
        rel = f.relative_to(p) if p.is_dir() else Path(f).name
        key = f"{s3_prefix.rstrip('/')}/{rel.as_posix()}"
        s3.upload_file(str(f), bucket, key)
        print(f"Uploaded {f} -> s3://{bucket}/{key}")
