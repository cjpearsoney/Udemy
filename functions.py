FILEPATH = 'todos.txt'

def get_tados(filepath=FILEPATH):
    """this function opens the file
    and reads the list data out
    to a return variable for use later"""
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos

def write_tados(todos_arg, filepath=FILEPATH):
    """this function opens the file
    and writes the input variable back to the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
