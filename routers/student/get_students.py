from fastapi import FastAPI,APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
import os.path
import json
from db import get_db


from app.logger import setup_logging
import logging
from db.services.Student_Service import BaseSerVice, StudentServiceManager

setup_logging()
logger=logging.getLogger(__name__)
routers=APIRouter()

@routers.get("/get_all_student")
def get_student(db:Session=Depends(get_db)):
    logger.info("Request Received to get all student info")
    StudentServiceManager.display_all_student_details(db)
    return JSONResponse(
        status_code=200,
        content={"message":"Testing ok"}
    )
@routers.get("/get_student_by_id/{student_id}")
def get_students(student_id:int):
    logger.info("Request Received to get all student by id")
    return JSONResponse(
        status_code=200,
        content={"message":"ok"}

    )

