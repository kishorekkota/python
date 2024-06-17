from fastapi import FastAPI, Request
from time import sleep

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World from FastAPI. This is the root route."}



@app.get("/items/{item_id}")
def read_items(item_id: int,q: str = None):
    return {"item_id":item_id,"q":q}


@app.get("/items_async/")
async def read_item(request: Request):
    sleep(5)
    print("read item async")
    query_params = request.query_params
    return {"query_params":query_params}

  
@app.get("/items/")
def read_item(request: Request):
    sleep(5)
    print("read item sync")
    query_params = request.query_params
    return {"query_params":query_params}