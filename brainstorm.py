from typing import Type
import question as Q
import testmssg as T
import careMssg as M


def determineQuestion(q):
    return getattr(Q,q)

def determineRequirements(q,a,d=[]):
    dummy_var = [
        { "quest" : "Q45", "ans" : "b" },
        { "quest" : "Q45", "ans" : "a" },
        { "quest" : "Q46", "ans" : "m" } ]

    newDummy_var = {
        "Q45":["a","b"],
        "Q46":["m"]
    }

    if q == "Q51":
        check = ["Q45","Q46"]
        checkLen = len(check)
        paramLen = 0
        for i in check:
            try:
                if newDummy_var[i]:
                    paramLen += 1
            except:
                paramLen = 1

        if checkLen != paramLen :
            print("Invalid!!")
            return 0

        ask_Q51 = a
        Q45 = newDummy_var["Q45"]
        Q46 = newDummy_var["Q46"]
        

        if Q45[1] == "b".lower() and Q46[0] == "m".lower() and ask_Q51 == "a".lower():
            # Q45 == NO and Q46 == M and ask_Q51 == YES
            # FV-14
            print(T.T202+"\n")
        elif Q45[0] == "a".lower() and Q46[0] == "m".lower() and ask_Q51 == "a".lower():
            # Q45 == YES and Q46 == M and ask_Q51 == YES
            # FV-15
            print(T.T201+"\n")
        elif Q45[1] == "b".lower() and Q46[0] == "m".lower() and ask_Q51 == "b".lower():
            # Q45 == NO and Q46 == M and ask_Q51 == NO
            # FV-16
            print(T.T201+"\n")
        elif Q45[0] == "a".lower() and Q46[0] == "m".lower() and ask_Q51 == "b".lower():
            # Q45 == YES and Q46 == M and ask_Q51 == NO
            # FV-17
            print(M.MSG304)
            print(T.T201+"\n")
        
    return 



def determineNxtQuest(curQ:str,curAns:str,pastQuestAns=None):
    return 0


#print(determineQuestion("Q0"))
#print(Q.Q0)

determineRequirements("Q51","a",[])