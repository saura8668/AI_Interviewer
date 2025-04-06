from typing import Union
from fastapi import FastAPI
from api.v1.endpoints import notes
from api.v1.endpoints import questions

app = FastAPI(
    title="AI Interview API",  # Custom title for Swagger UI
    description="API for managing interview questions and notes.",  # Custom description
    version="1.0.0",  # API version
    docs_url="/docs",  # URL for Swagger UI
    redoc_url="/redoc"  # URL for ReDoc
)

# Routes
app.include_router(notes.router, prefix="/api/v1/notes", tags=["notes"])
app.include_router(questions.router, prefix="/api/v1/test", tags=["questions"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)