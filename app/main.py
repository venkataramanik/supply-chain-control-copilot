from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.routes import suppliers, shipments
import os

app = FastAPI(title="Supply Chain Control Copilot", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

# include routers
app.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
app.include_router(shipments.router, prefix="/shipments", tags=["shipments"])

from app.routes import inventory
app.include_router(inventory.router, prefix="/inventory", tags=["inventory"])\n