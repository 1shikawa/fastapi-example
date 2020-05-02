import os

# モデル定義とクエリ生成
from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, ARRAY)
# DBアクセス
from databases import Database

# 環境変数から取得
DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', String(50)),
    Column('casts', String(250))
    # Column('genres', ARRAY(String)),
    # Column('casts', ARRAY(String))
)

database = Database(DATABASE_URI)
