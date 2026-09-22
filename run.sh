#!/bin/zsh

ollama pull llama3.2 || true
streamlit run content_app.py
