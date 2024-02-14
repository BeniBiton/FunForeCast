import uvicorn
from fastapi import FastAPI

from backend.api.routes.dates import router as dates_router

app = FastAPI()

app.include_router(dates_router)


if __name__ == '__main__':
    uvicorn.run(app)
