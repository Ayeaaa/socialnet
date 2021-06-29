from flask import render_template, request, redirect
from . import force
from ..models import Nodes,Edges
import json,MySQLdb,pymysql


def nodesToJson():
    try:
        conn = pymysql.connect(host="localhost", user="root",
                             password="123456", database="socialnet", charset='utf8')
        cur = conn.cursor()
        sql = "select id,name,image,intro from nodes where name  IS NOT NULL  "
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
            result['image'] = str(row[2])
            result['intro'] = str(row[3])
            jsonData.append(result)
    except:
        print('meilianshang')
        'MySQL connect fail...'
    else:
        jsondatar = json.dumps(jsonData, ensure_ascii=False)
        # 去除首尾的中括号
        jsonDatas = jsondatar[1:len(jsondatar) - 1]
        jsondatas = "[" + jsonDatas + "]"
        return jsondatas

def edgesToJson():
    try:
        conn = pymysql.connect(host="localhost", user="root",
                             password="123456", database="socialnet", charset='utf8')
        cur = conn.cursor()
        sql = "select id,source,target,relation from edges where source  IS NOT NULL  "
        cur.execute(sql)
        data = cur.fetchall()
        print(data)
        cur.close()
        conn.close()
        jsonData = []
        for row in data:
            result = {}
            result['id'] = row[0]
            result['source'] = row[1]
            result['target'] = row[2]
            result['relation'] = str(row[3])
            jsonData.append(result)
    except:
        print('meilianshang')
        'MySQL connect fail...'
    else:
        jsondatar = json.dumps(jsonData, ensure_ascii=False)
        # 去除首尾的中括号
        jsonDatas = jsondatar[1:len(jsondatar) - 1]
        jsondatas = "[" + jsonDatas + "]"
        return jsondatas

@force.route('/')
def index():
    return render_template('index.html')

@force.route('/force')
def force():
    nodesdata = nodesToJson()
    edgesdata = edgesToJson()
    # nodesdata = list(Nodes.query.filter(Nodes.id!=None).all())
    nodesnum = Nodes.query.filter(Nodes.id!=None).count()
    # edgesdata = list(Edges.query.filter(Edges.id!=None).all())
    edgesnum = Edges.query.filter(Edges.id!=None).count()
    return render_template('force.html',nodesdata = nodesdata, nodesnum = nodesnum,edgesdata=edgesdata,edgesnum=edgesnum)


# @yien.route('/xyzs')
# def xyzs():
#     wanted = request.args.get("wanted", type=str)
#     if wanted is None:
#         wanted = ''
#         rs = list(Xyzs.query.filter(Xyzs.content!=None))
#     else:
#         rs = list(Xyzs.query.filter(Xyzs.content.like('%'+wanted+'%')).all())
#     words = ""
#     sentilist = []
#     kwlist = []
#     for r in rs:
#         s = SnowNLP(r.content)
#         # print(s.sentiments)
#         ss = format(s.sentiments, '.2%')
#         kws = cutword(r.content)
#         sentilist.append(ss)
#         kwlist.append(kws)
#         words = words + r.content
#
#     vcloud = cutword(words)
#     wdcount=len(vcloud)
#     return render_template('xyzs.html', rs=rs, wdcloud=vcloud, wdcount=wdcount,sentilist=sentilist, kwlist=kwlist)
#
# @news.route('/awaketime')
# def awaketime():
#     wanted = request.args.get("wanted", type=str)
#     if wanted is None:
#         wanted = '觉醒'
#     rs = list(Awake.query.filter(Awake.content.like('%'+wanted+'%')).all())
#     words = ""
#     sentilist = []
#     kwlist = []
#     for r in rs:
#         s = SnowNLP(r.content)
#         # print(s.sentiments)
#         ss = format(s.sentiments, '.2%')
#         kws = cutword(r.content)
#         sentilist.append(ss)
#         kwlist.append(kws)
#         words = words + r.content
#
#     vcloud = cutword(words)
#     return render_template('jxnd.html', rs=rs, wdcloud=vcloud, sentilist=sentilist, kwlist=kwlist)

