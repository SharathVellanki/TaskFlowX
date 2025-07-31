from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, task

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "TaskFlowX backend is running"}

# TEMP: Create tables if they don't exist
from app.services.database import Base, engine
from app.models import user, task
Base.metadata.create_all(bind=engine)



from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="TaskFlowX API",
        version="1.0.0",
        description="Workflow automation backend with JWT auth",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

