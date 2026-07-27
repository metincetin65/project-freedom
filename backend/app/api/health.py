from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "Project Freedom",
        "version": "0.1.0"
    }