from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="Api-Py",
    description="API for Python and SQL management",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "users methods"
    }]
)

app.include_router(user)
