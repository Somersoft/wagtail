# Python/Wagtail Docksal template

This template provides a starting point for developers, who already use or are
thinking of using Docksal, to have a hosting environment to develop websites
based upon python and Wagtail CMS. 

This template shows how to add python the list of supported server side languages
as well as PHP and the JavaScript family.

Docksal has an aim of providing zero configuration hosting environment for
developers which can be customised and extended with a low software management
overhead.

Under [performance](https://docs.wagtail.org/en/stable/advanced_topics/performance.html)
the Wagtail documentation makes reference to using [Redis](https://redis.io/)
and [Memcache](https://memcached.org/) services which are both supported by
Docksal. See [redis](https://docs.docksal.io/service/other/redis/) and
[memcached](https://docs.docksal.io/service/other/memcached/).
Wagtail also indicates that it can work using [MySQL](https://www.mysql.com/)
database and Docksal supports this by default.

# Django and Wagtail command line administration

A Docksal command is available to make available the Django and Wagtail cli
commands. See the following command for more information.  

``` shell
fin manage.py help
```

For example to create a Wagtail Superuser account

``` shell
fin manage.py createsuperuser
```
and follow the prompts.

# Python library management

This template installs [poetry](https://python-poetry.org/) and
[poethepoet](https://poethepoet.natn.io/index.html) to help with managing the
external python libraries and as a task runner.
It is recommended to use [pyproject.toml](./pyproject.toml) file to manage these
libraries and project task. 

The base install python libraries are controlled by this [pyproject.toml](./.docksal/base/pyproject.toml)
can be overwritten by the PROJECT_ROOT file.

# Contributors

- [Jiminald](https://github.com/jiminald) Feedback after testing and supplying
  commands

# Notes

- [Docksal](https://docksal.io/) is an all-purpose web-development environment
  based on Docker and Docker Compose.
- [Wagtail](https://wagtail.org/) is an open source project by
  [Torchbox](https://torchbox.com/) based upon Django.
- [Django](https://www.djangoproject.com/) is an open source Python based web
  framework by [Django Software Foundation](https://www.djangoproject.com/foundation/)
- Thanks to [Michael Yin](https://github.com/michael-yin)'s article on
  [Dockerizing Wagtail App](https://www.accordbox.com/blog/dockerizing-wagtail-app/)
