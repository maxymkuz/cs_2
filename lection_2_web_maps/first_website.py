from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


@app.route('/andriy')
def index_andriy():
    # return '<h1 style="color:red">Andriy pidor</h1>'
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
