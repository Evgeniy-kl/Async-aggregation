import aiohttp


async def broadcast(payload, urls):
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.post(url, data={'image': payload}) as resp:
                print(resp.status)
                print(await resp.text())
