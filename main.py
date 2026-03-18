from enum import Enum
from fastapi import FastAPI
import settings

class FileHandler:
    url_pattern = settings.URL_PATTERN
    object = None

    def get_line_add(self):
        list = []
        for chave, valor in self.object.__dict__.items():
            list.append(f'{chave}={valor}')
        return ";".join(list)+"\n"

    def get_by_line(self):
        if not self.object:
            return False
        print ("... Mounting line.")
        line_mount = self.get_line_add()
        print ("... Looking for existing line in file.")
        file = open(self.file, "r")
        line_finded = ""
        while len(line := file.readline()):
            if line==line_mount:
                print ("... Line found.")
                line_finded=line_mount
                break
        file.close()
        line_exists = (line_finded!="")
        return line_exists

    def get_by_pk(self, pk):
        result = []
        file = open(self.file, "r")
        while len(line := file.readline()):
            item = {}
            parts = line.split(";")
            pk_line = parts[0].split("=")[1]
            if pk_line == str(pk):            
                for part in parts:
                    key, value = part.split("=")
                    item[key] = value
                result.append(item)
                break
        file.close()
        return result

    def add(self):
        if not self.get_by_pk(self.object.pk):
            print ("... adding line.")
            file = open(self.file, "a")
            file.write(self.get_line_add())
            file.close()
            return True
        return False

    def list(self):
        result = []
        file = open(self.file, "r")
        while len(line := file.readline()):
            item = {}
            parts = line.split(";")
            for part in parts:
                key, value = part.split("=")
                item[key] = value
            result.append(item)
        return result

class Product:
    def __init__(self, pk, name):
        self.pk = pk
        self.name = name

class ProductFH(FileHandler):
    def __init__(self):
        super().__init__()
        self.file = self.url_pattern+"products.txt"

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Store API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "online"
    }

@app.get("/items/add/{pk}/{name}")
async def file_handler_add(pk: int, name: str):
    pfh1 = ProductFH()
    pfh1.object = Product(pk, name)
    if pfh1.add():
        return {"message": "Done."}
    return {"message": "PK Already exists."}

@app.get("/items")
async def read_items():
    pfh1 = ProductFH()
    return pfh1.list()

@app.get("/items/{pk}")
async def read_item(pk: int):
    pfh1 = ProductFH()
    object_ = pfh1.get_by_pk(pk)
    if object_:
        return object_[0]
    return {"message": "Item not found."}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "Current user: Me(Opened access)"}