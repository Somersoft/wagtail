# install
$ poetry install
$ PYTHONPATH=`poetry env info | grep Path | head -1 | awk '{print $2}'`/lib/python3.11/site-packages
$ export PYTHONPATH

# create virtualenv
cd docroot
$ python3 -m venv venv
# create the project
$ django-admin startproject wagtail_app .

Manage
# Add the defailt admin account.
python3 manage.py createsuperuser
