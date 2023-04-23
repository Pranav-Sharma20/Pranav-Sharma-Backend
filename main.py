from fastapi import FastAPI
from routes.route import client

app = FastAPI()
app.include_router(client)

