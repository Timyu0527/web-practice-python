from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from crawler.keelungSightsCrawler import KeelungSightsCrawler
from starlette.responses import FileResponse 

app = FastAPI() # 建立一個 Fast API application

crawler = KeelungSightsCrawler()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/favicon.ico')
async def get_favicon():
    return FileResponse('static/favicon.ico')

@app.get("/")
async def get_index():
    return FileResponse('static/index.html')

@app.get("/SightAPI") # 指定 api 路徑 (get方法)
def get_sight(zone: Optional[str] = None):
    return crawler.getItem(zone)

