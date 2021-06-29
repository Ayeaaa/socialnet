from flask import render_template, request, redirect
from . import news
from ..models import Rmrb, Edges, Nodes
from .cut2word import cutword
import pymysql
import json
#from rmrb_wordcloud import cutword


@news.route('/')
def index():

    return redirect('/quicklook')


@news.route('/quicklook')
def quicklook():
    '''

    :return: rs:数据库中所有符合条件的内容，r[0]-date,r[1]-page,r[2]-tag,r[3]-title,r[4]-url,r[5]-content
             wdcloud:词云里的单词
    '''
    wanted = request.args.get("wanted", type=str)
    if wanted is None:
        wanted = '中国'
    rs = list(Rmrb.query.filter(Rmrb.content.like('%' + wanted + '%')).all())
    #rs = select_content_by_keyword(wanted)
    words = ""
    for r in rs:
        words = words + r.content
    wdcloud = cutword(words)
    return render_template('index.html', rs=rs, wdcloud=wdcloud)


@news.route('/column/theme')
def theme():
    #result = select_content_by_category('奋斗百年路 启航新征程')
    result = list(Rmrb.query.filter(Rmrb.tag.like('奋斗百年路 启航新征程')).all())
    return render_template('index3.html', rs=result)


@news.route('/column/keynews')
def important_news():
    result = list(Rmrb.query.filter(Rmrb.tag.like('要闻')).all())
    return render_template('index6.html', rs=result)


@news.route('/column/global')
def global_news():
    result = list(Rmrb.query.filter(Rmrb.tag.like('国际')).all())
    return render_template('index5.html',rs=result)


@news.route('/column/laws')
def laws():
    result = list(Rmrb.query.filter(Rmrb.tag.like('法治')).all())
    return render_template('index2.html',rs=result)


@news.route('/column/social')
def social_news():
    result = list(Rmrb.query.filter(Rmrb.tag.like('社会')).all())
    return render_template('index7.html',rs=result)


def nodesToJson():
    conn = pymysql.connect(host="localhost", user="root",
                           password="EGG2152", db="cucnews")
    cur = conn.cursor()
    sql = "select id,name,intro from nodes where id IS NOT NULL  "
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    cur.close()
    conn.close()
    jsonData = []
    for row in data:
        result = {}
        result['id'] = row[0]
        result['name'] = str(row[1])
        result['intro'] = str(row[2])
        jsonData.append(result)
    jsondatar = json.dumps(jsonData, ensure_ascii=False)
    # 去除首尾的中括号
    jsonDatas = jsondatar[1:len(jsondatar) - 1]
    jsondatas = "[" + jsonDatas + "]"
    return jsondatas

def edgesToJson():
    conn = pymysql.connect(host="localhost", user="root",
                           password="EGG2152", db="cucnews")
    cur = conn.cursor()
    sql = "select id,source,target,weight from edges where id IS NOT NULL  "
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    cur.close()
    conn.close()
    jsonData = []
    for row in data:
        result = {}
        result['id'] = row[0]
        result['source'] = str(row[1])
        result['target'] = str(row[2])
        result['weight'] = str(row[3])
        jsonData.append(result)
    jsondatar = json.dumps(jsonData, ensure_ascii=False)
    # 去除首尾的中括号
    jsonDatas = jsondatar[1:len(jsondatar) - 1]
    jsondatas = "[" + jsonDatas + "]"
    return jsondatas


@news.route('/net')
def show():
    nodesdata = nodesToJson()
    edgesdata = edgesToJson()
    nodesnum = Nodes.query.filter(Nodes.id != None).count()
    edgesnum = Edges.query.filter(Edges.id != None).count()
    wanted = request.args.get("wanted", type=str)
    if wanted is None:
        wanted = ''
    noders = list(Nodes.query.filter(Nodes.name.like('%' + wanted + '%')).all())
    edgers = list(Edges.query.filter(Edges.target.like('%' + wanted + '%')).all())
    return render_template('force.html',nodesdata=nodesdata, nodesnum=nodesnum, edgesdata=edgesdata, edgesnum=edgesnum,
                           noders=noders, edgers=edgers)

