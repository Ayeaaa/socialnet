from . import db

class top10(db.Model):
    __tablename__ = 'yien'
    id = db.Column(db.Integer, primary_key=True)
    ranking = db.Column(db.Integer)
    movie_name = db.Column(db.String(50))
    box_office = db.Column(db.Float)
    bo_per = db.Column(db.String(10))
    ntime = db.Column(db.String(20))

class Nodes(db.Model):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    image = db.Column(db.String(20))
    intro = db.Column(db.String(255))

class Edges(db.Model):
    __tablename__ = 'edges'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Integer)
    target = db.Column(db.Integer)
    relation = db.Column(db.String(50))

class Map_bo(db.Model):
    __tablename__ = 'map_bo'
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(20))
    box_office = db.Column(db.Float)
