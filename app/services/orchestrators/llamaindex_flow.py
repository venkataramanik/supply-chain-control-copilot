import os
def supplier_risk_with_llamaindex(question: str, retrieved_chunks: list) -> dict:
    # Safe mock unless LLAMAINDEX_REAL set
    if not os.getenv("LLAMAINDEX_REAL"):
        return {
            "risk_score": 62,
            "top_risks": ["Port delays", "Quality incidents"],
            "recommended_actions": ["Dual-source", "Expedite critical lanes"],
            "confidence": 0.78
        }
    # TODO: Implement LlamaIndex QueryEngine/ComposableGraph pipeline
    return {
        "risk_score": 61,
        "top_risks": ["TBD"],
        "recommended_actions": ["TBD"],
        "confidence": 0.75
    }
