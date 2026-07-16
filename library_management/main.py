from fastapi import FastAPI

from apis.books_api import router as books_router
from apis.members_api import router as members_router
from apis.reports_api import router as reports_router

app = FastAPI(title="Library Management Mini Project")

app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(members_router, prefix="/members", tags=["members"])
app.include_router(reports_router, prefix="/reports", tags=["reports"])


@app.get("/")
def read_root() -> dict:
    return {"message": "Library Management API is running"}
