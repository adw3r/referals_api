import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.responses import JSONResponse

from config import HOST, PORT, DEBUG
from referals import get_referrals_from_json

app = FastAPI()


@app.get('/')
async def get_root():
    return RedirectResponse('/referals')


@app.get('/referals')
async def get_referrals():
    content = get_referrals_from_json()
    return JSONResponse(content=content)


if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=DEBUG)
