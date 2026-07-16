"""
main.py

Application entry point.
"""

from fastapi import FastAPI

from app.api.product_api import router as product_router
from app.api.user_api import router as user_router
from app.api.cart_api import router as cart_router
from app.api.order_api import router as order_router

app = FastAPI(
    title="E-Commerce Backend",
    version="1.0.0",
)

# Register all routers
app.include_router(product_router)
app.include_router(user_router)
app.include_router(cart_router)
app.include_router(order_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to E-Commerce Backend"
    }