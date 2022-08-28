from fastapi import APIRouter
from typing import  Optional
from config.database import db
from crawler.keelungSightsCrawler import KeelungSightsCrawler

sightRouter = APIRouter()
collection = db["sight_python"]

def db_init():
    id = 0
    crawler = KeelungSightsCrawler()
    sights = crawler.getAllSight()
    for sight in sights:
        if collection.find_one({'_id': str(id)}) == None:
            collection.insert_one({'_id': str(id), **sight.dict()})
            id += 1

db_init()

@sightRouter.get("/SightAPI")
def get_sight(zone: Optional[str] = None):
    return list(collection.find({'zone': zone + "區"}))