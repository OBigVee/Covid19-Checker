# From Pediatric - Enter Screening


import question as Q
import testmssg as T
import pediatric as P
import careMssg as M


def pediatricSymExposed(Q31):
    ask_Q7_PED = str(input(P.Q7_PED)).lower()
    if Q31 == "a".lower() and ask_Q7_PED == "n".lower():
        # Q31 – Positive And Q14-PED - “Other symptoms
        # PS-104
        return(print(M.MSG10+"\n"), print(M.MSG27+"\n"), print(T.T5+"\n"))
    elif Q31 == "b".lower() and ask_Q7_PED == "n".lower():
        # Q31 – Negative And Q14-PED - “Other symptoms
        # PS-105
        return(
        print(M.MSG10+"\n"),\
        print(M.MSG28+"\n"),\
        print(T.T6+"\n")\
        )

    elif Q31 == "c".lower() and ask_Q7_PED == "n".lower():
        # Q31 – Pending And Q14-PED - “Other symptoms
        # PS-106
        return(
        print(M.MSG10+"\n"),\
        print(M.MSG29+"\n"),\
        print(M.MSG31+"\n"),\
            )
    elif Q31 == "b".lower() and ask_Q7_PED == "n".lower():
        # Q31 – No Test And Q14-PED - “Other symptoms
        # PS-107
        return(
        print(M.MSG10+"\n"),\
        print(T.T4+"\n"),\
        print(M.MSG31+"\n"),\
        print(M.MSG30+"\n"),\
        )