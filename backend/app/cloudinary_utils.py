import cloudinary
import cloudinary.uploader
from app.config import CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

async def upload_to_cloudinary(file, folder: str):
    # Upload image to: item_image/items/item_<item_id>/
    full_folder_path = f"item_image/{folder}"
    result = cloudinary.uploader.upload(
        file.file,
        folder=full_folder_path
    )
    return result["secure_url"]
