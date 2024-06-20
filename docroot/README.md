# Installation
This is a part of the container build process.
```bash
poetry install
PYTHONPATH=`poetry env info --path`/lib/python3.11/site-packages
export PYTHONPATH
```

# Manage

## Add the default superuser account.
```bash
cd $DOCROOT
python3 manage.py createsuperuser
```

# Create the project
```bash
django-admin startproject wagtail_app .
```
