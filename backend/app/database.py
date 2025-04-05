import asyncpg
from .postgres import database

async def insert_item(name: str, description: str) -> int:
    async with database.pool.acquire() as conn:
        row = await conn.fetchrow(
            "INSERT INTO items (name, description) VALUES ($1, $2) RETURNING id",
            name, description
        )
        return row["id"]

async def insert_image_urls(item_id: int, urls: list[str]):
    async with database.pool.acquire() as conn:
        for url in urls:
            await conn.execute(
                "INSERT INTO item_images (item_id, image_url) VALUES ($1, $2)",
                item_id, url
            )

async def get_item_with_images(item_id: int):
    async with database.pool.acquire() as conn:
        item = await conn.fetchrow("SELECT * FROM items WHERE id = $1", item_id)
        if not item:
            return None
        images = await conn.fetch("SELECT image_url FROM item_images WHERE item_id = $1", item_id)
        return {
            "id": item["id"],
            "name": item["name"],
            "description": item["description"],
            "images": [img["image_url"] for img in images]
        }
