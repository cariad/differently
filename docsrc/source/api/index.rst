Python usage
============

Classes
-------

**differently** supports difference visualisations through a library of classes:

- :class:`.StringDifferently` visualises the differences between strings
- :class:`.TextDifferently` visualises the differences between multi-line text bodies
- :class:`.ListDifferently` visualises the differences between lists of strings
- :class:`.JsonDifferently` visualises the differences between objects as JSON
- :class:`.YamlDifferently` visualises the differences between objects as YAML

Rendering
---------

A difference can be visualised by casting any class instance to a string (i.e. ``str(...)``).

If you want to avoid string manipulation, you can render directly to any string IO stream via each class's ``.render()`` function.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   deserialization
   string_differently
   list_differently
   text_differently
   json_differently
   yaml_differently
