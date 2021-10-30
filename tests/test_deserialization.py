from typing import Any, Tuple, Type

from pytest import mark

from differently.deserialization import deserialize_value
from differently.json_differently import JsonDifferently
from differently.list_differently import ListDifferently
from differently.yaml_differently import YamlDifferently


@mark.parametrize(
    "v, expect",
    [
        (None, (None, None)),
        ("foo: bar", (YamlDifferently, {"foo": "bar"})),
        ('{"foo": "bar"}', (JsonDifferently, {"foo": "bar"})),
    ],
)
def test_deserialize_value(
    v: str,
    expect: Tuple[Type[ListDifferently], Any],
) -> None:
    assert deserialize_value(v) == expect
