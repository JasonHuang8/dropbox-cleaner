# CleanDrop (dropbox-cleaner)

Privacy‑preserving **Dropbox → Scrubber → S3** connector. Auth via OAuth2, recursively ingest files from Dropbox, POST to an external scrubbing API, then upload sanitized outputs to S3.

## Overview
CleanDrop is modular and enterprise‑friendly from day one:
- `core/`: Dropbox, Scrubber, and Storage clients; config; models
- `cli/`: Click‑based CLI entrypoint
- `mock_scrubber/`: local FastAPI mock for the scrubbing API
- `integrations/`: placeholders for Airflow / Iceberg / Spark (enabled in Milestone 11)

> Platform: macOS (M1). Python 3.11+.

## Quickstart

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Create a local env file (never commit .env)
cp .env.example .env

## Planned Integrations
- [Airflow DAG](integrations/airflow/pipeline_dag.py)
- [Apache Iceberg Writer](integrations/iceberg/iceberg_writer.py)
- [Spark Job](integrations/spark/spark_job.py)
