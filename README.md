 # Competitor Intelligence & Vibe Monitor

## Overview

This AI Agent monitors competitors, tracks changes in pricing, features, positioning, and marketing strategies, and generates intelligence reports using Retrieval-Augmented Generation (RAG).

## Features

* Website Crawling using Playwright
* Snapshot Storage
* ChromaDB Vector Database
* RAG-based Context Retrieval
* Groq LLM Analysis
* Intelligence Report Generation
* Email Notifications
* Vision-Based Screenshot Comparison

## Tech Stack

* Python
* LangChain
* ChromaDB
* Groq
* Playwright
* Streamlit

## Installation

```bash
pip install -r requirements.txt
playwright install
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_key

EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_app_password
```

## Run Application

```bash
streamlit run app.py
```

## Project Architecture

Crawler → Snapshot Storage → Embeddings → ChromaDB → Retriever → Groq LLM → Intelligence Report → Email Alert

## AI Techniques Used

* Retrieval-Augmented Generation (RAG)
* Agentic Workflow
* Prompt Engineering
* API Integration
* Semantic Change Detection

## Author

Jaydeep Singh Chouhan
