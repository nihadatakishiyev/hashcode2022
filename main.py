from os import listdir
from os.path import isfile, join

files = list()


def read_input_files():
    global files
    files = [f for f in listdir('in')]


def write_to_files():
    for f in files:
        file = open('in/'+f)
        writable = open('out/'+f, 'w')
        writable.write(file.read())


if __name__ == '__main__':
    read_input_files()
    print(files)
    write_to_files()
