
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
