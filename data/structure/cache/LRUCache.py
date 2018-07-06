'''
Created on 2018年6月25日

缓存常用淘汰算法之一：LRU（least recently used 最近最少使用）算法根据数据的历史访问记录来进行淘汰数据，其核心思想是：如果数据最近被访问过，那么将来被访问的几率也更高。
当存在热点数据时，LRU的效率很好，但偶发性的、周期性的批量操作会导致LRU命中率急剧下降，缓存污染情况比较严重。

@author: zwustudy
'''
import collections

class LRUCache(collections.OrderedDict):

    def __init__(self, size=5):
        self.size = size
        self.cache = collections.OrderedDict()
        
        
    def get(self, key):
        
        if self.cache.__contains__(key):
            value = self.cache.pop(key)  #新访问了缓存，因此缓存需要移到最新的位置
            self.cache[key] = value
            return value
        else:
            return None
    
    
    def set(self, key, value):
        
        if self.cache.__contains__(key):
            self.cache.pop(key)  #新访问了缓存，因此缓存需要移到最新的位置
        elif len(self.cache) >= self.size:
            self.cache.popitem(last = False)
        self.cache[key] = value
            
class LRUCache1(object):
    
    def __init__(self, size = 5):
        self.size = size
        self.cache = dict()
        self.keyset = list()
        
    def get(self, key):
        if self.cache.__contains__(key):
            self.keyset.remove(key)  #新访问了缓存，因此缓存需要移到最新的位置
            self.keyset.insert(0, key)
            return self.cache.get(key)
        else:
            return None
    
    def set(self, key, value):
        if self.cache.__contains__(key):
            self.keyset.remove(key) #原来的key移除，好让后面把key的位置移到最新访问
        elif len(self.cache) >= self.size:
            removeKey = self.keyset.pop() #移除最近最少访问的缓存，给新缓存让个位置
            self.cache.pop(removeKey)
        self.keyset.insert(0, key)
        self.cache[key] = value
        
            
def main():
    cache = LRUCache1(5)
    for i in range(0, 6, 1):
        if i == 3:
            cache.set("key0", 0) #本来最早的缓存key是 key0,但是这里更新了之后，最早更新的就是key1，key1的缓存应该被淘汰
        cache.set("key" + str(i), i)
        
    for i in range(0, 7, 1):
        key = "key" + str(i)
        print(key + ":" + str(cache.get(key)))
    
if __name__ == "__main__":
    main()
            
        