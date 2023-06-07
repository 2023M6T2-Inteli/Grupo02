from fastapi import APIRouter
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("url")
key = os.getenv("api_key")
router = APIRouter(prefix="/images")


supabase: Client = create_client(supabase_url="",
                                 supabase_key="")


@router.get("/get/{file}")
async def get_all(file):
    address = supabase.storage.from_("/test").get_public_url(f"{file}")
    return address


@router.post("/add")
async def store_image(msg: dict):
    image = msg["image"]
    name = msg["name"]
    try:
        f = open(f"{name}.txt", "w")
        f.write(image)
        f.close()

        with open(f"{name}.txt", "rb+") as f:
            file = f.read()
            f.close()
        res = supabase.storage.from_("/test").upload(f"{name}.txt", file)
        os.remove(f"{name}.txt")
        return get_all(f'{name}.txt')
    except Exception as e:
        return str(e)
