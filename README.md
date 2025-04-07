# 

## Overview
This project demonstrates a simple **microservice-based architecture** using two virtual machines (**VM3** and **VM4**) connected via an internal network.

- **VM3 (Backend)**: Runs a FastAPI-based microservice.
- **VM4 (Frontend)**: Runs a Flask-based UI that fetches data from VM3.

## Architecture
- **VM3 IP Address**: `192.168.100.1`
- **VM4 IP Address**: `192.168.100.2`
- **Backend API URL**: `http://192.168.100.1:8000/`
- **Frontend UI URL**: `http://192.168.100.2:5000/`

## Setup Instructions

### 1. Configure Networking
Run the following on **VM3**:
```bash
sudo nano /etc/netplan/01-netcfg.yaml
```
Add:
```yaml
network:
  version: 2
  ethernets:
    enp0s8:
      addresses:
        - 192.168.100.1/24
```
Apply changes:
```bash
sudo netplan apply
```

### 2. Backend Setup (FastAPI on VM3)
```bash
mkdir app && cd app
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```
Create `app.py`:
```python
from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": f"Hello from {socket.gethostname()}!"}
```
Run the server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 2
```

### 3. Frontend Setup (Flask on VM4)
```bash
mkdir app2 && cd app2
python3 -m venv venv
source venv/bin/activate
pip install flask requests
```
Create `ui.py`:
```python
from flask import Flask
import requests

app = Flask(__name__)
API_URL = "http://192.168.100.1:8000/"

@app.route("/")
def home():
    try:
        response = requests.get(API_URL)
        message = response.json().get("message", "No response")
    except:
        message = "VM3 is unreachable!"
    
    return f"<html><body><h2>Response from VM3:</h2><p>{message}</p></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
Run the UI:
```bash
python3 ui.py
```

## Testing
1. Test the backend:
   ```bash
   curl http://192.168.100.1:8000/
   ```
2. Open the frontend in a browser:
   ```
   http://192.168.100.2:5000/
   ```
   - It should display `Hello from VM3!`


