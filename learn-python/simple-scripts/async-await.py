#!/usr/bin/env python3
import asyncio


async def hello():
    print('Hello ')
    await asyncio.sleep(3)
    print('World!')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
