file = open("python.py.pdf", "w")
file.write("Python is a programming language.")

file = open("python.py.pdf", "r")
content = file.read()
print(content)

file = open("python.py.pdf", "w")
file.write("Coding with Python is fun. Python is a programming language.")

file = open("python.py.pdf", "r" )
content = file.read()
print(content)