from fastapi import FastAPI
from app.logger import setup_logging
from routers.student import get_students
import logging




setup_logging()
logger=logging.getLogger(__name__)
app=FastAPI()
logger.info("School Backend application is getting started")
app.include_router(get_students.routers)