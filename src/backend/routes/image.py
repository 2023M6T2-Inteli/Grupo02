from fastapi import APIRouter
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("url")
key = os.getenv("api_key")
router =APIRouter(prefix="/images")


supabase:Client = create_client(supabase_url="",supabase_key="")


@router.get("/get/{file}")
async def get_all(file):
   
    return supabase.storage.from_("/Images").get_public_url(f"{file}")
# @router.post("/add")
# async def store_image(image:str,name:str):
#     try:
#         res =supabase.storage.from_("Images").upload(f"{name}.txt",image)
#         return str(res)
#     except Exception as e:
#         return e