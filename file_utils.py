def save_to_file(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()
    print("File saved!")


def read_from_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    print(content)
    return content
