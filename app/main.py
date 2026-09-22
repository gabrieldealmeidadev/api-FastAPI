from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.user_model import User

# Create the database tables
from app.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)


app = FastAPI()

# Include the user router
app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "API funcionando!"
    }