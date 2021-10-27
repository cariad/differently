from enum import Enum, auto, unique


@unique
class DifferenceType(Enum):
    NONE = auto()
    INSERTION = auto()
    DELETION = auto()
    REPLACEMENT = auto()
