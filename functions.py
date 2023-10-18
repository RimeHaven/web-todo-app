# This is called a module

FILEPATH = "todos.txt"


def get_file(filepath=FILEPATH):
    """ Return the contents of a file """
    with open(filepath, "r") as file:
        file_var = file.readlines()
    return file_var


def write_file(arg_list, filepath=FILEPATH):
    """ Write a list to a file """
    with open(filepath, "w") as file:
        file.writelines(arg_list)


if __name__ == "__main__":
    print(get_file())
