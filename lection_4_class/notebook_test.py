from notebook import Notebook, Note

if __name__ == '__main__':
    notebook = Notebook()
    notebook.new_note("Cool memo", "#tag #tags")
    print(notebook.notes[0])
    for note in notebook.notes:
        assert isinstance(note, Note)
    assert isinstance(notebook, Notebook)
    print("Methods: ", dir(notebook))
    print("Methods: ", dir(notebook.notes[0]))
    print("Attributes: ", notebook.__dict__)
    print("Attributes: ", notebook.notes[0].__dict__)
    print("There are no errors. Thank You!")