# Overview

## Install Requirements

`pip install -r requirements.txt`

## Activate Virtual Environment and Run

`source venv/bin/activate && python3 main.py`

## Deploy

Export flask app and `flask run`


# Troubleshooting

## SSL problem

Your computer may not allow incoming requests natively. In this case install the SSL certificate by running the following command in your terminal.

`create certificate ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.9/etc/openssl`
