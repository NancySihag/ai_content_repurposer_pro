#!/bin/zsh
set -e

# Start Ollama model if the CLI is installed (optional)
if command -v ollama >/dev/null 2>&1; then
  ollama pull llama3.2 || true
else
  echo "[run.sh] ollama CLI not found; starting Streamlit without auto-pulling model."
fi

# Run Streamlit app
streamlit run content_app.py
