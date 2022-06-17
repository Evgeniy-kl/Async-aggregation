import json
import os

from aiohttp import web

from http_request import broadcast

URLS = os.getenv('HOSTS').split(',')


async def send_image(request):
    # WARNING: don't do that if you plan to receive large files!
    data = await request.post()

    image = data['image'].file.read()
    await broadcast(image, URLS)

    response = {'status': 'success', 'message': 'OK'}
    return web.Response(text=json.dumps(response), status=200)
