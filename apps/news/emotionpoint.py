from snownlp import SnowNLP
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


# 创建一个会话
session = sessionmaker(engine)()
ids = session.query(Rmrb.id).all()
for i in ids:
    cons = session.query(Rmrb.content).filter(Rmrb.id == i[0]).first()
    if cons[0] is not None:
        poi = SnowNLP(cons[0]).sentiments
        news = session.query(Rmrb).filter(Rmrb.id == i[0]).first()
        news.point = poi
        session.commit()
        print(poi)




