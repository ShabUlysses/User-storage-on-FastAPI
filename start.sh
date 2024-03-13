#! /usr/bin/env bash
# Run migrations and code
alembic upgrade head && uvicorn app.app:app --host 0.0.0.0 --port 8000