from fastapi import APIRouter
from supabase import create_client, Client
import os

# load_dotenv()
url = os.getenv("url")
key = os.getenv("api_key")
image_router = APIRouter(prefix="/images")


supabase: Client = create_client(supabase_url="https://yvcygvkxsivgalfdzckg.supabase.co",
                                 supabase_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2Y3lndmt4c2l2Z2FsZmR6Y2tnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTcyOTYxNSwiZXhwIjoyMDAxMzA1NjE1fQ.yZR1pgyBHbIHv8qJjQ6_GxB1PNQt9dnBqh09j_-n9AA")


@image_router.get("/get/{file}")
async def get_all(file):
    address = supabase.storage.from_("/test").get_public_url(f"{file}")
    return address


@image_router.post("/add")
async def store_image(msg: dict):
    image = msg["image"]  # a imagem definida em base64
    name = msg["name"]  # nome para a imagem
    try:
        f = open(f"{name}.txt", "w")
        f.write(image)
        f.close()

        with open(f"{name}.txt", "rb+") as f:
            file = f.read()
            f.close()
        supabase.storage.from_("/test").upload(f"{name}.txt", file)
        os.remove(f"{name}.txt")
        return get_all(f'{name}.txt')
    except Exception as e:
        return str(e)