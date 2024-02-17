# bug-celery-az-servicebus

# Install

1. Set environnement variable `CELERY_BROKER_URL=azureservicebus://<user>:<pw>@<server>`
1. Then:

```
pipx install poetry
poetry install

```

Run tests (second test case is failing with azure-servicebus):

```
poetry run pytest
```

or run Django dev server and hit more than once http://localost/az

```
./manage runserver
```
