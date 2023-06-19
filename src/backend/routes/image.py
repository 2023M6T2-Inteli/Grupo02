import shutil
from fastapi import APIRouter, File, UploadFile
from supabase import create_client, Client
from datetime import datetime

import os

# load_dotenv()
url = "https://exwsjbueckvbqbvtahzr.supabase.co"#os.getenv("url")
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV4d3NqYnVlY2t2YnFidnRhaHpyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjY2NjYxMCwiZXhwIjoyMDAyMjQyNjEwfQ.k5B0bBc3ttbSlnvOzqQZldVQZYcOf7cxum9Eg3blavI"#os.getenv("api_key")
bucket_name = "bucket_teste"
image_router = APIRouter(prefix="/images")


supabase: Client = create_client(supabase_url=url,
                                 supabase_key=key)


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

@image_router.post("/send_supabase")
async def upload_image(file: UploadFile = File(...)):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{timestamp}_{file.filename}"
    print("File name: ", file.filename)
    print("File file: ", file.file)

    with open(f"/home/amandafontes/M6/Safe-McQueen/src/backend/supabase_images/{file_name}", "wb") as w:
        shutil.copyfileobj(file.file, w)
        with open(f"supabase_images/{file_name}", "+rb") as r:
            
            my_string = r.read()
            supabase.storage.from_(bucket_name).upload(f"{file_name}", my_string)

    image_url = f"{url}/storage/v1/object/public/{bucket_name}/{file_name}"
    
    return image_url