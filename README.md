# AI-Powered College Information Assistant Using Google Cloud Generative AI

A B.Tech internship project that uses **Google Cloud Vertex AI / Gemini** to
answer student questions from a controlled college information knowledge base.

## Features

- Streamlit conversational web interface
- Gemini on Vertex AI for natural-language answers
- Retrieval of relevant college information before generation
- Local fallback mode when Google Cloud credentials are unavailable
- Source titles shown with answers
- Sample college knowledge base in JSON
- Dockerfile for cloud deployment
- Simple architecture suitable for a B.Tech internship

## Architecture

Student → Streamlit UI → Keyword Retrieval → College Knowledge Base
→ Gemini on Vertex AI → Grounded Answer → Student

## Project Structure

```text
AI_College_Information_Assistant/
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
├── README.md
├── data/
│   └── college_information.json
├── src/
│   ├── __init__.py
│   └── assistant.py
├── docs/
│   └── PROJECT_REPORT.md
└── tests/
    └── test_assistant.py
```

## Run locally

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app can run in fallback mode without cloud credentials.

## Google Cloud setup

1. Create/select a Google Cloud project.
2. Enable Vertex AI API.
3. Install Google Cloud CLI.
4. Authenticate with Application Default Credentials:

```bash
gcloud auth application-default login
```

5. Set the project:

```bash
gcloud config set project YOUR_PROJECT_ID
```

6. Set environment variables:

```text
GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
GOOGLE_CLOUD_LOCATION=global
GEMINI_MODEL=gemini-2.5-flash
```

Then run:

```bash
streamlit run app.py
```

## Customize the project

Edit:

`data/college_information.json`

Replace the sample content with verified information from your college:
admissions, departments, fees, hostel, transport, library, academic calendar,
contacts, regulations, and FAQs.

## Important

Do not commit API keys, passwords, service-account private keys, or other
credentials to GitHub.

For a production system, use a stronger retrieval system such as Vertex AI
Search / RAG and maintain an approved document corpus with access controls.

## Suggested GitHub description

"An AI-powered college information assistant built with Streamlit and Google
Cloud Vertex AI Gemini. The application retrieves relevant college information
and generates concise answers while reducing hallucinations through a
controlled knowledge base."
