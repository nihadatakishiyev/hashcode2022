import utils
if __name__ == '__main__':
    files = utils.read_input_file_names()
    for i in files:
        data = open('src/in/'+i)
        for line in data.readlines():
            print(line)
