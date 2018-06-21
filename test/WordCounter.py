#coding=utf-8
'''
Created on 2015年8月15日
统计一篇英文文章各个单词出现的词频，并按单次的词频从大到小输出
@author: minmin
'''
import re
import collections

'''
从文件中读取内容，统计词频
'''
def count_word(path):
    result = {}
    with open(path) as file_obj:
        all_the_text = file_obj.read()
        #大写转小写
        all_the_text = all_the_text.lower()
        #正则表达式替换特殊字符
        all_the_text = re.sub("\"|,|\.", "", all_the_text)
        
        for word in all_the_text.split():
            if word not in result:
                result[word] = 0
            result[word] += 1 
            
        return result
    

'''
以词频倒序
'''
def sort_by_count(d):
    #字典排序
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d

if __name__ == '__main__':
    file_name = "..\my father.txt"

    dword = count_word(file_name)
    dword = sort_by_count(dword)
    
    for key,value in dword.items():
        print(key + ":%d" % value)

