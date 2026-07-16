from fastapi import FastAPI

from app.apis.product import router as product_router
from app.apis.customer import router as customer_router
from app.apis.cart import router as cart_router
from app.apis.order import router as order_router



app = FastAPI(
    title="E-Commerce API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Welcome to E-Commerce API"}


app.include_router(product_router)
app.include_router(customer_router)
app.include_router(cart_router)
app.include_router(order_router)
