#! python3
# coding: utf-8
import time
import math
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor

NUMBERS = range(240)
#URL = 'http://httpbin.org/get?a={}'
URL = 'http://192.168.1.22:8000/get?a={}'

async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return a, data['args']['a']

def sub_loop(numbers):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [fetch_async(num) for num in numbers]
    results = loop.run_until_complete(asyncio.gather(*tasks))
    #for num, result in results:
    #    print('fetch({}) = {}'.format(num, result))

async def run(executor, numbers):
    await asyncio.get_event_loop().run_in_executor(executor, sub_loop, numbers)

def chunks(l, size):
    n = math.ceil(len(l) / size)
    for i in range(0, len(l), n):
        yield l[i:i + n] 

start = time.time()
executor = ThreadPoolExecutor(3)
event_loop = asyncio.get_event_loop()
tasks = [run(executor, chunked) for chunked in chunks(NUMBERS, 3)]
results = event_loop.run_until_complete(asyncio.gather(*tasks))

print('Use asyncio+aiohttp+ThreadPoolExecutor cost: {}'.format(time.time() - start))
