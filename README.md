# differently

[![codecov](https://codecov.io/gh/cariad/differently/branch/main/graph/badge.svg?token=2hx57vSnN9)](https://codecov.io/gh/cariad/differently) [![CircleCI](https://circleci.com/gh/cariad/differently/tree/main.svg?style=shield)](https://circleci.com/gh/cariad/differently/tree/main)

`differently` is a CLI tool and Python package for visualising the differences between things.

## Installation

`differently` requires Python 3.8 or later.

```bash
pip install differently
```

## Example

```bash
differently examples/1.md examples/2.md
```

<!--dinject as=markdown host=shell range=start-->

```text
# "differently" example file                           =  # "differently" example file
                                                       =
To run this example, install `differently` then run:   =  To run this example, install `differently` then run:
                                                       =
```bash                                                =  ```bash
differently 1.md 2.md                                  =  differently 1.md 2.md
```                                                    =  ```
                                                       =
This line says "foo" in 1.md.                          ~  This line says "bar" in 2.md.
                                                       =
Now, a deletion:                                       =  Now, a deletion:
                                                       x
Hello from 1.md.                                       x
                                                       =
The line above should appear in 1.md but deleted in    =  The line above should appear in 1.md but deleted in
the diff because it's not in 2.md.                     =  the diff because it's not in 2.md.
                                                       =
And finally, this next line doesn't exist in 1.md but  =  And finally, this next line doesn't exist in 1.md but
should be added in the diff because it's in 2.md:      =  should be added in the diff because it's in 2.md:
                                                       >
                                                       >  Hello from 2.md.
```

<!--dinject range=end-->

`differently` also supports JSON and YAML comparisons and Python usage. Read the full documentation at [differently.readthedocs.io](https://differently.readthedocs.io).

## 👋 Hello!

**Hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).

If you ever raise a bug, request a feature or ask a question then mention that you're a sponsor and I'll respond as a priority. Thank you!
