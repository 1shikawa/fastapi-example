from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine

# テーブル作成
metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/movies/openapi.json", docs_url="/api/v1/movies/docs")
# app = FastAPI()

# 起動時にDBに接続する
@app.on_event("startup")
async def startup():
    await database.connect()

# 終了時にDBを切断する
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# movies routerを登録する
app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])
