# From Pediatric - Enter Screening


import question as Q
import testmssg as T
import pediatric as P
import careMssg as M

def pediatricAsymPathway(Q3= "b"):
    ask_Q25_PED = str(input(P.Q25_PED)).lower()
    if ask_Q25_PED == "b".lower():
        # Q25_PED == NO
        # PA-1
        print(M.MSG1+"\n")
        print(M.MSG16+"\n")
        print(T.T0+"\n")
    else:
        ask_Q26_PED = str(input(P.Q26_PED)).lower()
        if ask_Q26_PED == "a".lower():
            # Q26_PED = YES
            # PA-2
            print(M.MSG25+"\n")
            print(T.T3+"\n")
        else:
            ask_Q27_PED = str(input(P.Q27_PED)).lower()
            if ask_Q27_PED == "b".lower():
                # Q27_PED = NO
                # PA-3
                print(M.MSG18+"\n")
                print(T.T3+"\n")
            else:
                # Q27_PED = YES
                # PA-4
                print(M.MSG17+"\n")
                print(M.MSG26+"\n")
                print(T.T3+"\n")
