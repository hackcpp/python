import asyncio
from datetime import datetime


async def hello():
    # print(datetime.now())
    await asyncio.sleep(5)
    # print(datetime.now())


loop = asyncio.get_event_loop()
print(datetime.now())
loop.run_until_complete(asyncio.wait([hello(), hello()]))
loop.close()
print(datetime.now())

