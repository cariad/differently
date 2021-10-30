from typing import Any, Optional, Tuple, Type

from differently.exceptions import DeserializationError
from differently.json_differently import JsonDifferently
from differently.list_differently import ListDifferently
from differently.yaml_differently import YamlDifferently


def deserialize_value(
    v: Optional[str],
) -> Tuple[Optional[Type[ListDifferently]], Optional[Any]]:
    """
    Attempts to deserialise string `v`.

    Arguments:
        v: String to deserialise

    Returns:
        Deserialiser and deserialised value
    """

    if not v:
        return None, None

    try:
        return JsonDifferently, JsonDifferently.load(v)
    except DeserializationError:
        pass

    return YamlDifferently, YamlDifferently.load(v)
