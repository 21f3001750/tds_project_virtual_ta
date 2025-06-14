#!/bin/bash

echo "📦 Running embedding loader..."
python retriever/load_data.py

echo "🚀 Starting FastAPI server..."
uvicorn api:app --host 0.0.0.0 --port 10000
