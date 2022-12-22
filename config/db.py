from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://arsalan:123@localhost:3306/fast_api')

meta = MetaData()

conn = engine.connect()