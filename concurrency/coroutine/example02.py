#code=utf-8
'''
Created on 2018年6月21日

@author: zwustudy

yield接收外部value,先通过next()函数 开启携程coroutine
之后每一次调用send(),将参数传入yield,同时相当于grep函数自动运行到line=send的内容，协同工作。最终调用。close()关闭这个协程
'''

def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep('coroutine')
next(search)
# Output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
# Output: I love coroutines instead!
search.send("But where is coroutine!")
search.close()

if __name__ == '__main__':
    pass