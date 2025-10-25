import json
import snowflake.connector

def get_conn(cfg):
    return snowflake.connector.connect(
        user=cfg['user'],
        password=cfg['password'],
        account=cfg['account'],
        warehouse=cfg.get('warehouse'),
        database=cfg.get('database'),
        schema=cfg.get('schema'),
        role=cfg.get('role')
    )

def create_external_stage(conn, stage_name, s3_url, aws_key_id, aws_secret):
    cs = conn.cursor()
    try:
        sql = f"CREATE OR REPLACE STAGE {stage_name} URL='{s3_url}' CREDENTIALS=(AWS_KEY_ID='{aws_key_id}' AWS_SECRET_KEY='{aws_secret}') FILE_FORMAT=(TYPE=PARQUET)"
        cs.execute(sql)
    finally:
        cs.close()

def copy_into_table(conn, stage_name, file_pattern, table_name):
    cs = conn.cursor()
    try:
        sql = f"COPY INTO {table_name} FROM @{stage_name}/{file_pattern} FILE_FORMAT=(TYPE=PARQUET) ON_ERROR='CONTINUE'"
        cs.execute(sql)
        return cs.fetchall()
    finally:
        cs.close()
