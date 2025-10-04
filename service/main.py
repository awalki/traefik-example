from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

items = {
    1: "MacBook Air M4 13.6",
    2: "iPhone 17 Pro Max",
    3: "iPad Pro 14.4",
}


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"items": items}
    )
