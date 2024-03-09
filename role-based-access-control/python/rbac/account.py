import abc
from rbac.role import Role
from rbac.permission import Permission
from constant.my_enums import StatusEnum
from inventory.inventory import DataStore


class Account(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "add_role")
            and callable(subclass.add_role)
            and hasattr(subclass, "remove_role")
            and callable(subclass.remove_role)
            and hasattr(subclass, "check_role")
            and callable(subclass.check_role)
            and hasattr(subclass, "check_permission")
            and callable(subclass.check_permission)
            or NotImplemented
        )

    @abc.abstractmethod
    def add_role(self, input_role: Role) -> StatusEnum:
        raise NotImplementedError

    @abc.abstractmethod
    def remove_role(self, input_role: Role) -> StatusEnum:
        raise NotImplementedError

    @abc.abstractmethod
    def check_role(self, input_role: Role) -> StatusEnum:
        raise NotImplementedError

    @abc.abstractmethod
    def check_permission(self, perm: Permission) -> StatusEnum:
        raise NotImplementedError


class User(Account):
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.roles = set()

    def add_role(self, input_role: Role) -> StatusEnum:
        self.roles.add(input_role)
        return StatusEnum.SUCCESS

    def remove_role(self, input_role: Role) -> StatusEnum:
        if input_role in self.roles:
            self.roles.remove(input_role)
        return StatusEnum.SUCCESS

    def check_role(self, input_role: Role) -> StatusEnum:
        if input_role in self.roles:
            return StatusEnum.SUCCESS
        return StatusEnum.FAILURE

    def check_permission(self, perm: Permission, data_store: DataStore) -> StatusEnum:
        for role in self.roles:
            if perm in role.permissions:
                return StatusEnum.SUCCESS
        return StatusEnum.FAILURE
