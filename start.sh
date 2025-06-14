#!/bin/bash

# Install uv if not present
curl -Ls https://astral.sh/uv/install.sh | sh

# Add uv to PATH manually
export PATH="/opt/render/.local/bin:$PATH"

# Optional: create .venv with uv (if not already created)
# /opt/render/.local/bin/uv venv

# Install dependencies (optional if using requirements.txt)
# /opt/render/.local/bin/uv pip install -r requirements.txt

# Start the FastAPI app
/opt/render/.local/bin/uvicorn api:app --host 0.0.0.0 --port 10000


