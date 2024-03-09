from rbac.role import Admin, Customer, Owner

from rbac.permission import (
    DefaultPermission1,
    DefaultPermission2,
    AdminPermission1,
    AdminPermission2,
)


class DataStore:
    def __init__(self) -> None:
        # Stores User Details (Key: Email, Value: User Obj)
        self.USER_INVENTORY = {}

        # Stores Role Details(Key: Role.__name__, value: Role Obj)
        self.ROLE_INVENTORY = {
            Admin.__name__: Admin(),
            Customer.__name__: Customer(),
            Owner.__name__: Owner(),
        }

        # Stores Permission Details (Key: Permission.__name__, Value: Permission Class)
        self.PERMISSION_INVENTORY = {
            DefaultPermission1.__name__: DefaultPermission1,
            DefaultPermission2.__name__: DefaultPermission2,
            AdminPermission1.__name__: AdminPermission1,
            AdminPermission2.__name__: AdminPermission2,
        }


def load_inventory():
    data_store = DataStore()
    return data_store
