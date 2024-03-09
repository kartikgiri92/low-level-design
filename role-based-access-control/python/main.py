from inventory.inventory import load_inventory
from sys import argv
from handler.util import add_permission, create_user, add_role, check_user_permission
from constant.my_enums import StatusEnum


def main():
    data_store = load_inventory()
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, "r")
    Lines = f.readlines()
    for line in Lines:
        command = line.rstrip("\n").split(" ")
        if command[0] == "ADD_PERMISSION":
            if add_permission(command=command, data_store=data_store).value != int(
                command[-1]
            ):
                print("Wrong Answer:", command)
            else:
                print("Correct Answer:", command)
        elif command[0] == "CREATE_USER":
            if create_user(command=command, data_store=data_store).value != int(
                command[-1]
            ):
                print("Wrong Answer:", command)
            else:
                print("Correct Answer:", command)
        elif command[0] == "ADD_ROLE":
            if add_role(command=command, data_store=data_store).value != int(
                command[-1]
            ):
                print("Wrong Answer:", command)
            else:
                print("Correct Answer:", command)
        elif command[0] == "CHECK_USER_PERMISSION":
            if check_user_permission(
                command=command, data_store=data_store
            ).value != int(command[-1]):
                print("Wrong Answer:", command)
            else:
                print("Correct Answer:", command)
            pass
        else:
            print("Wrong Input")


if __name__ == "__main__":
    main()
