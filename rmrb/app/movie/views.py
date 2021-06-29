from flask import render_template, request, redirect
from . import movie
from ..models import Nodes,Edges

@movie.route('/')
def index():
    return render_template('index.html')

@movie.route('/xyzs')
def movie():
    nodes = list(Nodes.query.all())
    nodes_num = Nodes.query.count()
    edges = list(Edges.query.all())
    edges_num = Edges.query.count()
    return render_template('movie.html', nodes_num =nodes_num ,edges = edges, edges_num =edges_num,
                           nodes = nodes)



