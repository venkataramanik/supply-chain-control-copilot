from pydantic import BaseModel, Field
from typing import List, Optional

class SupplierRiskRequest(BaseModel):
    supplier_name: str = Field(..., min_length=1)
    question: str = Field(..., min_length=3)

class SourceItem(BaseModel):
    type: str
    title: str
    url: str

class SupplierRiskResponse(BaseModel):
    risk_score: int
    top_risks: List[str]
    recommended_actions: List[str]
    sources: List[SourceItem]
    confidence: float
    note: Optional[str] = None

class ShipmentEscalationRequest(BaseModel):
    shipment_id: str
    carrier: str
    expected_arrival: str  # ISO date string for simplicity

class ShipmentEscalationResponse(BaseModel):
    action_taken: str
    email_id: str
    next_steps: str
    note: Optional[str] = None
