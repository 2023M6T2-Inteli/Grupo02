import shutil
from fastapi import APIRouter
from supabase import create_client, Client
from datetime import datetime
from fastapi import  File, UploadFile
import os

# load_dotenv()
url = "https://xwotfvgmtbaarrqamwcn.supabase.co"#os.getenv("url")
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh3b3RmdmdtdGJhYXJycWFtd2NuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4Njg0NDIxNCwiZXhwIjoyMDAyNDIwMjE0fQ.UxjJWdWQk8POSV0OpYkEyw-XBqYaaByXyRBrlj31LSs"#os.getenv("api_key")
bucket_name = "imagens"
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

    with open(f"../supabase_images/{file_name}", "wb") as w:
        shutil.copyfileobj(file.file, w)
        with open(f"supabase_images/{file_name}", "+rb") as r:
            
            my_string = r.read()
            supabase.storage.from_(bucket_name).upload(f"{file_name}", my_string)

    image_url = f"{url}/storage/v1/object/public/imagens/{file_name}"
    
    return image_url