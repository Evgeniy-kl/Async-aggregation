#!/bin/sh

echo "Waiting for flask..."


gunicorn --bind 0.0.0.0:5000 --workers 1 wsgi:app --timeout 600

echo "Flask started"




exec "$@"