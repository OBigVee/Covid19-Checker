from fastapi import FastAPI, Response, status
from CovidE import Covid
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_item(questionId :Optional[str] = None, preAnswer:Optional[str] = None):
    return { "message": "Welcome" }


@app.get("/respond", status_code=200)
def read_item(questionId :Optional[str] = None, ans:Optional[str]=None, response: Response = None):
    if questionId == None or ans == None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": "Question id or Answer is required" }

    C = Covid()
    response.status_code = status.HTTP_200_OK
    getResponse = C.handleQuestion(quest=questionId, resp=ans, get_question=False)

    if(getResponse["isError"]): #if there is an error
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message":getResponse["msg"] if getResponse["msg"] else "Not found" }

    return {
        "message":  getResponse["msg"] if getResponse["msg"] else "Answer sent and saved successfully.",
        "next_quest_id": getResponse["goTo"],
        "current_question": getResponse["quest"],
        "current_answer": getResponse["ans"],
        "next_question": getResponse["next_question"]
    }

# @app.post("/", status_code=200)
# def create_user(response: Response = None):


@app.get("/question", status_code=200)
def read_item(questionId :Optional[str] = None, response: Response = None):
    if questionId == None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": "Question id is required" }

    C = Covid()
    response.status_code = status.HTTP_200_OK
    getResponse = C.handleQuestion(quest=questionId, resp=None, get_question=True)

    if getResponse["isError"]: #if there is an error
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message":getResponse["msg"] if getResponse["msg"] else "Not found" }

    return {
        "message":  getResponse["msg"] if getResponse["msg"] else "Question returned successfully.",
        "current_question": getResponse["quest"]
    }