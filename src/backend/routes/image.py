from fastapi import APIRouter
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("url")
key = os.getenv("api_key")
router = APIRouter(prefix="/images")


supabase: Client = create_client(supabase_url="https://xbjclntldtajiazipkem.supabase.co",
                                 supabase_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhiamNsbnRsZHRhamlhemlwa2VtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTcyOTIzNSwiZXhwIjoyMDAxMzA1MjM1fQ.LR3l7jL_i3WR4NsU6350WetqdIQSOBf8RZdTG7KzJM0")


@router.get("/get/{file}")
async def get_all(file):

    return supabase.storage.from_("/test").get_public_url(f"{file}")


@router.post("/add")
async def store_image(name: dict):
    text = name["text"]
    name = name["name"]
    try:
        f = open(f"{name}.txt", "w")
        f.write(text)
        f.close()

        with open(f"{name}.txt", "rb+") as f:
            file = f.read()
            f.close()
        res = supabase.storage.from_("/test").upload(f"{name}.txt", file)
        os.remove(f"{name}.txt")
        return name
    except Exception as e:
        return str(e)
