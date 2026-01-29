# IGCSE Business Studies AI Tutor (Local LLM)

A specialized AI tutor designed for the **Cambridge IGCSE Business Studies (0264)** syllabus. This tool uses Retrieval-Augmented Generation (RAG) to fetch live study materials and utilizes a local Mistral model to generate exam-ready responses.

---

## How It Works
1. **Search:** The script queries DuckDuckGo for IGCSE-specific study notes.
2. **Extract:** It scrapes relevant text from business revision websites using BeautifulSoup4.
3. **Process:** It feeds the context into a local **Mistral 7B** model via Ollama.
4. **Output:** The model generates bulleted, mark-scheme-oriented answers based strictly on the 0264 syllabus requirements.

---

## Requirements
* **Python:** 3.9 or higher
* **Ollama:** Installed and running locally ([Download here](https://ollama.com))
* **Hardware:** 8GB RAM minimum (16GB recommended for Mistral 7B)

---

## Installation & Setup

### 1. Model Setup
Ensure Ollama is installed, then open your terminal and pull the model:
```bash
ollama pull mistral:7b

```
---

### 2. Environmental Setup
Create a virtual environment to keep your dependencies organized.

#### MacOS/Linux

##### Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate

```

###### Install dependencies
```bash
pip install -r requirements.txt

```
#### Windows

##### Create and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate

```

##### Install dependencies
```bash
pip install -r requirements.txt

```
---
### How to Run
Once your environment is set up and activated, launch the tutor:
```bash
python main.py
```
Then enter the IGCSE Business Studies Questions in the terminal

---
### Notes:
1. This project runs locally only
2. AI computation happens on the user’s machine
3. No data is sent to external AI services
4. Intended for educational and exam practice use

---
### Disclaimers:
1. This tool is for learning purposes only
2. Responses can take upto ~3 minutes to load