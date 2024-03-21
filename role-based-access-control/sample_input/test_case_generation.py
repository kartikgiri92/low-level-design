import random
import string
import time

TOTAL_START_TIME = time.time()


FILE_NAME = "input_large.txt"

# GLOBAL DATA
NUMER_OF_LINES = 50000
BATCH_SAVE = 10000
BATCH_DATA = []
ALL_PERMISSIONS = [
    "DefaultPermission1",
    "DefaultPermission2",
    "AdminPermission1",
    "AdminPermission2",
]
ALL_ROLES = ["Admin", "Customer", "Owner"]
ALL_OPERATIONS = [
    "ADD_PERMISSION",
    "CREATE_USER",
    "ADD_ROLE",
    "CHECK_USER_PERMISSION",
    "REMOVE_ROLE",
    "REMOVE_PERMISSION",
]

current_user = {}
current_role = {"Admin": set(), "Customer": set(), "Owner": set()}

# Main Generation Code
f = open(FILE_NAME, "w")
f.close()


def write_to_file(BATCH_DATA):
    start_time = time.time()
    with open(FILE_NAME, "a") as f:
        f.write("".join(BATCH_DATA))
    end_time = time.time()
    time_taken = end_time - start_time
    print(
        "ENVs Written:",
        len(BATCH_DATA),
        "Time taken to write to file:",
        time_taken,
        "seconds",
    )


def generate_random_string(length):
    # Define the characters that can be used in the random string
    characters = string.ascii_letters

    # Generate a random string of the specified length
    random_string = "".join(random.choice(characters) for _ in range(length))

    return random_string


for i in range(1, NUMER_OF_LINES + 1):
    commands = []

    operation_chosen = random.choice(ALL_OPERATIONS)
    commands.append(operation_chosen)

    if operation_chosen == "ADD_PERMISSION":
        role = random.choice([random.choice(ALL_ROLES), generate_random_string(10)])
        permission = random.choice(
            [random.choice(ALL_PERMISSIONS), generate_random_string(10)]
        )
        commands.append(role)
        commands.append(permission)
        if (role not in ALL_ROLES) or (permission not in ALL_PERMISSIONS):
            commands.append("1")
        else:
            commands.append("0")
            current_role[role].add(permission)

    elif operation_chosen == "REMOVE_PERMISSION":
        role = random.choice([random.choice(ALL_ROLES), generate_random_string(10)])
        permission = random.choice(
            [random.choice(ALL_PERMISSIONS), generate_random_string(10)]
        )
        commands.append(role)
        commands.append(permission)
        if (role not in ALL_ROLES) or (permission not in ALL_PERMISSIONS):
            commands.append("1")
        else:
            commands.append("0")
            if permission in current_role[role]:
                current_role[role].remove(permission)

    elif operation_chosen == "CREATE_USER":
        if len(current_user) != 0:
            user_name = random.choice(
                [random.choice(list(current_user.keys())), generate_random_string(10)]
            )
            user_email = random.choice(
                [random.choice(list(current_user.keys())), generate_random_string(10)]
            )
        else:
            user_name = generate_random_string(10)
            user_email = generate_random_string(10)
        commands.append(user_name)
        commands.append(user_email)
        if user_email in current_user:
            commands.append("1")
        else:
            commands.append("0")
            current_user[user_email] = set()

    elif operation_chosen == "ADD_ROLE":
        if len(current_user) != 0:
            user_email = random.choice(
                [random.choice(list(current_user.keys())), generate_random_string(10)]
            )
        else:
            user_email = generate_random_string(10)
        role = random.choice([random.choice(ALL_ROLES), generate_random_string(10)])
        commands.append(user_email)
        commands.append(role)
        if (role not in ALL_ROLES) or (user_email not in current_user):
            commands.append("1")
        else:
            commands.append("0")
            current_user[user_email].add(role)

    elif operation_chosen == "REMOVE_ROLE":
        if len(current_user) != 0:
            user_email = random.choice(
                [random.choice(list(current_user.keys())), generate_random_string(10)]
            )
        else:
            user_email = generate_random_string(10)
        role = random.choice([random.choice(ALL_ROLES), generate_random_string(10)])
        commands.append(user_email)
        commands.append(role)
        if (role not in ALL_ROLES) or (user_email not in current_user):
            commands.append("1")
        else:
            commands.append("0")
            if role in current_user[user_email]:
                current_user[user_email].remove(role)

    elif operation_chosen == "CHECK_USER_PERMISSION":
        if len(current_user) != 0:
            user_email = random.choice(
                [random.choice(list(current_user.keys())), generate_random_string(10)]
            )
        else:
            user_email = generate_random_string(10)
        permission = random.choice(
            [random.choice(ALL_PERMISSIONS), generate_random_string(10)]
        )
        commands.append(user_email)
        commands.append(permission)
        if (permission not in ALL_PERMISSIONS) or (user_email not in current_user):
            commands.append("1")
        else:
            for role in current_user[user_email]:
                if permission in current_role[role]:
                    commands.append("0")
                    break
            else:
                commands.append("1")

    # Write to FILE
    BATCH_DATA.append(" ".join(commands) + "\n")
    if i % BATCH_SAVE == 0:
        write_to_file(BATCH_DATA=BATCH_DATA)
        BATCH_DATA.clear()

if len(BATCH_DATA) != 0:
    write_to_file(BATCH_DATA=BATCH_DATA)
    BATCH_DATA.clear()

TOTAL_END_TIME = time.time()

print("TOTAL TIME IT TOOK:", TOTAL_END_TIME - TOTAL_START_TIME)
