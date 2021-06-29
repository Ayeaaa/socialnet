from wordcloud import WordCloud, ImageColorGenerator
import jieba
import time
import numpy as np
from PIL import Image
import glob
import os


def deleteoldfile():
    path = "../../static/pic/"
    fileNames = glob.glob(path + r'\*')
    for file in fileNames:
        os.remove(file)
    fileNames = glob.glob(path + r'\*')
    return len(fileNames)


def cutword(txt):
    jieba.load_userdict("E:/Ayeaaa/socialnet/apps/news/AIDict.txt")
    seg_list = jieba.cut(txt, cut_all=False)
    tf = {}
    for seg in seg_list:
        if seg in tf:
            tf[seg] += 1
        else:
            tf[seg] = 1
    ci = list(tf.keys())
    with open('E:/Ayeaaa/socialnet/apps/news/stopwords.txt', 'r', encoding='utf-8') as ft:
        sw = ft.read()

    for seg in ci:
        if tf[seg] < 6 or len(seg) < 2 or seg in sw or "一" in seg:
            tf.pop(seg)
    ci = list(tf.keys())
    num = list(tf.values())
    data = []
    for i in range(len(tf)):
        data.append((num[i], ci[i]))
    data.sort()
    data.reverse()
    return data


def wordc(data):
    wcdata = {}
    for d in data:
        wcdata[d[1]] = d[0]

    font = r'ZaoZiGongFangLangChangGuiTi-1.otf'
    mask = np.array(Image.open("C:\\Users\\10988\\PycharmProjects\\datarequest\\111.jpg"))
    wc = WordCloud(font_path=font, width=200, height=200, background_color='white').generate_from_frequencies(wcdata)
    image_colors = ImageColorGenerator(mask)
    wc.recolor(color_func=image_colors)
    datetime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    picname = "static/pic/" + datetime + ".jpg"
    deleteoldfile()
    wc.to_file(picname)
    return picname
