## wagtail
The wagtail container services the requests.  

## cli
This is present for developers to manage Python libraries.

The PostgeSQL command line utility [psql](https://www.postgresql.org/docs/current/app-psql.html) is also installed
To connect
```bash
psql --username ${POSTGRES_USER} --dbname ${POSTGRES_DB} --host ${POSTGRES_HOST}
```
