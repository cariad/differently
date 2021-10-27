"""
**differently** is a CLI tool and Python package for visualising the differences between things.
"""


# ## CLI usage

# ```bash
# differently examples/1.md examples/2.md
# ```

# ```text
# # "differently" example file                           =  # "differently" example file
#                                                        =
# To run this example, install `differently` then run:   =  To run this example, install `differently` then run:
#                                                        =
# ```bash                                                =  ```bash
# differently 1.md 2.md                                  =  differently 1.md 2.md
# ```                                                    =  ```
#                                                        =
# This line says "foo" in 1.md.                          ~  This line says "bar" in 2.md.
#                                                        =
# Now, a deletion:                                       =  Now, a deletion:
#                                                        x
# Hello from 1.md.                                       x
#                                                        =
# The line above should appear in 1.md but deleted in    =  The line above should appear in 1.md but deleted in
# the diff because it's not in 2.md.                     =  the diff because it's not in 2.md.
#                                                        =
# And finally, this next line doesn't exist in 1.md but  =  And finally, this next line doesn't exist in 1.md but
# should be added in the diff because it's in 2.md:      =  should be added in the diff because it's in 2.md:
#                                                        >
#                                                        >  Hello from 2.md.

# ```

# ## Python usage

# TODO

# ## Installation

# **differently** requires Python 3.8 or later.

# ```bash
# pip install differently
# ```

# ## Feedback

# Please raise bugs, request features and ask questions at [github.com/cariad/differently/issues](https://github.com/cariad/differently/issues).

# Mention if you're a [sponsor](https://github.com/sponsors/cariad) to ensure I respond as a priority. Thank you!

# ## Project

# The source for `differently` is available at [github.com/cariad/differently](https://github.com/cariad/differently) under the MIT licence.

# And, **hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).


# from differently.version import get_version
from differently.change_type import DifferenceType

# from differently.change_calculator import ChangeCalculator
from differently.handlers import (
    JsonDifferently,
    ListDifferently,
    TextDifferently,
    YamlDifferently,
    render,
)
from differently.string_differently import StringDifferently

# from differently.change import Change
# from differently import handlers

__all__ = [
    #     "Change",
    #     "ChangeCalculator",
    "DifferenceType",
    #     "get_version",
    "JsonDifferently",
    "ListDifferently",
    "render",
    "StringDifferently",
    "TextDifferently",
    "YamlDifferently",
]
