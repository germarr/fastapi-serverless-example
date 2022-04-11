from fastAPIapp import app
import azure.functions as func

@app.get("/hello/{name}")
async def get_names(name:str):
    return{
        "name":f"Hello, my name is {name}"
    }

def main(req:func.HttpRequest, context:func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)