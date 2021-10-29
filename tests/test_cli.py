from io import StringIO

from differently.cli import entry


def test__text_vs_text() -> None:
    writer = StringIO()
    assert entry(["examples/1.md", "examples/2.md"], writer) == 0
    assert (
        writer.getvalue()
        == """# "differently" example file                           =  # "differently" example file
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
                                                       >  Hello from 2.md."""
    )


def test__json_vs_yaml_as_json() -> None:
    writer = StringIO()
    assert (
        entry(
            [
                "examples/1.json",
                "examples/2.yml",
                "--in-format",
                "json,yaml",
                "--out-format",
                "json",
            ],
            writer,
        )
        == 0
    )
    assert (
        writer.getvalue()
        == """{                                          =  {
  "array_of_dictionaries": [               =    "array_of_dictionaries": [
    {                                      =      {
      "name": "Bobby Pringles",            ~        "name": "Bobby Salami",
      "occupation": "Fire Starter"         ~        "occupation": "Fire Fighter"
    },                                     =      },
    {                                      =      {
      "name": "Susan Cheddar",             =        "name": "Susan Cheddar",
      "occupation": "Transporter Chief"    =        "occupation": "Transporter Chief"
    },                                     =      },
    {                                      =      {
      "name": "Jade Rat",                  =        "name": "Jade Rat",
      "occupation": "Lightning Conductor"  ~        "occupation": "Lightning Chaser"
    }                                      =      }
  ],                                       =    ],
  "array_of_strings": [                    =    "array_of_strings": [
    "This is the first line.",             =      "This is the first line.",
    "This is the second line.",            =      "This is the second line.",
                                           >      "This is the second-point-five line.",
    "This is the third line."              =      "This is the third line."
  ],                                       =    ],
  "dictionary": {                          =    "dictionary": {
                                           >      "flavour": "Cheese and Onion",
    "greeting": "Hello",                   =      "greeting": "Hello",
    "sound": "Fire Truck",                 x
    "username": "operator"                 ~      "username": "root"
  }                                        =    }
}                                          =  }"""
    )


def test_multiple_in_no_out() -> None:
    writer = StringIO()
    assert entry(["--in-format", "json,yaml"], writer) == 1
    assert (
        writer.getvalue()
        == 'You must include "--out-format" when you specify multiple values for "--in-format".\n'
    )


def test_version() -> None:
    writer = StringIO()
    assert entry(["--version"], writer) == 0
    assert writer.getvalue() == "-1.-1.-1\n"
