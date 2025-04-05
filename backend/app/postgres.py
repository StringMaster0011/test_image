import asyncpg
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE  = os.getenv("DB_DATABASE")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

class PostgresConnection:
    def __init__(self, db_url:str):
        self.db_url = db_url

    async def connect(self):
        self.pool = await asyncpg.create_pool(self.db_url)

    async def disconnect(self):
        self.pool.close()

database = PostgresConnection(DB_URL)