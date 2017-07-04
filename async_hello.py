import asyncio
loop = asyncio.get_event_loop()


def test():
    print('Hiii')

@asyncio.coroutine
def hello():
        print('Hello')
        yield from asyncio.sleep(3)
        print('World!')


if __name__=='__main__':
    loop.run_until_complete(asyncio.wait([loop.create_task(hello()) for i in range(5)]))
