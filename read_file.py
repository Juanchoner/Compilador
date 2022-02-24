def read_text():
    with open("content.txt", "r") as archivo:
        data = archivo.read()
        return data
        