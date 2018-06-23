'''
Created on 2018年6月23日

@author: zwustudy
'''
import asyncio

@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        yield from asyncio.sleep(1)
        n -= 1

if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(countdown("A", 2)),
             asyncio.ensure_future(countdown("B", 3))]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

