# Python usage

## Change calculation

`ChangeCalculator` calculates the differences between two lists. Its `changes` property exposes the differences as `Change` objects, which in turn expose the `before`, `after` and `change_type` of each element in those lists.

```python
from differently import ChangeCalculator

calc = ChangeCalculator(
    ["one", "too", "three", "four"],
    ["one", "two", "four"],
)

for line, change in enumerate(calc.changes):
    print(f"line {line}: before={change.before or ''}")
    print(f"line {line}: after={change.after or ''}")
    print(f"line {line}: change_type={change.change_type}")
    print()
```

<!--dinject as=markdown host=shell range=start-->

```text
line 0: before=one
line 0: after=one
line 0: change_type=ChangeType.none

line 1: before=too
line 1: after=two
line 1: change_type=ChangeType.replace

line 2: before=three
line 2: after=
line 2: change_type=ChangeType.delete

line 3: before=four
line 3: after=four
line 3: change_type=ChangeType.none
```

<!--dinject range=end-->

## Rendering plain text differences

`TextDifferently` visualises the differences between strings:

```python
from differently import TextDifferently

diff = TextDifferently("one\ntoo\nthree", "one\ntwo\nthree")

print(diff)
```

<!--dinject as=markdown host=shell range=start-->

```text
one    =  one
too    ~  two
three  =  three
```

<!--dinject range=end-->

## Rendering JSON differences

`JsonDifferently` visualises the differences between dictionaries as JSON.

```python
from differently import JsonDifferently
from typing import List, TypedDict

class PersonDict(TypedDict):
    name: str
    movies: List[str]

a: PersonDict = {
  "name": "Bobby Pringles",
  "movies": ["Fire Everywhere", "The World Is Exploding"],
}

b: PersonDict = {
  "name": "Susan Cheddar",
  "movies": ["The World Is Exploding", "Watch Out For The Moon"],
}

diff = JsonDifferently(a, b)

print(diff)
```

<!--dinject as=markdown host=shell range=start-->

```text
{                             =  {
  "movies": [                 =    "movies": [
    "Fire Everywhere",        x
    "The World Is Exploding"  ~      "The World Is Exploding",
                              >      "Watch Out For The Moon"
  ],                          =    ],
  "name": "Bobby Pringles"    ~    "name": "Susan Cheddar"
}                             =  }
```

<!--dinject range=end-->

## Rendering YAML differences

`YamlDifferently` visualises the differences between dictionaries as YAML.

```python
from differently import YamlDifferently
from typing import List, TypedDict

class PersonDict(TypedDict):
    name: str
    movies: List[str]

a: PersonDict = {
  "name": "Danny Jam",
  "movies": ["Oh, What a Lovely Implosion!", "Touch It and Die", "Mice! Mice! Mice!"],
}

b: PersonDict = {
  "name": "Sandy Jelly",
  "movies": ["Oh, What a Lovely Explosion!", "Mice! Mice! Mice!"],
}

diff = YamlDifferently(a, b)

print(diff)
```

<!--dinject as=markdown host=shell range=start-->

```text
movies:                         =  movies:
- Oh, What a Lovely Implosion!  ~  - Oh, What a Lovely Explosion!
- Touch It and Die              x
- Mice! Mice! Mice!             =  - Mice! Mice! Mice!
name: Danny Jam                 ~  name: Sandy Jelly
```

<!--dinject range=end-->
