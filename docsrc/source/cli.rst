CLI Usage
=========

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
