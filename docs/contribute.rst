.. index:: clone

Contribute
==========

Download sources

.. code-block:: bash

    $ git clone |giturl| tag_images_for_google_drive

then:

.. code-block:: bash

    $ cd tag_images_for_google_drive
    $ make configure
    $ conda activate tag_images_for_google_drive
    $ make docs


* A ``make validate`` was executed before a ``git push`` in branch ``master``.
  It possible to force the push with ``FORCE=y git push``.
