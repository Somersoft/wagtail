# install
$ poetry install
$ PYTHONPATH=`poetry env info --path`/lib/python3.11/site-packages
$ export PYTHONPATH

Manage
# Add the default superuser account.
python3 manage.py createsuperuser

# Create the project
$ django-admin startproject wagtail_app .
