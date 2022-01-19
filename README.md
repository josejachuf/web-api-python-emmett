# web-api-python-emmett

## Create a virtualenv

## Install emmett and orjson
pip install emmett orjson

## Start included server

emmett serve --workers 8

more info in https://emmett.sh/docs/2.4.x/deployment#included-server

## Start server with gunicorn
pip install gunicorn

gunicorn main:app -w 8 -k emmett.asgi.workers.EmmettWorker
