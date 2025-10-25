# External Data Cloud Publishing & Metadata Discovery (Extended)

This is the **Extended** version of the project scaffold. It contains:
- Ingest & uploader utilities to push raw data to S3
- PySpark metadata extractor & data quality jobs
- Snowflake loader example to create external stage & COPY INTO
- Airflow DAG to orchestrate the pipeline
- Dockerfile and docker-compose for local testing
- GitHub Actions CI workflow (smoke tests)
- Example data, configs and a Jupyter notebook for metadata exploration

**IMPORTANT:** Replace credentials in config files with secrets stored in your environment or secrets manager. Do NOT commit real secrets to GitHub.
