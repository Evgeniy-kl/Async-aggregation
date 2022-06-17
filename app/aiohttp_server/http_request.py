import asyncio

import aiohttp


async def post_image(session, url, image):
    async with session.post(url, data={'image': image}) as resp:
        return await resp.text()


async def broadcast(image, urls):
    async with aiohttp.ClientSession() as session:

        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(post_image(session, url, image)))

        words = await asyncio.gather(*tasks)
        for word in words:
            print(word)
