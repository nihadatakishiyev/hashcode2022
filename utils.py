from os import listdir


def read_input_file_names():
    return [f for f in listdir('in')]


def write_to_file(file, content):
    writable = open('out/' + file, 'w')
    writable.write(content)
