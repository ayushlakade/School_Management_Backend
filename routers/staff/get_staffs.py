from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse

from app.logger import setup_logging
import logging

setup_logging()
logger=logging.getLogger(__name__)
routers=APIRouter()

@routers.get("/")
def get_staff():
    logger.info("Request Received ti get all staff info")
    return JSONResponse(
        status_code=200,
        content={"message":"Testing ok"}
    )
