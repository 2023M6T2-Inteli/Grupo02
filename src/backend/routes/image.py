from fastapi import APIRouter
from supabase import create_client, Client



url = "https://xbjclntldtajiazipkem.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhiamNsbnRsZHRhamlhemlwa2VtIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODU3MjkyMzUsImV4cCI6MjAwMTMwNTIzNX0.Ln0EQ-nQ4zLhOpQNAItzLizO8vxcQuWceN_7qTUmdbg"
router = APIRouter(prefix="/images")


supabase: Client = create_client(supabase_url=url,
                                 supabase_key=key)


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
        #os.remove(f"{name}.txt")
        return get_all(f'{name}.txt')
    except Exception as e:
        return str(e)
