from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
from routers.sight import db_init, sightRouter

app = FastAPI()
app.include_router(sightRouter)

app.mount("/", StaticFiles(directory="static", html=True), name="static")

# @app.get('/favicon.ico')
# async def get_favicon():
#     return FileResponse('static/favicon.ico')

# @app.get("/")
# async def get_index():
#     return FileResponse('static/index.html')
