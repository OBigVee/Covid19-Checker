import careMssg as M
import question as Q
import pediatric as P
import secrets as s

class Covid:

    def __init__(self):
        self.pastAnswers = {}
        self.token = None

    def generateToken(self):
        self.token = s.token_hex(16)
        return self.token

    def updateQuestionStack(self, ques, ans):
        self.pastAnswers.update({ques: ans})

    def createUser(self):
        new_token = self.generateToken()
        return { "token": new_token}

    def handleQuestion(self, quest, resp=None, get_question=True):
        newName = "question" + str(quest[1::])
        try:
            q = getattr(self, newName)
            return q(resp=resp, get_question=get_question)
        except:
            return {"isError": True, "goTo": None, "quest": None, "ans": resp, "type": "get" if get_question else "analyze" ,"msg": None, "next_question": None}

    def question39(self, resp=None, get_question=True):
        if get_question:
            return {"isError": False, "goTo": None, "quest": Q.Q39, "ans": resp, "type": "get","msg": None, "next_question": None}
        else:
            if resp == "a":
                self.updateQuestionStack("Q39", resp)
                return {"isError": False, "goTo": "Q40", "quest": Q.Q39, "ans": resp, "type": "analyze", "msg": None, "next_question": Q.Q40}
            elif resp == "b":
                self.updateQuestionStack("Q39", resp)
                return {"isError": False, "goTo": "Q2", "quest": Q.Q39, "ans": resp, "type": "analyze", "msg": None, "next_question": Q.Q2}
            else:
                return {"isError": True, "goTo": None, "quest": Q.Q39, "ans": resp, "type": "analyze", "msg": "Invalid answer", "next_question": None}

    def question2(self, resp=None, get_question=True):
        if get_question:
            return {"isError": False, "goTo": None, "quest": Q.Q2, "ans": resp, "type": "get", "msg": None , "next_question": None}
        else:
            if resp in "abcde":
                self.updateQuestionStack("Q2", resp);
                return self.screening(resp=resp, get_question=False)
            elif resp in "fghijklm":
                self.updateQuestionStack("Q2", resp)
                return {"isError": False, "goTo": "Q5", "quest": Q.Q2, "ans": resp, "type": "analyze", "msg": None, "next_question": Q.Q5}
            else:
                return {"isError": True, "goTo": None, "quest": Q.Q2, "ans": resp, "type": "analyze", "msg": None, "next_question": None}

    def question5(self, resp=None, get_question=True):
        if get_question:
            return {"isError": False, "goTo": None, "quest": Q.Q5, "ans": resp, "type": "get","msg": None, "next_question": None}
        else:
            self.updateQuestionStack("Q5", resp)
            return {"isError": False, "goTo": "Q35", "quest": Q.Q5, "ans": resp, "type": "analyze", "msg": None, "next_question": Q.Q35}

    def screening(self, resp=None, get_question=True):
        if get_question:
            return {"isError": False, "goTo": None, "quest": Q.Q2, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            if resp in "a":
                self.updateQuestionStack("Q2", resp)
                return {"isError": False, "goTo": None, "quest": Q.Q2, "ans": resp, "type": "analyze", "msg": M.MSG19, "next_question": None}
            elif resp in "bc":
                self.updateQuestionStack("Q2", resp)
                return {"isError": False, "goTo": None, "quest": Q.Q2, "ans": resp, "type": "analyze", "msg": M.MSG20, "next_question": None}
            elif resp in "d":
                self.updateQuestionStack("Q2", resp)
                return {"isError": False, "goTo": "Q5-PED", "quest": Q.Q2, "ans": resp, "type": "analyze",
                        "msg": M.MSG21, "next_question": P.Q5_PED }
            elif resp in "e":
                self.updateQuestionStack("Q2", resp)
                return {"isError": False, "goTo": "Q5-PED", "quest": Q.Q2, "ans": resp, "type": "analyze",
                        "msg": M.MSG22, "next_question": P.Q5_PED}
            else:
                return {"isError": True, "goTo": None, "quest": Q.Q2, "ans": resp, "type": "analyze", "msg": None, "next_question": None}

    # def newName(self, resp, get_question):
    #    pass


# C = Covid()
# quest = C.handleQuestion(quest="Q39", resp="b", get_question=False);
# quest = C.question5(resp="f", get_question=False)
# print(C.pastAnswers)
# print("/n")
# print(quest)
