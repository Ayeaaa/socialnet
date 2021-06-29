from flask import render_template, request, redirect
from . import yien
from ..models import top10


@yien.route('/')
def index():
    return render_template('index.html')


@yien.route('/bo_top10')
def bo_top():
    data = list(top10.query.filter(top10.ntime == '06月10日 周四 18:15').all())
    datanum = top10.query.filter(top10.ntime == '06月10日 周四 18:15').count()

    return render_template('yien.html', data=data, datanum=datanum)

