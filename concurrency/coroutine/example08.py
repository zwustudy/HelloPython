'''
Created on 2018年6月23日

@author: zwustudy
'''

def bottom():
    # Returning the yield lets the value that goes up the call stack to come right back
    # down.
    print("----bottom----")
    return (yield 42)

def middle():
    print("----middle----")
    return (yield from bottom())

def top():
    print("----top----")
    return (yield from middle())

if __name__ == '__main__':
    # Get the generator.
    gen = top()
    value = next(gen)
    print(value)  # Prints '42'.
    try:
        value = gen.send(value * 2)
    except StopIteration as exc:
        print("----except----")
        print(value)  # Prints '42'.
        value = exc.value
    print(value)  # Prints '84'.
