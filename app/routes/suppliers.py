from fastapi import APIRouter, HTTPException
from app.models.schemas import SupplierRiskRequest, SupplierRiskResponse, SourceItem
from app.services import rag, llm_client
import json, re

router = APIRouter()

@router.post("/risk-rag", response_model=SupplierRiskResponse)
def supplier_risk_rag(req: SupplierRiskRequest):
    chunks = rag.retrieve_chunks(req.question)
    prompt = rag.build_rag_prompt(req.question, chunks)
    llm_out = llm_client.generate(prompt, max_tokens=300)

    # very simple heuristic parse for demo
    top_risks = ["Port congestion", "Quality incidents"]
    recommended = ["Increase safety stock", "Dual-source critical SKUs"]
    sources = [SourceItem(type="doc", title=c.get("title",""), url=c.get("url","")) for c in chunks]
    return SupplierRiskResponse(
        risk_score=62,
        top_risks=top_risks,
        recommended_actions=recommended,
        sources=sources,
        confidence=0.78,
        note="Mocked scoring until MongoDB/Voyage configured"
    )


from app.services.orchestrators.langchain_flow import supplier_risk_with_langchain
from app.services.orchestrators.llamaindex_flow import supplier_risk_with_llamaindex

@router.post("/risk-langchain", response_model=SupplierRiskResponse)
def supplier_risk_langchain(req: SupplierRiskRequest):
    chunks = rag.retrieve_chunks(req.question)
    out = supplier_risk_with_langchain(req.question, chunks)
    sources = [SourceItem(type="doc", title=c.get("title",""), url=c.get("url","")) for c in chunks]
    return SupplierRiskResponse(
        risk_score=out["risk_score"],
        top_risks=out["top_risks"],
        recommended_actions=out["recommended_actions"],
        sources=sources,
        confidence=out["confidence"],
        note="LangChain mocked unless LANGCHAIN_REAL=1"
    )

@router.post("/risk-llamaindex", response_model=SupplierRiskResponse)
def supplier_risk_llamaindex(req: SupplierRiskRequest):
    chunks = rag.retrieve_chunks(req.question)
    out = supplier_risk_with_llamaindex(req.question, chunks)
    sources = [SourceItem(type="doc", title=c.get("title",""), url=c.get("url","")) for c in chunks]
    return SupplierRiskResponse(
        risk_score=out["risk_score"],
        top_risks=out["top_risks"],
        recommended_actions=out["recommended_actions"],
        sources=sources,
        confidence=out["confidence"],
        note="LlamaIndex mocked unless LLAMAINDEX_REAL=1"
    )
