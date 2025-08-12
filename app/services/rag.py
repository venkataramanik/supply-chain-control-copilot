import os, json, requests
from typing import List, Dict

MONGO_URI = os.getenv("MONGODB_URI")
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")

def retrieve_chunks(query: str) -> List[Dict]:
    # For first demo, return mocked chunks if missing config
    if not (MONGO_URI and VOYAGE_API_KEY):
        return [
            {"text": "SLA requires 95% OTIF and max 48h delay allowance.", "title": "Acme SLA", "url": "https://example.com/acme-sla"},
            {"text": "Recent news indicates port congestion impacting Asia-US lanes.", "title": "Logistics News", "url": "https://news.example.com/ports"}
        ]
    # TODO: Implement actual MongoDB Atlas Vector Search + Voyage embeddings
    # Left as future work to keep the starter deployable immediately.
    return []

def build_rag_prompt(question: str, chunks: List[Dict]) -> str:
    ctx = "\n\n".join([f"- {c['title']}: {c['text']}" for c in chunks])
    prompt = f"""Use the context to answer the supply chain risk question.
Context:
{ctx}

Question: {question}

Return concise, actionable insights."""
    return prompt
