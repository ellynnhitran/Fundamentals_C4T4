from flask import *
import mlab
from models.food import Food
app = Flask(__name__)

mlab.connect()
  
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pagecon")
def pagecon():
    return render_template("pagecon.html")

if __name__ == "__main__":
    app.run(debug=True)