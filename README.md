# IGCSE Business Studies AI Tutor (Local LLM)

This project is a local AI tutor for **Cambridge IGCSE Business Studies (0264)**.
It runs entirely on the user's device through **Ollama** and does not rely on paid APIs or browser-based AI.

## How It Works
1. The script runs in the terminal.
2. The user enters a question.
3. Relevant reference material is retrieved from the web via DuckDuckGo.
4. A local LLM (Mistral 7B) generates a structured, exam-ready answer based on the syllabus.

## Model Used
* **Mistral:7b** (via Ollama)

## Requirements
* Python 3.9+
* Ollama installed locally

## Installation

### 1. Install Ollama
Download and install Ollama from [ollama.com](https://ollama.com).

### 2. Pull the Model
Open your terminal and run:
```bash
ollama pull mistral:7b

Install python dependencies:
pip install -r requirements.txt

How to run:
python main.py

Then enter the IGCSE Business Studies Questions in the terminal

Notes:

This project runs locally only
AI computation happens on the user’s machine
No data is sent to external AI services
Intended for educational and exam practice use

Disclaimer:
This tool is for learning purposes only
