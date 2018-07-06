'''
Created on 2018年6月23日

@author: zwustudy
'''

def jumping_range(up_to):
    """Generator for the sequence of integers from 0 to up_to, exclusive.

    Sending a value into the generator will shift the sequence by that amount.
    """
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump
        print("----index----", index)
        print("----jump----", jump)

if __name__ == '__main__':
    iterator = jumping_range(6)
    print(next(iterator))
    print(next(iterator))  # 0
    print(iterator.send(2))  # 2
    print(next(iterator))  # 3
    print(iterator.send(-1))  # 2
    for x in iterator:
        print(x)