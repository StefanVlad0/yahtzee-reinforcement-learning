import os


def load_text(source):
    if os.path.isfile(source):
        # read from file
        with open(source, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        # read from command line
        return source
