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