"""foo"""

from enum import Enum


class ChangeType(Enum):
    """
    Change type.
    """

    none = "none"
    """No change."""

    insert = "insert"
    delete = "delete"
    replace = "replace"
