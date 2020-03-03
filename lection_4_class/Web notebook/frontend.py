from flask import Flask, render_template, request, url_for
from main import Menu


menu = Menu()
menu.add_note("First note", "#cool # first")
menu.add_note("Second note", "#not # cool")
index_to_edit = -1

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
        notes = menu.return_notes()
    return render_template("index.html", notes=notes)


@app.route('/add/')
def result():
    notes = menu.return_notes()
    return render_template("add_note.html", notes=notes)


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    notes = menu.return_notes()
    if request.method == 'POST':
        global index_to_edit
        if 'submit_button' in request.form:
            button_info = request.form['submit_button']
            for i in range(1, len(menu.return_notes()) + 2):
                if button_info == f"Edit note №{i}":
                    index_to_edit = i
                    print(index_to_edit, "SUCESS!!!!!!!!!!!!!!!")
                    return render_template("edit_note.html")
                if button_info == f"Delete №{i}":
                    menu.notebook.notes = menu.notebook.notes[:i - 1] + \
                                          menu.notebook.notes[i:]
                    notes = menu.return_notes()
                    print("HERE", i)
                    print(notes)
                    return render_template("index.html", notes=notes)
        else:
            notes = menu.return_notes()

            menu.modify_note(index_to_edit,
                             request.form['memo'], request.form['tags'])
            notes = menu.return_notes()

            return render_template("index.html", notes=notes)




if __name__ == '__main__':
    app.run(debug=True)
