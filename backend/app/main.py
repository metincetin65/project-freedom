from fastapi import FastAPI

app = FastAPI(
    title="Project Freedom",
    description="Open Source AI Productivity Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "project": "Project Freedom",
        "status": "running",
        "version": "0.1.0"
    }