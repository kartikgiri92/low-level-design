from inventory.inventory import DataStore
from constant.my_enums import StatusEnum
from rbac.account import User
from rbac.role import Role


def add_permission(command: list, data_store: DataStore) -> StatusEnum:
    role_n, permission_n = command[1], command[2]

    if (
        role_n not in data_store.ROLE_INVENTORY
        or permission_n not in data_store.PERMISSION_INVENTORY
    ):
        # ROLE/Permission Does not Exist
        return StatusEnum.FAILURE
    permission_n = data_store.PERMISSION_INVENTORY[permission_n]
    return data_store.ROLE_INVENTORY[role_n].add_permission(permission_n)


def remove_permission(command: list, data_store: DataStore) -> StatusEnum:
    role_n, permission_n = command[1], command[2]

    if (
        role_n not in data_store.ROLE_INVENTORY
        or permission_n not in data_store.PERMISSION_INVENTORY
    ):
        # ROLE/Permission Does not Exist
        return StatusEnum.FAILURE
    permission_n = data_store.PERMISSION_INVENTORY[permission_n]
    return data_store.ROLE_INVENTORY[role_n].remove_permission(permission_n)


def create_user(command: list, data_store: DataStore) -> StatusEnum:
    name_n, email_n = command[1], command[2]

    if email_n in data_store.USER_INVENTORY:
        # User Already Exist
        return StatusEnum.FAILURE
    data_store.USER_INVENTORY[email_n] = User(name=name_n, email=email_n)
    return StatusEnum.SUCCESS


def add_role(command: list, data_store: DataStore) -> StatusEnum:
    email_n, role_n = command[1], command[2]
    if (email_n not in data_store.USER_INVENTORY) or (
        role_n not in data_store.ROLE_INVENTORY
    ):
        # Email or Role not found
        return StatusEnum.FAILURE
    role_n = data_store.ROLE_INVENTORY[role_n]
    return data_store.USER_INVENTORY[email_n].add_role(role_n)


def remove_role(command: list, data_store: DataStore) -> StatusEnum:
    email_n, role_n = command[1], command[2]
    if (email_n not in data_store.USER_INVENTORY) or (
        role_n not in data_store.ROLE_INVENTORY
    ):
        # Email or Role not found
        return StatusEnum.FAILURE
    role_n = data_store.ROLE_INVENTORY[role_n]
    return data_store.USER_INVENTORY[email_n].remove_role(role_n)


def check_user_permission(command: list, data_store: DataStore) -> StatusEnum:
    email_n, permission_n = command[1], command[2]
    if (email_n not in data_store.USER_INVENTORY) or (
        permission_n not in data_store.PERMISSION_INVENTORY
    ):
        # Email or Role not found
        return StatusEnum.FAILURE
    permission_n = data_store.PERMISSION_INVENTORY[permission_n]
    return data_store.USER_INVENTORY[email_n].check_permission(permission_n, data_store)
