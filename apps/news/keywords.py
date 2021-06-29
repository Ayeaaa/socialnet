import jieba
from sqlalchemy import Column, Integer, String,Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 配置链接数据库信息
db_config = {
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'rmrb',
    'username': 'root',
    'password': '123456'
}
# 数据库链接地址
db_url = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8'.format(**db_config)
# 创建数据库引擎
engine = create_engine(db_url)
Base = declarative_base()
Base.metadata.create_all(engine)

class Rmrb(Base):
    __tablename__ = 'rmrb_all'
    id = Column(Integer, primary_key=True)
    date = Column(String(255))
    page = Column(String(255))
    tag = Column(String(255))
    title = Column(String(10000))
    url = Column(String(255))
    content = Column(String(10000))
    point = Column(Float)
    key = Column(String(255))


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
        if tf[seg] < 5 or len(seg) < 2 or seg in sw or "一" in seg:
            tf.pop(seg)
    ci = list(tf.keys())
    num = list(tf.values())
    data = []
    for i in range(len(tf)):
        data.append((num[i], ci[i]))
    data.sort()
    data.reverse()
    return data


# 创建一个会话
session = sessionmaker(engine)()
ids = session.query(Rmrb.id).all()
tt = []
ss = ""
for i in ids:
    cons = session.query(Rmrb.content).filter(Rmrb.id == i[0]).first()
    news = session.query(Rmrb).filter(Rmrb.id == i[0]).first()
    if cons[0] is not None:
        poi = cutword(cons[0])
        # print(poi)
        for p in poi:
            tt.append(p[1])
        key = tt[0:3]
        for k in key:
            ss += k
            ss += ' '
    news.key = ss
    session.commit()
    print(ss)
    tt.clear()
    ss = ""







