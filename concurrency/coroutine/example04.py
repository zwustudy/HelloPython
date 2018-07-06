'''
Created on 2018年6月21日

@author: zwustudy
'''
import asyncio
import example03


@asyncio.coroutine
def broadcast(targets):
    for target in targets:
        next(target)
    while True:
        item = (yield)
        for target in targets:
            target.send(item)
        

if __name__ == '__main__':
    f = open("my father.txt")
    p = example03.printer()
    example03.follow(f,
                     broadcast([example03.grep('mandolin',p),
                      example03.grep('a',p),
                      example03.grep('music',p)])
                      )
    pass