import careMssg as M
import question as Q
import pediatric as P
import secrets as s


class Covid:

    def __init__(self):
        self.pastAnswers = {}
        self.token = None


    def generateToken(self):
        # generate unique tokens
        self.token = s.token_hex(16)
        return self.token


    def updateQuestionStack(self, ques, ans):
        # update question and answer
        self.pastAnswers.update({ques: ans})


    def createUser(self):
        # users get a new token
        new_token = self.generateToken()
        return {"token": new_token}


    def handleQuestion(self, quest, resp=None, get_question=True):
        # function handles current question and detect what question to get next
        """
        quest: question
        resp : response or answer
        get_question: boolean detects if there's a further question or not
        """
        newName = "question" + str(quest[1::]) # get the question int value

        try:
            q = getattr(self, newName)
            return q(resp=resp, get_question=get_question)
        except:
            return {"isError": True, "goTo": None, "quest": None, "ans": resp, "type": "get" if get_question else "analyze", "msg": None, "next_question": None}


    def question39(self, resp=None, get_question=True):
        if get_question:
            return {"isError": False, "goTo": None, "quest": Q.Q39, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            if resp == "a":
                # enter fully vaccination screen
                self.updateQuestionStack("Q39", resp)
                return {"isError": False, "goTo": "Q40", "quest": Q.Q39, "ans": resp, "type": "analyze", "msg": None, "next_question": Q.Q40}
            elif resp == "b":
                self.updateQuestionStack("Q39", resp)
                return {"isError": False, "goTo": "Q2", "quest": Q.Q39, "ans": resp, "type": "analyze", "msg": None, "next_question": Q.Q2}
            else:
                return {"isError": True, "goTo": None, "quest": Q.Q39, "ans": resp, "type": "analyze", "msg": "Invalid answer", "next_question": None}


    def question2(self, resp=None, get_question=True):
        if get_question:
            return {"isError": False, "goTo": None, "quest": Q.Q2, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            if resp in "abcde":
                self.updateQuestionStack("Q2", resp)
                return self.screening(resp=resp, get_question=False)
            elif resp in "fghijklm":
                self.updateQuestionStack("Q2", resp)
                return {"isError": False, "goTo": "Q5", "quest": Q.Q2, "ans": resp, "type": "analyze", "msg": None, "next_question": Q.Q5}
            else:
                return {"isError": True, "goTo": None, "quest": Q.Q2, "ans": resp, "type": "analyze", "msg": None, "next_question": None}


    def question5(self, resp=None, get_question=True):
        if get_question:
            return {"isError": False, "goTo": None, "quest": Q.Q5, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            self.updateQuestionStack("Q5", resp)
            return {"isError": False, "goTo": "Q35", "quest": Q.Q5, "ans": resp, "type": "analyze", "msg": None, "next_question": Q.Q35}
    
    def question35(self, resp=None, get_question=True):
        if get_question:
            return {"isErrofr": False, "goTo": "Q36", "quest": Q.Q35, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            self.updateQuestionStack("Q35", resp)
            return {"isError" : False, "goTo": "Q36", "quest": Q.Q36, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q36 }

    def question36(self, resp=None, get_question=True):
        if get_question:
            return {"isErrofr": False, "goTo": "Q37", "quest": Q.Q36, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            self.updateQuestionStack("Q36", resp)
            return {"isError" : False, "goTo": "Q37", "quest": Q.Q36, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q37 }
    
    def question37(self, resp=None, get_question=True):
        if get_question:
            return {"isErrofr": False, "goTo": "Q1", "quest": Q.Q37, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            return {"isError" : False, "goTo": "Q1", "quest": Q.Q37, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q1 }

    def question1(self, resp=None, get_question=True):
        if get_question:
            return {"isErrofr": False, "goTo": None, "quest": Q.Q1, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            if resp == 'a':
                self.updateQuestionStack("Q1",resp)
                return {"isError": False, "goTo": None, "quest": Q.Q1, "ans": resp, "type": "get", "msg": M.MSG4, "next_question": None}
            elif resp == 'b':
                self.updateQuestionStack("Q1",resp)
                return {"isError" : False, "goTo": "Q3", "quest": Q.Q1, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q3 }

    def question3(self, resp=None, get_question=True):
        if get_question:
            return {"isErrofr": False, "goTo": None, "quest": Q.Q1, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            if resp == "a":
                self.updateQuestionStack("Q3", resp)
                return {"isError": False, "goTo": "Q6", "quest": Q.Q3, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q6 }
            elif resp == "b":
                self.updateQuestionStack("Q3", resp)
                return {"isError": False, "goTo": "Q6", "quest": Q.Q3, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q25 }
        
    def question6(self, resp=None, get_question=True):
        self.resp6 = resp
        if get_question:
            return { "isError": False, "goTo": None, "quest":Q.Q6, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            self.updateQuestionStack("Q6", resp)
            return {"isError": False, "goTo": "Q31", "quest":Q.Q6, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q31}

    def question31(self, resp=None, get_question=True):
        self.resp31 = resp
        if get_question:
            return { "isError": False, "goTo": None, "quest":Q.Q6, "ans": resp, "type": "get", "msg": None, "next_question": None}
        else:
            # consider question 6 response and 
            if resp in "abcd" and self.resp6 in "ab" : # GOTO Adult Symptomatic Exposed
                self.updateQuestionStack("Q31", resp)
                return { "isError": False, "goTo": "Q7", "quest":Q.Q31, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q7}

            elif resp in "abcd" and self.resp6 == "b": #GOTO Adult Symptomatic Non-Exposed 
                self.updateQuestionStack("Q31", resp)
                return { "isError": False, "goTo": "Q14", "quest":Q.Q31, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q14}
            elif resp == "e" and self.resp6 in "abc": #GOTO Adult Symptomatic > 10 days of test
                self.updateQuestionStack("Q31", resp)
                return { "isError": False, "goTo": "Q201", "quest":Q.Q31, "ans": resp, "type": "get", "msg": None, "next_question": Q.Q201}
            






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
                        "msg": M.MSG21, "next_question": P.Q5_PED}
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
