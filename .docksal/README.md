## wagtail
The wagtail container services the requests. This is based upon the standard cli
container.  

## cli
This is present for developers to manage Python libraries.

It has been extended by adding [Pipx](https://realpython.com/python-pipx/) and
[Poetry](https://python-poetry.org/)  

The PostgeSQL command line utility [psql](https://www.postgresql.org/docs/current/app-psql.html) is also installed.
To connect to the PostgreSQL database
``` bash
psql --username ${POSTGRES_USER} --dbname ${POSTGRES_DB} --host ${POSTGRES_HOST}
```
