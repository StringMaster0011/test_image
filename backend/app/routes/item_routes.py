from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List
from app.database import insert_item, insert_image_urls, get_item_with_images
from app.cloudinary_utils import upload_to_cloudinary

router = APIRouter()

@router.post("/admin/upload-item")
async def upload_item(
    name: str = Form(...),
    description: str = Form(...),
    files: List[UploadFile] = File(...)
):
    try:
        # Step 1: Create item and get ID
        item_id = await insert_item(name, description)
        
        # Step 2: Upload all images to Cloudinary under item_image/items/item_<item_id>
        folder = f"items/item_{item_id}"
        image_urls = []
        for file in files:
            url = await upload_to_cloudinary(file, folder)
            image_urls.append(url)
        
        # Step 3: Save URLs to DB
        await insert_image_urls(item_id, image_urls)

        return {
            "message": "Item uploaded successfully",
            "item_id": item_id,
            "image_urls": image_urls
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    item = await get_item_with_images(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
