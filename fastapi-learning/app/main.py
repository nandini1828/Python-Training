from fastapi import FastAPI,status,Body
from app import pyd
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Home"}


@app.get("/about")
def about():
    return {"message": "About API"}


@app.get("/number")
def number():
    return 100

 
@app.get("/fruits")
def fruits():
    return [
        "Apple",
        "Orange",
        "Banana"
    ]


@app.get("/employee")
def employee():

    return {

        "id":101,

        "name":"Rahul",

        "address":{

            "city":"Hyderabad",

            "state":"Telangana"

        }

    }



@app.post("/employee",status_code=status.HTTP_201_CREATED)
def create_employee():

    return {

        "message":"Employee Created"

    }

#path parameters
@app.get("/students/{course}/{student_id}")
def student(course:str,student_id:int):

    return {

        "course":course,

        "student":student_id

    }


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(payload: pyd.Item = Body(...)):
    # payload will capture any JSON sent in the request body
    item_name = payload.name
    item_price = payload.price

    return {
        "success": True,
        "message": f"Item '{item_name}' created successfully!",
        "data": payload
    }


#query parameters
@app.get("/productss")
def products(page:int=1):

    return {

        "page":page

    }


@app.get("/department/{dept_id}")
def department(

dept_id:int,

page:int=1

):

    return{

        "department":dept_id,

        "page":page

    }