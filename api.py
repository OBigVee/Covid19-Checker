from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import question as Q
import careMssg as M
import testmssg as T
import file as F

import question as Q
import pediatric as P
import careMssg as M
import testmssg as T


app = FastAPI()


@app.get("/")
async def read_item(questionId: str, preAnswer: str):
    return {"current_questionId": questionId,
            "prev_question": " ",
            "next_questionId": "dummy"
            } 

# def disclaimer(y):
#     print(y)
#     return {"message":"this"}
   # return (F.data["testMessage"]['disclaimer'])


@app.get("/intro-mssg")
def introMessage():
    return{M.introMessage}


@app.get("/country")
# Q0
def askCountry():
    return Q.Q0


@app.get("/state")
# Q0A
def askState():
    return Q.Q0A


@app.get("/assessment-permission")
# Q4
def assessmentPermission():
    return(Q.Q4)


@app.get("/are-you-vaccinated")
# Q39
def ask_Q39():
    return (Q.Q39)


@app.get("/age")
# age for non vaccinated
def ask_Q2():
    return (Q.Q2)
