import os, random
from typing import List, Dict

def run_restock_simulation(items: List[Dict]):
    # If CREWAI_REAL not set, return simple deterministic recs
    if not os.getenv("CREWAI_REAL"):
        recs = []
        for it in items:
            deficit = max(0, it['safety_stock'] + it['forecast_next_30d'] - it['on_hand'])
            qty = max(deficit, 0)
            recs.append({
                "sku": it['sku'],
                "location": it['location'],
                "recommended_order_qty": qty,
                "rationale": "Cover safety stock + 30d forecast; subtract on-hand."
            })
        return recs, "CrewAI mocked unless CREWAI_REAL=1"
    # TODO: Implement CrewAI agents (Researcher/Analyst/ActionAgent) and return real recs
    return [], "CrewAI real mode not yet implemented"
