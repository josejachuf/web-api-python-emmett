# web-api-python-emmett

## Create a virtualenv

## Install emmett and orjson
pip install emmett orjson

## Start included server

emmett serve --workers 4

more info in https://emmett.sh/docs/2.4.x/deployment#included-server

## Start server with gunicorn
pip install gunicorn

gunicorn app:app -w 4 -k emmett.asgi.workers.EmmettWorker
