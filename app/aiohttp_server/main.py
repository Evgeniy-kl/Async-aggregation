from aiohttp import web

from api import send_image


async def init():
    app = web.Application()
    app.router.add_post("/image", send_image)
    return app


if __name__ == "__main__":
    application = init()
    web.run_app(application, port=8000)
