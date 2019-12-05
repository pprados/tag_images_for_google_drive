# Commands

The Makefile contains the central entry points for common tasks related to this project.

* ``make help`` will print all majors target
* ``make configure``  will prepare the environment (conda venv, kernel, ...)
* ``make lint`` will lint the code
* ``make test`` will run all unit-tests
* ``make typing`` will check the typing
* ``make add-typing`` will add annotation for typing
* ``make validate`` will validate the version before commit
* ``make clean`` will clean current environment

* ``make docs`` will create and show a HTML documentation in 'build/'
* ``make dist`` will create a full wheel distribution

## Twine commands
* ``make check-twine`` will check the packaging before publication
* ``make test-twine`` will publish the package in `test.pypi.org <https://test.pypi.org>`_)
* ``make twine`` will publish the package in `pypi.org <https://pypi.org>`_)


