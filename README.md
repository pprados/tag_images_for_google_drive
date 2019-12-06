# tag_images_for_google_drive

## Motivation

Synchronize a CSV database and PNG/JPEG files to add #hashtag in image description.
Then, you can synchronize all files with Google drive.

By default, this tools merge the tags from CSV and files.

## Synopsis

Google drive use only the description meta-data to index an image.
After this synchronisation it's possible to search an image with
"type:image an_hash_tag".

This tools use [Exiftools](https://github.com/exiftool/exiftool)

You can update the tags inside the description in your CSV file,
or use some others tools like [XnView](https://www.xnview.com/fr/)
and extract tags to CSV and descriptions.

## The latest version

Clone the git repository (see upper button)

## Installation

Go inside the directory and
```bash
$ make configure
$ conda activate tag_images_for_google_drive
$ make docs
```

## Tests

To test the project
```bash
$ make test
```

To validate the typing
```bash
$ make typing
```

To validate all the project
```bash
$ make validate
```

## Project Organization

    ├── Makefile              <- Makefile with commands like `make data` or `make train`
    ├── README.md             <- The top-level README for developers using this project.
    ├── docs                  <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── reports               <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures           <- Generated graphics and figures to be used in reporting
    │
    ├── setup.py              <- makes project pip installable (pip install -e .[tests])
    │                            so sources can be imported and dependencies installed
    ├── tag_images_for_google_drive                <- Source code for use in this project
    │   ├── __init__.py       <- Makes src a Python module
    │   └── tools.py          <- Python module for functions, object, etc
    │
    └── tests                 <- Unit and integrations tests ((Mark directory as a sources root).


