# FastAPI Auth Example

This is an example of how to use [FastAPI](https://fastapi.tiangolo.com/) with
JWT authentication, using the
[fastapi_users](https://fastapi-users.github.io/fastapi-users/) library. It also
has `async` database access using [SQLAlchemy](https://www.sqlalchemy.org/)

Currently uses **SQLite** as the database, but can be easily changed to any
other database. It largely follows the example in the fastapi-users
documentation, however I have laid the project out in a way that I find more
readable and maintainable.

We use the [database
strategy](https://fastapi-users.github.io/fastapi-users/latest/configuration/authentication/strategies/database/)
instead of the default `jwt` strategy, as it allows us to invalidate tokens on
the server side. For the Transport, we use the
[Bearer](https://fastapi-users.github.io/fastapi-users/latest/configuration/authentication/transports/bearer/)
strategy where the token is sent in the `Authorization` header.

The project uses [uv](https://docs.astral.sh/uv/) to manage the dependencies. To
install the dependencies and switch to the virtual environment, run:

```bash
uv sync
source .venv/bin/activate # On Windows, use .venv\Scripts\activate
```

Now you can run the project with:

```bash
python main.py
```

> [!NOTE]
>
> The above uses the `--reload` option, so the server will restart whenever you
> change a file. This is useful for development, but not recommended for
> production.

The project will be available at `http://localhost:8000`.

You can access the API documentation at `http://localhost:8000/docs` (or
`http://localhost:8000/redoc` if you prefer that).
