import os

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return its content as a list of separeted lines"""
    if not os.path.exists(filepath):
        with open(filepath,'w') as file_local:
            pass

    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return  todos_local

def save_todos(datalist, filepath=FILEPATH):
    """Write a text file from the contents of a list"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(datalist)

def show_todos(datalist):
    """Print the contents of a list, each of them numerated"""
    if len(datalist) == 0 :
                print("The list has 0 elements to show.")
    else :
        print ("Current List")
        for index, item in enumerate(datalist):
            print(f"{index + 1} -{item.capitalize().strip("\n")}")


if __name__ == '__main__':
     print('Testing fuctions for the To-Do App')
     print(get_todos())