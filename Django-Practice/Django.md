Django REST Framework CRUD API using ModelViewSet

Project Name

Django-Practice

⸻

Objective

The objective of this project is to learn how to build RESTful CRUD APIs using Django and Django REST Framework (DRF). The project demonstrates the use of ModelViewSet to automatically generate Create, Read, Update, and Delete operations for multiple models.

⸻

Technologies Used

* Python
* Django
* Django REST Framework (DRF)
* SQLite (Default Database)

⸻

Project Structure

Django-Practice/
│
├── api/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── requirements.txt

⸻

What We Implemented

1. Created a Django Project

* Created a new Django project named Django-Practice.
* Created a virtual environment.
* Installed Django and Django REST Framework.
* Configured the project settings.

⸻

2. Created a Django App

Created an application named api.

Added the following applications to INSTALLED_APPS:

'rest_framework',
'api',

⸻

3. Created Models

Three database models were created.

Department

Represents a department inside an organization.

Fields:

* id
* name
* location

⸻

Employee

Represents an employee.

Fields:

* id
* name
* email
* age
* department (ForeignKey)

Relationship:

One Department
        │
        ├── Employee 1
        ├── Employee 2
        └── Employee 3

⸻

Project

Represents a project assigned to an employee.

Fields:

* id
* title
* description
* employee (ForeignKey)

Relationship:

One Employee
      │
      ├── Project 1
      ├── Project 2
      └── Project 3

⸻

4. Database Migration

Generated migration files:

python manage.py makemigrations

Applied migrations:

python manage.py migrate

This created the required database tables.

⸻

5. Registered Models in Django Admin

Registered all models inside admin.py.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)

Created a superuser using:

python manage.py createsuperuser

Verified all models through the Django Admin panel.

⸻

6. Created Serializers

Created serializers.py.

Implemented the following serializers:

* DepartmentSerializer
* EmployeeSerializer
* ProjectSerializer

Each serializer inherits from ModelSerializer.

Example:

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

Purpose:

* Converts Model → JSON
* Converts JSON → Model

⸻

7. Created ViewSets

Implemented CRUD operations using ModelViewSet.

Created:

* DepartmentViewSet
* EmployeeViewSet
* ProjectViewSet

Example:

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

Each ViewSet automatically provides:

* Create
* Read
* Update
* Delete

No separate functions for GET, POST, PUT, PATCH, or DELETE were required.

⸻

8. Configured Routing

Created api/urls.py.

Used DefaultRouter to automatically generate REST API URLs.

router = DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("employees", EmployeeViewSet)
router.register("projects", ProjectViewSet)
urlpatterns = router.urls

Connected the app URLs inside the project.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]

⸻

API Endpoints

Department

GET     /api/departments/
POST    /api/departments/
GET     /api/departments/<id>/
PUT     /api/departments/<id>/
PATCH   /api/departments/<id>/
DELETE  /api/departments/<id>/

⸻

Employee

GET     /api/employees/
POST    /api/employees/
GET     /api/employees/<id>/
PUT     /api/employees/<id>/
PATCH   /api/employees/<id>/
DELETE  /api/employees/<id>/

⸻

Project

GET     /api/projects/
POST    /api/projects/
GET     /api/projects/<id>/
PUT     /api/projects/<id>/
PATCH   /api/projects/<id>/
DELETE  /api/projects/<id>/

⸻

CRUD Operations Supported

HTTP Method	Operation
GET	Retrieve data
POST	Create new record
PUT	Update entire record
PATCH	Update selected fields
DELETE	Remove a record

⸻

Key Concepts Learned

* Creating a Django project
* Creating Django apps
* Defining models
* Database migrations
* ForeignKey relationships
* Registering models in Django Admin
* Creating serializers
* Using ModelSerializer
* Creating APIs using ModelViewSet
* Using DefaultRouter
* Building RESTful CRUD APIs
* Working with JSON requests and responses

⸻

Conclusion

This project demonstrates the implementation of a complete REST API using Django REST Framework. Three related models (Department, Employee, and Project) were created, serialized using ModelSerializer, and exposed as CRUD APIs using ModelViewSet. Routing was simplified with DefaultRouter, allowing all CRUD endpoints to be generated automatically with minimal code.