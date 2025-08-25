try:
    name = input("Enter your file name: ")
    file = open(name, "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

    