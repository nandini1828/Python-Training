from fastapi import APIRouter

from services.report_service import get_summary

router = APIRouter()


@router.get("/summary")
def summary_report():
    return get_summary()
