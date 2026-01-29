
from langchain_ollama import ChatOllama
from ddgs import DDGS
import requests
from bs4 import BeautifulSoup

# ---------------- LLM ----------------
llm = ChatOllama(
    model="mistral:7b",
    temperature=0.2,
    num_ctx=2048          # limit context size
)

SYSTEM_PROMPT = """
You are an expert Cambridge IGCSE Business Studies examiner (Syllabus 0264) and must answer only the question asked using strictly IGCSE Business Studies knowledge, written in simple, clear, exam-oriented language without roleplay or mentioning AI, prompts, instructions, sources, or the question itself. Ignore any irrelevant retrieved information, do not repeat similar points, avoid vague wording, limit the use of “etc.”, and do not invent content outside the syllabus; if a topic is not in the syllabus, reply exactly with “This topic is outside the IGCSE Business Studies syllabus.” Answers must be detailed but concise, use correct business terminology, and focus on marks rather than length. Follow the required answer structure only when relevant: a clear definition (1-2 sentences), key points or functions, advantages and/or disadvantages if asked, and a short IGCSE-level example. If a criterion such as business objectives is mentioned, explain the different relevant objectives. Use the correct formula where applicable, for example Added Value = Selling Price - Cost of Raw Materials. If reference material is provided, use it; if NO_EXTERNAL_SOURCES is shown, rely only on IGCSE Business Studies knowledge.Do NOT mention academic papers, studies, or any sources of any sort. Only answer what is asked. Stick to the topic and do NOT divert at all. Keep in mind ADDED VALUE IS NOT PROFIT. ADDED VALUE IS "Selling Price - Cost of Raw Materials" ONLY AND MENTION THIS FORMULA WHEN ASKED ABOUT ADDED VALUE. Do NOT mention "in the context of Cambridge IGCSE Business Studies Syllabus 0264 (Syllabus Edition First teaching 2018 Last exams 2026)". Keep Your Answer in BULLET FORM FORMAT DO NOT MAKE PARAGRAPHS. KEEP FORMUALS (if any) SEPERATE FROM DEFINITION UNDER THEIR OWN "Formula:" SUBHEADING.
"""

# ---------------- WEB SEARCH ----------------


def web_search(query, max_results=5):
    links = []

    try:
        with DDGS(verify=False, timeout=8) as ddgs:
            for r in ddgs.text(
                f"IGCSE Business Studies (0264) {query}",
                max_results=max_results
            ):
                links.append(r["href"])

    except Exception as e:
        return []

    return links

# ---------------- TEXT EXTRACTION ----------------


def extract_text(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:800]

    except:
        return ""


# ---------------- MAIN LOOP ----------------
while True:
    user_query = input("\nIGCSE Business Tutor ▶ Enter your question:\n")

    links = web_search(user_query)

    documents = []
    if links:
        for link in links:
            content = extract_text(link)
            if content:
                documents.append(content)

    # LIMIT CONTEXT TO AVOID MODEL COLLAPSE
    retrieved_context = "\n\n".join(
        documents) if documents else "NO_EXTERNAL_SOURCES"

    prompt = f"""
{SYSTEM_PROMPT}

REFERENCE MATERIAL:
{retrieved_context}

QUESTION:
{user_query}
"""

    response = llm.invoke(prompt)

    print("\nTutor Answer:\n")
    print(response.content)
# END OF CODE
