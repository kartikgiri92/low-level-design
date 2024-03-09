import abc
from rbac.permission import Permission
from constant.my_enums import StatusEnum


class Role(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "add_permission")
            and callable(subclass.add_permission)
            and hasattr(subclass, "remove_permission")
            and callable(subclass.remove_permission)
            and hasattr(subclass, "check_permission")
            and callable(subclass.check_permission)
            or NotImplemented
        )

    @abc.abstractmethod
    def add_permission(self, perm: Permission) -> StatusEnum:
        raise NotImplementedError

    @abc.abstractmethod
    def remove_permission(self, perm: Permission) -> StatusEnum:
        raise NotImplementedError

    @abc.abstractmethod
    def check_permission(self, perm: Permission) -> StatusEnum:
        raise NotImplementedError


class Admin(Role):
    def __init__(self) -> None:
        self.permissions = set()

    def add_permission(self, perm: Permission) -> StatusEnum:
        self.permissions.add(perm)
        return StatusEnum.SUCCESS

    def remove_permission(self, perm: Permission) -> StatusEnum:
        if perm in self.permissions:
            self.permissions.remove(perm)
        return StatusEnum.SUCCESS

    def check_permission(self, perm: Permission) -> StatusEnum:
        if perm in self.permissions:
            StatusEnum.SUCCESS
        return StatusEnum.FAILURE


class Customer(Role):
    def __init__(self) -> None:
        self.permissions = set()

    def add_permission(self, perm: Permission) -> StatusEnum:
        self.permissions.add(perm)
        return StatusEnum.SUCCESS

    def remove_permission(self, perm: Permission) -> StatusEnum:
        if perm in self.permissions:
            self.permissions.remove(perm)
        return StatusEnum.SUCCESS

    def check_permission(self, perm: Permission) -> StatusEnum:
        if perm in self.permissions:
            StatusEnum.SUCCESS
        return StatusEnum.FAILURE


class Owner(Role):
    def __init__(self) -> None:
        self.permissions = set()

    def add_permission(self, perm: Permission) -> StatusEnum:
        self.permissions.add(perm)
        return StatusEnum.SUCCESS

    def remove_permission(self, perm: Permission) -> StatusEnum:
        if perm in self.permissions:
            self.permissions.remove(perm)
        return StatusEnum.SUCCESS

    def check_permission(self, perm: Permission) -> StatusEnum:
        if perm in self.permissions:
            StatusEnum.SUCCESS
        return StatusEnum.FAILURE
