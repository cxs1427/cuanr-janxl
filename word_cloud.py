# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 16:24
# @Author  : -- CXS --
# @File    : word_cloud.py

from collections import Counter
import wordcloud
from jieba_test import ExtractTxt
import math
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import cv2

file_name = '平凡的世界-路遥.txt'
name = file_name.replace('.txt','')
extract = ExtractTxt(file_name)
d = extract.jieba_parse()
d_demo = d.most_common(10)
# num = 2
# d = Counter({'没有': 377, '太阳': 180, '变成': 154, '知道': 121, '开始': 119, '世界': 111, '眼睛': 96, '不能': 91, '生命': 88, '孩子': 87, '看见': 85, '不会': 79, '天空': 78, '月亮': 75, '影子': 70, '还有': 69, '愿望': 69, '喜欢': 66, '需要': 63, '微笑': 62, '地方': 59, '声音': 59, '生活': 58, '呼吸': 58, '好像': 56, '大地': 55, '相信': 54, '土地': 52, '无法': 50, '时候': 49, '黑夜': 48, '花朵': 47, '玻璃': 47, '寻找': 47, '森林': 47, '美丽': 46, '时间': 46, '等待': 45, '看着': 43, '走向': 43, '火焰': 42, '空气': 42, '上帝': 39, '海洋': 37, '燃烧': 37, '留下': 37, '树枝': 35, '云朵': 33, '穿过': 31, '死亡': 31})
# d_demo = Counter({'没有': 377, '太阳': 180, '变成': 154, '知道': 121, '开始': 119, '世界': 111, '眼睛': 96, '不能': 91, '生命': 88, '孩子': 87,})

def mat_bar():
    # 生成的是一个列表，放弃= =
    # d_demo = d.most_common(10)
    values = [value for key,value in d_demo]
    keys = [key for key,value in d_demo]
    index = numpy.arange(len(keys))
    width = 0.45  # 柱子宽度

    #解决plt中文乱码问题
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False

    plt.bar(index,values,width,label='word',color = '#87CEFA')
    plt.xlabel(file_name.replace('.txt',''))
    plt.ylabel('词频(次)')
    plt.title('高频词')

    # 添加横纵轴的刻度
    end = (math.ceil(values[0]/100))*100
    step = 100 if end > 500 else 50  # 动态变量
    plt.xticks(index,(keys))
    plt.yticks(numpy.arange(0,end,step))

    # 设置坐标轴的粗细(设置只是线的粗线，汗~)
    ax = plt.gca()  # 获得坐标轴的句柄
    # ax.spines['bottom'].set_linewidth(3)  # 设置底部坐标轴的粗细
    # ax.spines['left'].set_linewidth(2)  # 设置左边坐标轴的粗细
    # ax.spines['right'].set_linewidth(2);  # 设置右边坐标轴的粗细
    # ax.spines['top'].set_linewidth(2);  # 设置上部坐标轴的粗细

    # 添加图例
    plt.legend(loc='upper right')
    plt.savefig('%s 柱状图.png' % name)  # 在show之前保存，否则为空白
    plt.show()



def word_cloud():
    # mask = numpy.array(Image.open('timg.jpg'))
    # mask = numpy.array(Image.open('timg.png'))
    wc = wordcloud.WordCloud(
        font_path='cxs_font.ttf',
        width=1000,
        height=500,
        background_color='black',
        font_step=1,
        # mask = mask,
        min_font_size=4,
        max_font_size=200,
    )
    wc.generate_from_frequencies(d)
    img_name = '%s词云.png' % name
    # image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
    # wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
    wc.to_file(img_name)
    # plt.imshow(wc) # 显示词云
    # plt.axis('off') # 关闭坐标轴
    # plt.show() # 显示图像
    #
    # 显示图片,任意键关闭
    img = cv2.imread(img_name)
    cv2.imshow('cxs.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # word_cloud()
    mat_bar()




