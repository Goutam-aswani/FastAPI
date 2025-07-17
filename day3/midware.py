import time
from fastapi import Request, FastAPI

app = FastAPI()

@app.middleware("http")
async def time_process(request : Request,call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time =time.time() - start_time
    response.headers["X-process time"] = str(process_time)
    print(response)
    return response

@app.get("/")
async def main():
    return {"hello" : "world"}
