from fastapi import FastAPI

app = FastAPI()

@app.get("/user/list")
def list_users():
    return {"users": ["Alice", "Bob", "Charlie"]}



@app.post("/user/create")
def create_user(name: str):
    return {"message": f"User {name} created successfully"}