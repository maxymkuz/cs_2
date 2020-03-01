from flask import Flask, render_template, request, url_for
from main import Menu


menu = Menu()
menu.add_note("First note", "#cool # first")
menu.add_note("Second note", "#not # cool")

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        memo = request.form['memo']
        tags = request.form['tags']
        menu.show_notes()
        menu.add_note(memo, tags)
        notes = menu.return_notes()
        print(notes)
    else:
        print("GETTTTT")
        notes = menu.return_notes()
        print(notes)
    return render_template("index.html", notes=notes)


@app.route('/add/')
def result():
    notes = menu.return_notes()
    return render_template("add_note.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
