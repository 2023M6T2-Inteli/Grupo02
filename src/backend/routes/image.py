from fastapi import APIRouter
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("url")
key = os.getenv("api_key")
router =APIRouter(prefix="/images")


supabase:Client = create_client(supabase_url="https://xbjclntldtajiazipkem.supabase.co",
                                supabase_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhiamNsbnRsZHRhamlhemlwa2VtIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODU3MjkyMzUsImV4cCI6MjAwMTMwNTIzNX0.Ln0EQ-nQ4zLhOpQNAItzLizO8vxcQuWceN_7qTUmdbg")


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