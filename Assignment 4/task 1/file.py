
def read_file():
    with open("/workspaces/TudeDude-Py/Assignment 4/task 1/file.txt", "r") as fh:
        try :
            print("Reading file contents...")

            for l in fh:
                print(l, end='')

        except FileNotFoundError:
            print("\nThe file does not exist.")

        else:
            print("\nDone..")

read_file()


"""
with open("/workspaces/TudeDude-Py/Assignment 4/task 1/file.txt", "r") as fh:
    print("Reading file contents...")

    for l in fh:
        print(l, end='')
"""