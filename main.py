from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="RAG Testing API")

class TestRunRequest(BaseModel):
    endpoint_url: str
    test_doc_path: str

class TestRunResponse(BaseModel):
    status: str
    message: str
    tests_executed: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/test-run")
def run_tests(request: TestRunRequest):
    return TestRunResponse(
        status="success",
        message="RAG testing scaffold ready",
        tests_executed=0
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)