# Supply Chain Control Copilot

## Overview
**Supply Chain Control Copilot** is a **cloud-based AI assistant** that helps supply chain teams **monitor risks, detect delays, and optimize inventory** — all without running anything locally.  
It combines **LLM orchestration**, **multi-agent systems**, and **retrieval-augmented generation (RAG)** to turn raw supply chain data into **actionable decisions**.

This repo is a **full working demo** that runs in **mock mode** without keys, but can switch to live mode by adding API credentials for popular tools like **Together AI**, **Fireworks.ai**, **MongoDB Atlas Vector Search**, **Voyage AI**, **Arcade.dev**, **CrewAI**, and **LangSmith**.

---

## Why it matters
- **Proactive Supply Chain Management** — Identify supplier risks before they cause disruption.  
- **Automated Escalations** — Trigger carrier/buyer alerts without human intervention.  
- **Smarter Inventory Planning** — Predict shortages and recommend restocks using multi-agent logic.  
- **Scalable Architecture** — Works as a prototype in days, scales to production-ready with minimal changes.

---

## Key Features
1. **Supplier Risk Analysis (RAG + Orchestration)**
   - Pulls insights from contracts, scorecards, and live news feeds.  
   - Can run via **LangChain** or **LlamaIndex** pipelines.  
   - Outputs: risk score, top risks, recommended actions, and sources.

2. **Shipment Delay Detection & Escalation (Agentic AI)**
   - Compares planned vs actual shipment timelines.  
   - If late and breaching SLA, drafts and sends escalation email via **Arcade.dev**.

3. **Inventory Restock Recommendations (Multi-Agent)**
   - Uses **CrewAI** to simulate roles: Researcher, Analyst, and Action Agent.  
   - Calculates order quantities based on stock, safety stock, lead time, and forecast.

4. **Mock Mode for Instant Demo**
   - Returns realistic JSON responses even without API keys.  
   - Perfect for showing recruiters or stakeholders a live API on Day 1.

---

## Tech Stack
- **API Layer:** FastAPI + Pydantic  
- **LLM Hosting:** Together AI / Fireworks.ai  
- **Orchestration:** LangChain / LlamaIndex  
- **Vector Search (RAG):** MongoDB Atlas Vector Search  
- **Embeddings:** Voyage AI  
- **Agentic Actions:** Arcade.dev  
- **Multi-Agent:** CrewAI  
- **Monitoring:** LangSmith / Galileo  

---

## Endpoints (Full App Surface)

### Suppliers
- `POST /suppliers/risk-rag` – Supplier risk via RAG prompt (mock until DB configured)  
- `POST /suppliers/risk-langchain` – Same via LangChain (mock unless `LANGCHAIN_REAL=1`)  
- `POST /suppliers/risk-llamaindex` – Same via LlamaIndex (mock unless `LLAMAINDEX_REAL=1`)  

### Shipments
- `POST /shipments/escalate` – Delay escalation workflow with email send (mock unless `ARCADE_API_KEY` set)  

### Inventory
- `POST /inventory/restock` – Multi-agent restock simulation (mock unless `CREWAI_REAL=1`)  

---

## Environment Flags (Mock → Real Mode)

| Feature                | Env Vars Needed |
|------------------------|-----------------|
| LLM Calls              | `MODEL_PROVIDER` (`together` or `fireworks`) + API key |
| RAG                    | `MONGODB_URI`, `VOYAGE_API_KEY` |
| LangChain Pipeline     | `LANGCHAIN_REAL=1` |
| LlamaIndex Pipeline    | `LLAMAINDEX_REAL=1` |
| Email Actions          | `ARCADE_API_KEY` |
| Multi-Agent Restock    | `CREWAI_REAL=1` |
| Monitoring             | `LANGSMITH_API_KEY` |

---

## Quick Start
1. **Fork** this repo.  
2. Deploy to **Railway** or **Render** from GitHub.  
3. Without any keys, all endpoints work in mock mode.  
4. Add API keys as you go to switch to real data and actions.

---

## Deployment
- **Railway**: New Project → Deploy from GitHub → set env vars → Deploy  
- **Render**: New Web Service → GitHub → set env vars → Deploy  
- Open `/docs` for Swagger UI.

---

## License
MIT
