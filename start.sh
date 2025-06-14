#!/bin/bash
set -e

# Install uv (if not already in environment)
curl -Ls https://astral.sh/uv/install.sh | bash

# Install all dependencies from pyproject.toml
uv pip install --system

# Activate the virtual environment
source .venv/bin/activate

# Start your FastAPI app
uvicorn api:app --host 0.0.0.0 --port 8000

