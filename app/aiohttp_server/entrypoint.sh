#!/bin/sh

echo "Waiting for aiohttp..."

python main.py

echo "Aiohttp started"




exec "$@"