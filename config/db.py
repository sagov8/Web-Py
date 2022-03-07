from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root123@localhost:3306/DatabaseTest")

meta = MetaData()

conn = engine.connect()