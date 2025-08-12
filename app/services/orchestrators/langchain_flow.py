import os
def supplier_risk_with_langchain(question: str, retrieved_chunks: list) -> dict:
    # Safe mock unless LANGCHAIN_REAL set
    if not os.getenv("LANGCHAIN_REAL"):
        return {
            "risk_score": 58,
            "top_risks": ["Supplier financial stress", "Logistics congestion"],
            "recommended_actions": ["Increase safety stock", "Qualify backup vendor"],
            "confidence": 0.73
        }
    # TODO: Implement real LangChain graph with retriever, LLM, and structured output parser
    return {
        "risk_score": 60,
        "top_risks": ["TBD"],
        "recommended_actions": ["TBD"],
        "confidence": 0.7
    }
