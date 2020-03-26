from main import Menu

n = Menu()
n.add_note("Qwerty", "#Insta")
n.add_note("Asdas", "#ass")
n.show_notes()

print()
print(n.search_notes("Insta"))

n.modify_note(1, "New text", "dfhz")
n.show_notes()

