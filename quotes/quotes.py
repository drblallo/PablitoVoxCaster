
def get_quotes(path):
    with open(path, "r") as f:
        return f.readlines()
