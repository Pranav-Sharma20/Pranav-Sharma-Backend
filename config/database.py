from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ps25372:<password>@cluster0.3iahorv.mongodb.net/?retryWrites=true&w=majority"
conn = MongoClient(uri)
