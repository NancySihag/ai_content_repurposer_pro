# AI Content Repurposer Pro ✨

A local AI-powered content repurposing tool built with Python, Streamlit, and Ollama. Upload a blog or article and transform it into platform-specific content such as LinkedIn posts, Twitter threads, Instagram content, email copy, or YouTube content.

The application runs AI generation locally through Ollama, allowing users to experiment with content transformation without relying on a paid cloud AI API.

## 🚀 Features

- Upload `.txt` and `.md` content files
- Generate 5 content variations from one source
- Support multiple content formats:
  - Twitter Thread
  - LinkedIn
  - Instagram
  - Email
  - YouTube
- Choose content tone:
  - Casual
  - Professional
  - Fun
- Control generated content length
- Local AI generation using Ollama
- Ollama availability check
- Download generated posts as CSV
- Simple Streamlit interface
- No paid AI API required

## 🧠 How It Works

```text
Upload Blog / Article
        ↓
Read Source Content
        ↓
Select Platform + Tone + Length
        ↓
Generate Prompts
        ↓
Ollama + Llama 3.2
        ↓
Generate 5 Content Variations
        ↓
Display Results
        ↓
Download as CSV
