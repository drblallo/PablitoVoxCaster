def split_every(string, count):
    while string:
        yield string[:count]
        string = string[count:]
