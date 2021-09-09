# FROM FULLY VACCINATED

import question as Q
import testmssg as T
import pediatric as P
import careMssg as M

def fullyVaccinated_Symptomatic(Q40, Q41, Q45, Q46):
    """Q40 = age , Q41 = gender, Q45 ="""
    ask_Q47 = str(input(Q.Q47)).lower()
    if (Q45=="b".lower() and Q46 != "m".lower() and ask_Q47 == "a".lower() ):
        # ask_Q47 = Yes and Q45 = Yes or I don’t know and Q46 = a-l
        # FV-4
        print(M.MSG300+"\n")
        print(T.T200+"\n")
    elif (Q45=="a".lower() or "c".lower() and Q46 != "m".lower() and ask_Q47 == "a".lower()):
        # ask_Q47 = Yes  or IDk and Q45 = Yes or I don’t know and Q46 = a-l
        # FV-5
        print(M.MSG300+"\n")
        print(T.T200+"\n") 

    else:
        ask_Q48 = str(input(Q.Q48)).lower()
        if ask_Q48 == "a".lower():
            # Q48 = yes

            if ask_Q48 == "a".lower() and Q45 == "b".lower() and Q46 !="m".lower() :
                # FV-6
                #Q48 = Yes and Q45 = No and Q46 = a-l
                print(M.MSG302+"\n")
                print(T.T200+"\n")
            elif ask_Q48 == "a".lower() and Q45 == "a".lower() or "c".lower()  and Q46 !="m".lower():
                # FV-7
                #Q48 = Yes and Q45 = yes or IDK and Q46 = a-l
                print(M.MSG302+"\n")
                print(T.T200+"\n")
            
        else:
            # Q48 = no 
            # confirm (age) Q40 is not >= 80 and (gender)Q41 is not Male 
            if Q40 != "j".lower() or "i".lower() or "" and Q41 !="a".lower():
                ask_Q49_preg = str(input(Q.Q49_Pregnacy)).lower()
                if ask_Q49_preg == "b".lower():
                    # Q49_pregnacy = NO
                    if Q45 == "b".lower() and Q46 !="m".lower() and ask_Q49_preg =="b".lower():
                        # Q45 = NO and Q46 != m and 49_preg = No
                        # FV-9
                        print(T.T200+"\n")

                    elif Q45 == "a".lower() or "c".lower() and Q46 != "m".lower() and ask_Q49_preg == "b".lower():
                        # Q45 = YES or IDK and Q46 != m and 49_preg = No
                        # FV-11 
                        print(T.T200+"\n")
                else:
                    # Q49_pregnacy = YES
                    if Q45 == "b".lower() and Q46 !="m".lower() and ask_Q49_preg =="a".lower():
                        # Q45 = NO and Q46 != m and 49_preg = yes
                        # FV-9 mine
                        print(M.MSG301+'\n')
                        print(T.T200+"\n")
                        

                    elif Q45 == "a".lower() or "c".lower() and Q46 != "m".lower() and ask_Q49_preg == "a".lower():
                        # Q45 = YES or IDK and Q46 != m and 49_preg = yes
                        # FV-11 Minr
                        print(M.MSG301+"\n")
                        print(T.T200+"\n")
                        
            else:
                # (age) Q40 is > 80
                ask_Q49 = str(input(Q.Q49)).lower()
                if ask_Q49 == "a".lower():
                    if Q45 == "b".lower() and Q46 !="m".lower() and ask_Q49 =="a".lower():
                        # Q45 = NO and Q46 != m and 49_preg = YES
                        # FV-8
                        print(M.MSG301+'\n')
                        print(T.T200+"\n")
                    elif Q45 == "a".lower() or "c".lower() and Q46 !="m".lower() and ask_Q49 =="a".lower():
                        # Q45 = NO and Q46 != m and 49_preg = YES
                        # FV-8
                        print(M.MSG301+'\n')
                        print(T.T200+"\n")




                
