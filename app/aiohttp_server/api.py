import json
import os

from aiohttp import web

from http_request import broadcast

URLS = os.getenv('HOSTS').split(',')


async def send_image(request):
    data = await request.post()

    image = data['image'].file.read()
    await broadcast(image, URLS)

    response = {'status': 'success', 'message': 'OK'}
    return web.Response(text=json.dumps(response), status=200)
