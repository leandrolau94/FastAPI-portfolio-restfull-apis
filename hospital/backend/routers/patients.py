from fastapi import APIRouter

patients_router = APIRouter(
    prefix="/patients",
    tags=["patients"],
)