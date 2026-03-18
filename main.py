from enum import Enum
from fastapi import FastAPI
import settings

class FileHandler:
    url_pattern = settings.URL_PATTERN

    def __init__(self,object):
        self.object = object

    def get_line_add(self):
        list = []
        for chave, valor in self.object.__dict__.items():
            list.append(f'{chave}={valor}')
        return ";".join(list)+"\n"

    def get_by_line(self):
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
    
    def add_in_file(self):
        if not self.get_by_line():
            print ("... adding line.")
            file = open(self.file, "a")
            file.write(self.get_line_add())
            file.close()    

class Product:
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name

class ProductFH(FileHandler):

    def __init__(self, object):
        super().__init__(object)
        self.file = self.url_pattern+"products.txt"

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/file_handler/go")
async def file_handler_go():
    pfh1 = ProductFH(Product(1, "notebook"))
    pfh1.add_in_file()
    pfh2 = ProductFH(Product(2, "mouse"))
    pfh2.add_in_file()
    pfh3 = ProductFH(Product(3, "keyboard"))
    pfh3.add_in_file()
    pfh4 = ProductFH(Product(4, "monitor"))
    pfh4.add_in_file()
    return {"user_id": "The FileHandler went."}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}