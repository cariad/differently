from enum import Enum


class ChangeType(Enum):
    none = 0
    insert = 1
    delete = 2
    modify = 3
