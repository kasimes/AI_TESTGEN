from fastapi import FastAPI

app = FastAPI()

@app.get("/user/list")
def list_users():
    return {"users": ["Alice", "Bob", "Charlie"]}



@app.post("/user/create")
def create_user(name: str):
    return {"message": f"User {name} created successfully"}

@app.delete("/user/delete/{user_id}")
def delete_user(user_id: int):
    return {"message": f"User with ID {user_id} deleted successfully"}