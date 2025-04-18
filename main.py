from fastapi import FastAPI
# from app.routes import user

app = FastAPI()

# app.include_router(user.router, prefix="/users", tags=["Users"])

@app.get("/users")
def read_root():
    return {"message": "Welcome to the FastAPI Boilerplate!"}
