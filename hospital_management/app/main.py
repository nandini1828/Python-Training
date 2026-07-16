"""
FastAPI Application

This is the main entry point for the Hospital Management System API.

The app is structured with:
- Models: Pydantic models for data validation
- Services: Business logic and data management
- Routers: API endpoints
- Utils: Helper functions

FastAPI automatically generates interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all routers
from app.routers import patient_router, doctor_router, appointment_router


# Create FastAPI application instance
# The title appears in the API documentation
app = FastAPI(
    title="Hospital Management System API",
    description="A beginner-friendly REST API for managing patients, doctors, and appointments",
    version="1.0.0"
)


# Configure CORS (Cross-Origin Resource Sharing)
# This allows the API to be accessed from web applications on different domains
# In production, you'd restrict this to specific domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Include all routers
# Routers organize endpoints into logical groups
app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint that provides information about the API.
    
    Returns:
        Welcome message and API information.
        
    Note:
        This demonstrates a simple endpoint that returns JSON data.
    """
    return {
        "message": "Welcome to Hospital Management System API",
        "documentation": "Visit /docs for interactive API documentation",
        "version": "1.0.0"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint.
    
    Used to verify that the API is running and responding correctly.
    
    Returns:
        Status indicating the API is healthy.
    """
    return {"status": "healthy"}


# This is standard practice for running Flask/FastAPI apps
# It prevents the server from running when the file is imported
if __name__ == "__main__":
    import uvicorn
    
    # Run the application using Uvicorn ASGI server
    # host="0.0.0.0" makes it accessible from any IP
    # port=8000 is the default port
    # reload=True restarts the server when files change (useful for development)
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
