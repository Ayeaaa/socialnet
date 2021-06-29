from flask import render_template, request, redirect
from . import maoyan
from ..models import Map_bo

@maoyan.route('/')
def index():
    return render_template('index.html')

@maoyan.route('/map')
def map():
    data = list(Map_bo.query.all())
    data_num = Map_bo.query.count()
    return render_template('map_d3.html',data = data, data_num = data_num)



