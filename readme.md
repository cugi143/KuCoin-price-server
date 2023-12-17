# KuCoin price server
## Description
This is a simple server that will return the current price of a given cryptocurrency on KuCoin. It is written in Python and uses the iohttps package.

## OpenAPI Specification
The OpenAPI specification for this server can be found in the `openapi.yaml` or `openapi.json` file.

## Postman Configuration
The postman configuration for this server can be found in the `postman-config.json` file.

## Setup
### Install requirements
```
pip install -r requirements.txt
```

### Run server
Run the server with the following command:
```
python run.py
```
Or use a gunicorn server with the following command:
```
gunicorn -w 2 run:app
```

