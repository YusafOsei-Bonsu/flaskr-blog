# Importing flask
from flask import Flask

# Flask instance
app = Flask(__name__)

# Entering 127.0.0.1:5000 in the address bar will show "Hello, World!"
@app.route('/')
def hello():
    return 'Hello, World!'