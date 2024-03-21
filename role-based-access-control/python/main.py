import time
from inventory.inventory import load_inventory
from sys import argv
from handler.util import (
    add_permission,
    create_user,
    add_role,
    check_user_permission,
    remove_permission,
    remove_role,
)
from constant.my_enums import StatusEnum


def main():
    data_store = load_inventory()
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, "r")
    Lines = f.readlines()
    TOTAL, CORRECT, WRONG = 0, 0, 0
    for line in Lines:
        TOTAL += 1
        command = line.rstrip("\n").split(" ")
        if command[0] == "ADD_PERMISSION":
            if add_permission(command=command, data_store=data_store).value != int(
                command[-1]
            ):
                # print("Wrong Answer:", command)
                WRONG += 1
            else:
                CORRECT += 1
                # print("Correct Answer:", command)
        elif command[0] == "REMOVE_PERMISSION":
            if remove_permission(command=command, data_store=data_store).value != int(
                command[-1]
            ):
                WRONG += 1
                # print("Wrong Answer:", command)
            else:
                CORRECT += 1
                # print("Correct Answer:", command)
        elif command[0] == "CREATE_USER":
            if create_user(command=command, data_store=data_store).value != int(
                command[-1]
            ):
                WRONG += 1
                # print("Wrong Answer:", command)
            else:
                CORRECT += 1
                # print("Correct Answer:", command)
        elif command[0] == "ADD_ROLE":
            if add_role(command=command, data_store=data_store).value != int(
                command[-1]
            ):
                WRONG += 1
                # print("Wrong Answer:", command)
            else:
                CORRECT += 1
                # print("Correct Answer:", command)
        elif command[0] == "REMOVE_ROLE":
            if remove_role(command=command, data_store=data_store).value != int(
                command[-1]
            ):
                WRONG += 1
                # print("Wrong Answer:", command)
            else:
                CORRECT += 1
                # print("Correct Answer:", command)
        elif command[0] == "CHECK_USER_PERMISSION":
            if check_user_permission(
                command=command, data_store=data_store
            ).value != int(command[-1]):
                WRONG += 1
                # print("Wrong Answer:", command)
            else:
                CORRECT += 1
                # print("Correct Answer:", command)
            pass
        else:
            print("Wrong Input")
    print("Total => ", TOTAL)
    print("Correct => ", CORRECT)
    print("Wrong => ", WRONG)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Total Time:", end_time - start_time)
