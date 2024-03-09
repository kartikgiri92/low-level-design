import abc


class Permission(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return NotImplemented


class DefaultPermission1(Permission):
    def __init__(self) -> None:
        pass


class DefaultPermission2(Permission):
    def __init__(self) -> None:
        pass


class AdminPermission1(Permission):
    def __init__(self) -> None:
        pass


class AdminPermission2(Permission):
    def __init__(self) -> None:
        pass
