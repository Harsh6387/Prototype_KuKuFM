# Chatbot Microservice (FastAPI)

## Overview
This project sets up a **FastAPI-based chatbot microservice** running on **VM3**, which can be consumed by other services such as a frontend UI or external systems. It is a core part of a microservice architecture designed for intelligent, conversational interactions using a lightweight and modular backend.

---

## Architecture
- **Microservice Location**: VM3
- **API Base URL**: `http://192.168.100.1:8000/`
- **Framework**: FastAPI
- **Primary Functionality**: Exposes a chatbot endpoint that can be used for recommendations, summaries, or content suggestions.

---

## Features
- Stateless REST API for chatbot interactions
- JSON-based communication
- Easy to integrate with frontend or other microservices

---

## Setup Instructions

### 1. System Requirements
- Python 3.8+
- `pip` package manager
- Linux-based VM (e.g., Ubuntu)

### 2. Environment Configuration (VM3)

#### Update Netplan for Internal Network
```bash
sudo nano /etc/netplan/01-netcfg.yaml
```
Add the following configuration:
```yaml
network:
  version: 2
  ethernets:
    enp0s8:
      addresses:
        - 192.168.100.1/24
```
Apply the changes:
```bash
sudo netplan apply
```

### 3. Backend Setup

#### Clone the Repository
```bash
git clone -b main <repository_url>
cd <repository_directory>
```

#### Create Virtual Environment and Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Example FastAPI App (app.py)
```python
from fastapi import FastAPI, Request
from pydantic import BaseModel
import socket

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
async def chat(query: Query):
    response = f"You said: {query.message}. Response from {socket.gethostname()}"
    return {"response": response}
```

#### Run the FastAPI Server
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 2
```

---

## API Specification

### POST `/chat`
- **Request Body**:
```json
{
  "message": "Suggest me something for my mood."
}
```
- **Response**:
```json
{
  "response": "You said: Suggest me something for my mood. Response from chatbot-host"
}
```

---

## Testing
1. Using `curl` from any device on the same network:
```bash
curl -X POST http://192.168.100.1:8000/chat -H "Content-Type: application/json" -d '{"message": "Hello!"}'
```

2. You can also connect this endpoint with a Flask-based frontend running on another VM (e.g., VM4).

---

## Future Enhancements
- Integration with LLMs for natural language responses
- Rate limiting and auth tokens
- Docker and CI/CD pipeline
- Load balancing and horizontal scaling

---

## License
This project is licensed 

---

## Maintainers
- Backend Architect: Harsh Pratap Singh
- AI Model Integration: Harsh Pratap Singh
- DevOps & Deployment: Harsh Pratap Singh
