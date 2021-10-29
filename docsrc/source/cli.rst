CLI usage
=========

Plain text comparison
---------------------

By default, **differently** will perform a plain text comparison between any two files:

.. code-block:: console

  $ differently examples/1.md examples/2.md

.. code-block:: text

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

Style
-----

**differently** will guess whether to emit style codes. When she does:

- **green** indicates no change
- **yellow** indicates change
- **red** indicates deletion

To force style codes to be emitted, pass ``--color``.

Regardless of whether or not colour is emitted, the symbols in the visualisation indicate:

- **=** no change
- **>** inserted line
- **~** modified line
- **x** deleted line

Data comparison
---------------

**differently** can also compare the data described by JSON and YAML files.

Comparing the same type
~~~~~~~~~~~~~~~~~~~~~~~

To perform a data comparison, specify the file type via the ``--in-format`` argument:

.. code-block:: console

  $ differently examples/1.json examples/2.json --in-format json

.. code-block:: text

  {                                          =  {
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
  }                                          =  }

Comparing the same type but visualising as another
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regardless of the type of the data you're comparing, you can visualise as another by adding the `--out-format` argument.

For example, to compare two JSON files but emit the visualisation as YAML:

.. code-block:: console

  $ differently examples/1.json examples/2.json --in-format json --out-format yaml

.. code-block:: text

  array_of_dictionaries:             =  array_of_dictionaries:
  - name: Bobby Pringles             ~  - name: Bobby Salami
    occupation: Fire Starter         ~    occupation: Fire Fighter
  - name: Susan Cheddar              =  - name: Susan Cheddar
    occupation: Transporter Chief    =    occupation: Transporter Chief
  - name: Jade Rat                   =  - name: Jade Rat
    occupation: Lightning Conductor  ~    occupation: Lightning Chaser
  array_of_strings:                  =  array_of_strings:
  - This is the first line.          =  - This is the first line.
  - This is the second line.         =  - This is the second line.
                                     >  - This is the second-point-five line.
  - This is the third line.          =  - This is the third line.
  dictionary:                        =  dictionary:
                                     >    flavour: Cheese and Onion
    greeting: Hello                  =    greeting: Hello
    sound: Fire Truck                x
    username: operator               ~    username: root

Comparing across types
~~~~~~~~~~~~~~~~~~~~~~

Finally, **differently** allows you to compare data between JSON and YAML by specifying the file types comma-separated to ``--in-format``. You *must* specify an ``--out-format`` in this case.

.. code-block:: console

  $ differently examples/1.json examples/2.yml --in-format json,yaml --out-format yaml

.. code-block:: text

  array_of_dictionaries:             =  array_of_dictionaries:
  - name: Bobby Pringles             ~  - name: Bobby Salami
    occupation: Fire Starter         ~    occupation: Fire Fighter
  - name: Susan Cheddar              =  - name: Susan Cheddar
    occupation: Transporter Chief    =    occupation: Transporter Chief
  - name: Jade Rat                   =  - name: Jade Rat
    occupation: Lightning Conductor  ~    occupation: Lightning Chaser
  array_of_strings:                  =  array_of_strings:
  - This is the first line.          =  - This is the first line.
  - This is the second line.         =  - This is the second line.
                                     >  - This is the second-point-five line.
  - This is the third line.          =  - This is the third line.
  dictionary:                        =  dictionary:
                                     >    flavour: Cheese and Onion
    greeting: Hello                  =    greeting: Hello
    sound: Fire Truck                x
    username: operator               ~    username: root
