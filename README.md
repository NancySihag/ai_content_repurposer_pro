# AI Content Repurposer Pro

AI-powered content repurposing application that transforms long-form blog content into multiple social-media-ready posts using a local LLM.

## Overview

AI Content Repurposer Pro is a Python and Streamlit application designed to make content repurposing faster and more efficient.

The application accepts long-form content in TXT or Markdown format and uses Ollama with Llama 3.2 to generate multiple short-form social media posts from the original content.

The project demonstrates local AI integration, content processing, Streamlit application development, and automated testing.

## Features

- Convert long-form content into multiple social-media-ready posts
- Support for TXT and Markdown input
- Local AI generation using Ollama
- Llama 3.2 model integration
- Simple Streamlit user interface
- Automated testing with Pytest
- Structured content generation workflow
- Download/export support for generated content

## Tech Stack

- **Python** — Core application logic
- **Streamlit** — Web application interface
- **Ollama** — Local LLM integration
- **Llama 3.2** — Local language model
- **Pytest** — Automated testing
- **Pandas** — Data handling and processing
- **Git & GitHub** — Version control

## How It Works

The application follows a simple workflow:

1. User provides long-form content.
2. The application reads the TXT or Markdown content.
3. The content is processed and prepared for the AI model.
4. Ollama sends the content to the local Llama 3.2 model.
5. The model generates multiple social-media-ready posts.
6. The generated content is displayed through the Streamlit interface.
7. Users can export the generated results.

## Project Structure
ai_content_repurposer_pro/
│
├── content_app.py
├── tests/
│   └── test_*.py
├── README.md
└── requirements.txt

Installation
1. Clone the repository
git clone https://github.com/NancySihag/ai_content_repurposer_pro.git

2. Move into the project directory
cd ai_content_repurposer_pro

3. Create a virtual environment
python3 -m venv .venv

4. Activate the virtual environment
5. macOS / Linux
source .venv/bin/activate

Windows
.venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

Ollama Setup
This project uses Ollama to run the language model locally.
Install Ollama and make sure the required model is available:
 ollama pull llama3.2
Then verify that Ollama is running before starting the application.
Run the Application
Start the Streamlit application with:
 streamlit run content_app.py
Streamlit will provide a local URL where the application can be opened in a browser.
Testing
The project includes automated tests using Pytest.
Run:
 pytest -v
The tests help verify that important parts of the application work as expected.

Example Workflow
Input
A user provides a long-form blog post or article in TXT or Markdown format.
Processing
The application sends the content through the local LLM workflow using Ollama and Llama 3.2.
Output
The application generates multiple shorter posts that can be adapted for social media.
Screenshots
![AI Content Repurposer Pro](screenshots/content-repurposer.png)

Why I Built This
I built this project to explore practical applications of local AI models and demonstrate how AI can automate repetitive content-related workflows.
The project combines Python development, Streamlit interfaces, local LLM integration, content processing, and automated testing.

Key Learning
Through this project, I practiced:
- Integrating a local LLM into a Python application
- Working with Ollama and Llama models
- Building interactive Streamlit applications
- Processing TXT and Markdown files
- Structuring AI-powered workflows
- Writing automated tests with Pytest
- Managing projects with Git and GitHub

Future Improvements
Possible future improvements include:
- Additional social media output formats
- Custom tone and writing-style controls
- More local LLM model options
- Improved content customization
- Batch content processing
- Additional export formats
- Content history and project management

Author
Nancy Sihag
BCA Student | Python Developer | AI & Automation | Web Development

GitHub:
https://github.com/NancySihag

LinkedIn:
https://www.linkedin.com/in/nancy-sihag/

License
This project is intended for learning, experimentation, and portfolio purposes.

