# README

## Motivation
Synchronize a CSV database and PNG/JPEG files to add #hashtag in image description.
Then, you can synchronize all files with Google drive and search image with *tags*.
Google set the metadata of the file from the 'description' metadata in graphic file.

## Synopsis
Google drive use only the description meta-data to index an image.
After this synchronisation it's possible to search an image with
"`type:image a_hashtag`".
```
type:image apple
```

This tool use [Exiftool](https://github.com/exiftool/exiftool)
```shell
$ sudo apt-get install exiftool        # Debian
$ sudo brew install exiftool           # Mac
$ sudo yum install perl-Image-ExifTool # CentOS
...
...
```

You can update the tags inside the description in your CSV file,
or use some others tools like [XnView](https://www.xnview.com/fr/)
and extract tags to CSV and descriptions.

By default, this tool merge the tags from CSV and files.

```shell
$ # Merge tags from descriptions.csv and selected files, and save all tags in tags.txt
$ tag_images_for_google_drive -v --db descriptions.csv '**/*.png' '**/*.jpg' \
--tagfile tags.txt
```

But it's possible to apply tags from database or files only
```shell
$ tag_images_for_google_drive -v --from-db   --db descriptions.csv '**/*.png' '**/*.jpg'
$ tag_images_for_google_drive -v --from-file --db descriptions.csv '**/*.png' '**/*.jpg'
```

To add a specific tag for all images in a directory, add it in command line.
```shell
$ tag_images_for_google_drive -v --db descriptions.csv -t myimages '**/*.png' '**/*.jpg'
```
The, you can filter theses specifics images with `type:image myimages ...`.

For more informations
```shell
$ tag_images_for_google_drive --help
```

or [read the documention](https://tag-images-for-google-drives.readthedocs.io/en/latest/)

To synchronize the google files, you can use different tools.
In the proposed Docker image, we use the `google-drive-ocamlfuse`.

## The latest version
Clone the git repository (see upper button)

## Installation
Different solutions is possible.

### For windows
Use `chcp 16001` (utf-8), before use this tools.

### Installation from one executable
- Copy the file 'tag_images_for_google_drive.${OS}' to local directory
- Rename this file to 'tag_images_for_google_drive'
- And run-it
```shell
$ tag_images_for_google_drive --help
```

### Installation from PIP
- In virtualenv or conda env, use
```shell
$ pip install tag_images_for_google_drive
```

- Then, run-it

```shell
$ tag_images_for_google_drive --help
```

### Installtion in Docker
- From the source code, use `make Dockerfile`
- WARNING, this image have the credential for manipulate all yours Google files
- Eventually, create a dedicated volume for the GDrive cache

```shell
> docker volume create --name tag_image_for_google_drive
```

- Create the container with custom parameters

```shell
$ docker build \
-f Dockerfile \
--build-arg OS_VERSION="latest" \
--build-arg GDRIVE_ROOT_FOLDER="/Images" \
--build-arg GDRIVE_TEAM_DRIVE_ID="" \
--build-arg PARAMS="'**/*.png' '**/*.jpg'" \
--build-arg CRON_FREQUENCE="* */12 * * *" \
-t "$(USER)/tag_image_for_google_drive:latest" .
```

- Start the container

```shell
$ docker run --detach --cpus=0.5 \
--privileged \
-v tag_image_for_google_drive:/cache
-i "$(USER)/tag_image_for_google_drive:latest"
```

Inside the container, a `google-drive-ocamlfuse` is installed to synchronize the google files
from `GDRIVE_ROOT_FOLDER` in the cache, and a crontab is periodically executed (see `CRON_REQUENCE`)
to invoke `tag_image_for_google_drive` with `PARAMS`.

### Installation from source
Go inside the directory and

```bash
$ make configure
$ conda activate tag_images_for_google_drive
$ make install
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
    ├── setup.py              <- makes project pip installable (pip install -e .[tests])
    │                            so sources can be imported and dependencies installed
    ├── tag_images_for_google_drive                <- Source code for use in this project
    └── tests                 <- Unit and integrations tests ((Mark directory as a sources root).


