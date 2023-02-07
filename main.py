import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.responses import JSONResponse

from config import HOST, PORT
from referals import get_referals_from_json

app = FastAPI()


@app.get('/')
async def get_root():
    return RedirectResponse('/referals')


@app.get('/referals')
async def get_referals():
    content = get_referals_from_json()
    return JSONResponse(content=content)


if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=int(PORT))
