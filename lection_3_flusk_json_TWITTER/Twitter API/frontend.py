from flask import Flask, render_template, request
from secret_keys import keys
from backend import make_map, get_location_name


app = Flask(__name__)


@app.route("/")
def index():
    return  render_template("index.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        username = request.form['username']
        users = get_location_name(username, keys)
        make_map(users)
    return render_template("map.html")


app.run(debug=True)