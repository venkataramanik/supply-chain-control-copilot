from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List
from app.services.agents.crewai_team import run_restock_simulation

router = APIRouter()

class RestockItem(BaseModel):
    sku: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    on_hand: int
    safety_stock: int
    lead_time_days: int
    forecast_next_30d: int

class RestockRequest(BaseModel):
    items: List[RestockItem]

class RestockResponse(BaseModel):
    recommendations: List[dict]
    note: str | None = None

@router.post("/restock", response_model=RestockResponse)
def restock(req: RestockRequest):
    recs, note = run_restock_simulation([i.model_dump() for i in req.items])
    return RestockResponse(recommendations=recs, note=note)
