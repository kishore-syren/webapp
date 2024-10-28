#!/bin/bash
python  -m  pip  install  --upgrade  pip
pip  install  -r  requirements.txt
gunicorn  -b  0.0.0.0:${WEBSITES_PORT} -w  4  --timeout  600  app:app
