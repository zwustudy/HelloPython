'''
Created on 2018年6月23日

@author: zwustudy
'''
def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    def gratuitous_refactor():
        index = 0
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()

if __name__ == '__main__':
    iterator = lazy_range(5)
    for x in iterator:
        print(x)