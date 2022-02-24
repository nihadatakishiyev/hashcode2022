import utils
if __name__ == '__main__':
    files = utils.read_input_file_names()
    print(files)
    for i in files:
        data = open('src/in/'+i)
        utils.write_to_file(i, data.read())
