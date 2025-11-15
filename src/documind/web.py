from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from .main import main as run_documind


app = FastAPI(
    title="DocuMind",
    description="AI Document Intelligence Agent API",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: str
    message: str


@app.get("/", response_model=HealthResponse)
def root() -> HealthResponse:
    """Basic health/info endpoint.

    Extend this later to return app metadata, available workflows, etc.
    """

    return HealthResponse(
        status="ok",
        message=(
            "DocuMind environment initialized. Implement web workflows here."
        ),
    )


@app.post("/run")
def run_workflow() -> dict:
    """Placeholder endpoint that triggers the existing main workflow.

    Replace this with real document ingestion + agent orchestration later.
    """

    run_documind()
    return {"status": "ok", "detail": "DocuMind workflow triggered (placeholder)."}
