from fastapi import FastAPI
from routers import path_parameter, query_parameter, request_body


app = FastAPI()
app.include_router(path_parameter.router)
app.include_router(query_parameter.router)
app.include_router(request_body.router)


# GET method
@app.get("/")
def read_root():

    return {
        "Hello": "World",
    }
