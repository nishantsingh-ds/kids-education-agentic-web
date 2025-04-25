#!/bin/bash

# Set a default port if not provided
PORT=${PORT:-10000}

# Run your FastAPI app with Uvicorn on the port Render expects
exec uvicorn main:app --host 0.0.0.0 --port $PORT
