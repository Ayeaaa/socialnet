from . import db


class Rmrb(db.Model):
    __tablename__ = 'rmrb_copy2'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(255))
    page = db.Column(db.String(255))
    tag = db.Column(db.String(255))
    title = db.Column(db.String(10000))
    url = db.Column(db.String(255))
    content = db.Column(db.String(10000))


class Nodes(db.Model):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    intro = db.Column(db.String(255))
    outdegree = db.Column(db.Integer)
    indegree = db.Column(db.Integer)
    pagerank = db.Column(db.Float)
    centrality = db.Column(db.Float)


class Edges(db.Model):
    __tablename__ = 'edges'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(255))
    target = db.Column(db.String(255))
    weight = db.Column(db.Integer)