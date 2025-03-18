import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Received request to /")  # Debug log
    return "Hello, World!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    print(f"Starting Flask on port {port}...")  # Debug log
    app.run(host="0.0.0.0", port=port)
