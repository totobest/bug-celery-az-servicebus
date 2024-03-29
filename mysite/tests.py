import asyncio
import aiohttp
import pytest


async def multi_calls(url):
    async with aiohttp.ClientSession() as session:
        resp_1, resp_2 = await asyncio.gather(session.get(url), session.get(url))
        assert resp_1.status == 200
        assert resp_2.status == 200


@pytest.mark.asyncio
async def test_async_ping(live_server):
    url = f"{live_server.url}/ping"
    await multi_calls(url)


@pytest.mark.asyncio
async def test_async_az(live_server):
    url = f"{live_server.url}/az"
    await multi_calls(url)
