# from enter screen
import question as Q
import testmssg as T
import pediatric as P
import careMssg as M

import fully_vacinated_sym
import fully_vacinated_asym

def fullyVacinated(Q39):
    
    ask_Q40 = str(input(Q.Q40)).lower()
    ask_Q41 = str(input(Q.Q41)).lower()
    ask_Q42 = str(input(Q.Q42)).lower()
    ask_Q43 = str(input(Q.Q43)).lower()
    ask_Q44 = str(input(Q.Q44)).lower()
    ask_Q52 = str(input(Q.Q52)).lower()
    if ask_Q52 == "a":
        # Q52 = Yes
        # FV-1
        print(M.MSG4)
    else:
        ask_Q45 = str(input(Q.Q45)).lower()
        ask_Q46 = str(input(Q.Q46)).lower()
        if ask_Q45 != "b" and ask_Q46 == "l":
            # Q46 = l Q45 = Yes or I don’t know
            # FV-2
            print(M.MSG304)
        elif ask_Q45 == "b" and ask_Q46 =="l":
            # Q46 = l Q45 = No
            # FV-3
            print(T.T201)
        elif ask_Q45 != "b" and ask_Q46 !="m":
            # Q46 is not equal  to M and Q45 = Yes or No or I don’t know
            # GOTO Fully Vaccinated Sysmptomatic
            return fully_vacinated_sym.fullyVaccinated_Symptomatic(ask_Q40, ask_Q41, ask_Q45,ask_Q46)
        elif ask_Q45 != "None" and ask_Q46 =="m":
            # Q45 = Yes or No or I don’t know and Q46 = M
            # Goto fully Vaccinated Asymptomatic
            return fully_vacinated_asym.fullyVaccinated_Asymptomatic(ask_Q45,ask_Q46)
            