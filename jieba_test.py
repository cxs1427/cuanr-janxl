# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 13:37
# @Author  : -- CXS --
# @File    : jieba_test.py

import jieba
import jieba.posseg as ps
import jieba.analyse as an
import jieba.finalseg as fl
from datetime import datetime
from collections import Counter


# def get_content(file_name):
#     # utf-8给中文编码会报错
#     # gbk编码也会报错 --
#     with open (file_name,encoding='gb18030') as f:
#         content = f.read()
#     return content

# 词频统计
# def word_counter(content):
#     words = jieba.cut(content)
#     counter = Counter()

# start_time = datetime.now()
# end_time = datetime.now()
# print(start_time - end_time)

# sentence = '巴拉巴拉哔哩哔哩变量哔哩哔哩弹幕'


# 添加自定义字典,防止被分词
# jieba.load_userdict('')

# 全模式,会出现叠词
# words_all = jieba.cut(sentence,cut_all=True)  # lcut直接生成列表
# 搜索引擎模式
# words_search = jieba.cut_for_search(sentence)
# 精准模式,默认

# words = jieba.cut(sentence,cut_all=False)
# print('|'.join(words_search))
# print('|'.join(words_all))
# print('|'.join(words))

# 过滤停止词
# jieba.analyse.set_stop_words('停止词.txt')
# 选取权重
# content = get_content('百年孤独.txt')
# content = get_content('顾城诗全集.txt')
# content = get_content('平凡的世界-路遥.txt')
# word_list = jieba.cut(content)
# start_time = datetime.now()
# result = an.textrank(content,topK=100,withFlag=False,withWeight=False)
# d = Counter()
# 生成器不能多次遍历
# for each_word in word_list:
#     if each_word in result:
#         d[each_word] += 1
# end_time = datetime.now()
# print('用时： ',end_time - start_time)
# print(d)

# 判断词性
# words_type = ps.cut(sentence)
# for word,type in words_type:
#     print(word,type)
# pass

class ExtractTxt(object):
    # 创建一个分词类
    def __init__(self,filename):
        self.file_name = filename

    def get_content(self):
        # 读取文本内容
        with open(self.file_name, encoding='gb18030') as f:
            content = f.read()
        return content

    def jieba_parse(self):
        # 分词处理，返回词频字典
        content = self.get_content()
        word_list = jieba.cut(content)
        result = an.textrank(content, topK=200, withFlag=False, withWeight=False)
        d = Counter()
        for each_word in word_list:
            if each_word in result:
                d[each_word] += 1
        return d
