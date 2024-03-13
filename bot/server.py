from flask import Flask

# Lil flasky app pookie bear
app = Flask(__name__)


# Good ol hello world equivalent right here
@app.route('/')
def index():
      return "Bot up and running"


# A nice function for our bff threads
def run_flask():

    # Run the flask app
    app.run(host="0.0.0.0", debug=False, port=8080)

