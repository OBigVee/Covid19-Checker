# From Pediatric - Enter Screening


import question as Q
import testmssg as T
import pediatric as P
import careMssg as M



def pediatricSymNonExposed(Q31):
    ask_Q14_PED = str(input(P.Q14_PED)).lower()
    if Q31 == "a".lower() and ask_Q14_PED == "n".lower():
        # Q31 – Positive And Q14-PED - “Other symptoms
        # PS-108
        print(M.MSG10+"\n")
        print(M.MSG27+"\n")
        print(T.T5+"\n")
    elif Q31 == "b".lower() and ask_Q14_PED == "n".lower():
        # Q31 – Negative And Q14-PED - “Other symptoms
        # PS-109
        print(M.MSG10+"\n")
        print(M.MSG28+"\n")
        print(T.T6+"\n")
    elif Q31 == "c".lower() and ask_Q14_PED == "n".lower():
        # Q31 – Pending And Q14-PED - “Other symptoms
        # PS-110
        print(M.MSG10+"\n")
        print(M.MSG29+"\n")
    elif Q31 == "b".lower() and ask_Q14_PED == "n".lower():
        # Q31 – No Test And Q14-PED - “Other symptoms
        # PS-111
        print(M.MSG10+"\n")
        print(T.T4+"\n")
        print(M.MSG30+"\n")