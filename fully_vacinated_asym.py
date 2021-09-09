# FROM FULLY VACCINATED

import question as Q
import testmssg as T
import pediatric as P
import careMssg as M


def fullyVaccinated_Asymptomatic(Q45, Q46):
    ask_Q50 = str(input(Q.Q50)).lower()
    if ask_Q50 == "a".lower():
        if Q45 == 'b'.lower() and Q46 == "m".lower() and ask_Q50 == "a".lower():
            # Q50 = YEs and Q46 = m and Q45 = NO
            # FV-12
            print(T.T202)
        elif Q45 == 'a'.lower() and Q46 == "m".lower() and ask_Q50 == "a".lower():
            # Q50 = YEs and Q46 = m and Q45 = Yes
            # FV-13
            print(M.MSG305+"\n")
            print(M.MSG303+'\n')
    else:
        ask_Q50 = "b".lower()
        ask_Q51 = str(input(Q.Q51)).lower()
        if Q45 == "b".lower() and Q46 == "m".lower() and ask_Q51 == "a".lower():
            # Q45 == NO and Q46 == M and ask_Q51 == YES
            # FV-14
            print(T.T202+"\n")
        elif Q45 == "a".lower() and Q46 == "m".lower() and ask_Q51 == "a".lower():
            # Q45 == YES and Q46 == M and ask_Q51 == YES
            # FV-15
            print(T.T201+"\n")
        elif Q45 == "b".lower() and Q46 == "m".lower() and ask_Q51 == "b".lower():
            # Q45 == NO and Q46 == M and ask_Q51 == NO
            # FV-16
            print(T.T201+"\n")
        elif Q45 == "a".lower() and Q46 == "m".lower() and ask_Q51 == "b".lower():
            # Q45 == YES and Q46 == M and ask_Q51 == NO
            # FV-17
            print(M.MSG304)
            print(T.T201+"\n")