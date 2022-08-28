from pymongo import MongoClient

mongodb_uri = 'mongodb+srv://youwaiting:youwaiting@demo.hs2gr1r.mongodb.net/Demo' 
port = 8000

client = MongoClient(mongodb_uri, port)
db = client["Demo"]