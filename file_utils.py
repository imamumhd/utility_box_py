def save_to_file(filename, text):
    file = open(filename, "a")
    file.write(text + "\n")
    file.close()
    print("Text saved!")


def read_from_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    print("File content:")
    print(content)
    return content
