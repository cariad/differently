# differently

`differently` is a CLI tool and Python package for visualising the differences between objects.

![](example.png)

## Installation

```bash
pip install differently
```

## Command line usage

On the command line, run `differently` with the two files to compare:

```bash
bash file1 file2
```

## Python usage

To compare two strings, create a `TextDifferently` instance:

```python
from differently import TextDifferently

print(TextDifferently("foo", "bar"))
```

To compare two lists, create a `ListDifferently` instance:

```python
from differently import TextDifferently

print(ListDifferently(["foo"], ["bar"]))
```
