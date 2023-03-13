import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.responses import JSONResponse

from config import HOST, PORT, DEBUG
from referals import get_referrals_from_json

app = FastAPI()
referrals = get_referrals_from_json()


@app.get('/')
async def get_root():
    return RedirectResponse('/referals')


@app.get('/referals')
async def get_referrals():
    return JSONResponse(content=referrals)


if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=DEBUG)
