#!/usr/bin/env bash

#: exec_target = cli
## Run manage.py which enables command line management of Django and Wagtail.
## Usage: fin manage [help]
## Parameters:
##   help: List further commands

cd /var/www/${DOCROOT}
python3 manage.py $@
