from document import Character, Cursor, Document

doc = Document()
cursor = Cursor(doc)

assert isinstance(doc, Document)
assert isinstance(cursor, Cursor)
assert cursor.document == doc

m = Character('m', bold=True)
a = Character('a')
x = Character('x', underline=True)
y = Character('y')
assert isinstance(m, Character)
assert m.character == 'm'

doc.insert(m)
cursor.forward()
doc.insert(a)
doc.insert(a)
cursor.forward()
cursor.forward()
doc.insert(x)
cursor.end()
doc.insert(x)
cursor.end()
cursor.forward()
cursor.back()
doc.delete()
doc.insert(y)

assert doc.string == "|B:maa|U:xy"

print("Testing is done successfullt")
