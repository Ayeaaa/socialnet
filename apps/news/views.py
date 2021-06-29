from flask import render_template, request, redirect
from . import news
from ..models import Rmrb, Edges, Nodes
from .cut2word import cutword
import pymysql
import json
from snownlp import SnowNLP


# from rmrb_wordcloud import cutword


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
    # rs = select_content_by_keyword(wanted)
    words = ""
    sentilist = []
    kwlist = []
    for r in rs:
        s = r.point
        ss = format(s, '.2%')
        kws = r.key
        kwlist.append(kws)
        sentilist.append(ss)
        words = words + r.content
    wdcloud = cutword(words)
    wdcount = len(rs)
    return render_template('quicklook.html', rs=rs, wdcloud=wdcloud, sentilist=sentilist, kwlist=kwlist, wdcount=wdcount)


@news.route('/column/theme')
def theme():
    # result = select_content_by_category('奋斗百年路 启航新征程')
    result = list(Rmrb.query.filter(Rmrb.tag.like('奋斗百年路 启航新征程')).all())
    wdcount = len(result)
    return render_template('theme.html', rs=result, wdcount=wdcount)


@news.route('/column/keynews')
def important_news():
    result = list(Rmrb.query.filter(Rmrb.tag.like('要闻')).all())
    wdcount = len(result)
    return render_template('keynews.html', rs=result, wdcount=wdcount)


@news.route('/column/global')
def global_news():
    result = list(Rmrb.query.filter(Rmrb.tag.like('国际')).all())
    wdcount = len(result)
    return render_template('global.html', rs=result, wdcount=wdcount)


@news.route('/column/laws')
def laws():
    result = list(Rmrb.query.filter(Rmrb.tag.like('法治')).all())
    wdcount = len(result)
    return render_template('laws.html', rs=result, wdcount=wdcount)


@news.route('/column/social')
def social_news():
    result = list(Rmrb.query.filter(Rmrb.tag.like('社会')).all())
    wdcount = len(result)
    return render_template('social.html', rs=result, wdcount=wdcount)


@news.route('/net')
def show():
    nodes = list(Nodes.query.all())
    nodes_num = Nodes.query.count()
    edges = list(Edges.query.all())
    edges_num = Edges.query.count()

    # nodesdata = nodesToJson()
    # edgesdata = edgesToJson()
    # nodesnum = Nodes.query.filter(Nodes.id != None).count()
    # edgesnum = Edges.query.filter(Edges.id != None).count()

    wanted = request.args.get("wanted", type=str)
    if wanted is None:
        wanted = '要闻栏目'
    noders = Nodes.query.filter(Nodes.name.like('%' + wanted + '%'))
    for n in noders:
        id = n.id
    print(wanted, id)
    in_edgers = list(Edges.query.filter(Edges.target.like('%' + str(id) + '%')).all())
    out_edgers = list(Edges.query.filter(Edges.source.like('%' + str(id) + '%')).all())
    print(in_edgers, out_edgers)
    in_nodes_id = []
    out_nodes_id = []
    for i in in_edgers:
        in_nodes_id.append(i.source)
    for o in out_edgers:
        out_nodes_id.append(o.target)
    in_nodes = []
    out_nodes = []
    for inid in in_nodes_id:
        in_nodes.append(Nodes.query.filter(Nodes.id.like('%' + str(inid) + '%')).all())
    for outid in out_nodes_id:
        out_nodes.append(Nodes.query.filter(Nodes.id.like('%' + outid + '%')).all())
    in_nodes += out_nodes
    in_edgers += out_edgers
    in_nodes_rs = []
    for i in in_nodes:
        in_nodes_rs.append(i[0])
    noders_num = len(in_nodes_rs)
    edgers_num = len(in_edgers)
    return render_template('net.html', nodes_num=nodes_num, edges=edges, edges_num=edges_num, nodes=nodes,
                           noders=in_nodes_rs, edgers=in_edgers, noders_num=noders_num, edgers_num=edgers_num)
