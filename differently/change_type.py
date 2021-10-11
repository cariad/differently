from enum import Enum


class ChangeType(Enum):
    none = "none"
    insert = "insert"
    delete = "delete"
    replace = "replace"
