from fastapi import FastAPI

from apis.books import router as books_router
from apis.members import router as members_router
from apis.transactions import router as transactions_router

app = FastAPI(
    title="Library Management System",
    description="A beginner-friendly library management API using FastAPI and in-memory storage.",
    version="1.0.0",
)

app.include_router(books_router, prefix="/books", tags=["Books"])
app.include_router(members_router, prefix="/members", tags=["Members"])
app.include_router(transactions_router, prefix="/transactions", tags=["Transactions"])


@app.get("/")
def root() -> dict:
    return {"message": "Welcome to the Library Management System"}
