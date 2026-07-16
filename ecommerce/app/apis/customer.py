from fastapi import APIRouter, HTTPException

from app.models.request_models import CustomerRequest
from app.services.customer_service import CustomerService
from app.utils.exceptions import CustomerNotFound

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get("/")
def get_customers():
    return CustomerService.get_all_customers()


@router.get("/{customer_id}")
def get_customer(customer_id: int):

    try:
        return CustomerService.get_customer(customer_id)

    except CustomerNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.post("/")
def add_customer(customer: CustomerRequest):

    return CustomerService.add_customer(
        customer.name,
        customer.email,
        customer.phone,
        customer.address
    )


@router.put("/{customer_id}")
def update_customer(customer_id: int, customer: CustomerRequest):

    try:
        return CustomerService.update_customer(
            customer_id,
            name=customer.name,
            email=customer.email,
            phone=customer.phone,
            address=customer.address
        )

    except CustomerNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/{customer_id}")
def delete_customer(customer_id: int):

    try:
        return CustomerService.delete_customer(customer_id)

    except CustomerNotFound as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )