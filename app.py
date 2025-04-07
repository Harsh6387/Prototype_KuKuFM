from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": f"Hello from {socket.gethostname()}!"}