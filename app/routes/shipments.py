from fastapi import APIRouter
from app.models.schemas import ShipmentEscalationRequest, ShipmentEscalationResponse
from app.services.agents.arcade_actions import send_email

router = APIRouter()

@router.post("/escalate", response_model=ShipmentEscalationResponse)
def escalate(req: ShipmentEscalationRequest):
    subject = f"SLA Breach Alert – Shipment {req.shipment_id} ({req.carrier})"
    body = f"""Hello Carrier Team,

Shipment {req.shipment_id} is late vs SLA. Expected arrival: {req.expected_arrival}.
Please confirm recovery action within 4 hours.

Thanks,
Supply Chain Control Copilot"""
    email_id = send_email("carrier@example.com", subject, body)
    return ShipmentEscalationResponse(
        action_taken="email_sent",
        email_id=email_id,
        next_steps="Carrier to confirm recovery plan in 4h",
        note="Arcade call mocked unless ARCADE_API_KEY is set"
    )
