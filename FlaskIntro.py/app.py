#1 Create Flask App
from flask import Flask #Flask is a class

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello C4T4, this is homepage"

@app.route("/about-me")
def about_me():
    return "My name is Nhi. I'm in grade 12th. A true bookworm."

@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name + " :>"

#2 Run app
if __name__ == "__main__":
    app.run(debug=True)