import os

from flask import Flask, Response, request

from validate import torch_image
from file_reader import get_label

app = Flask(__name__)


@app.post('/')
def query_example():
    image = request.files['image'].stream.read()
    print(get_label(torch_image(image)))
    return Response('received')
