import os
import sys

import careMssg as M
import color
import pediatric as P
import question as Q
import testmssg as T
import userX as UX


import adult_asym_path
import adult_sym_10D_test
import adult_sym_exp
import adult_sym_Nexp


import fully_vacinated


import pediatric_enterScreen

import user_Ex 




disclaimer = T.disclaimer

introMessage = """Hi, I’m Julie. \nI’m going to ask you some questions. I will use your answers to give you advice about
the level of medical care you should seek.\n \nIf answering for someone else, please respond to to all questions as if you are them.\n
If you are experiencing a life-threatening emergency, please call 911 immediately.\n
If you are not experiencing a life-threatening emergency, let’s get started.\n\n"""


endMessage = "Steps to follow Everday:\n \
    • Get a COVID-19 Vaccine as soon as you can when eligble. Individuals 12 years old and over are\n \
        currently eligible. Continue to follow the steps below every day until you are fully vaccinated.\n\
    •Wear a mask over your nose and mouth.*\n\
    •Stay at least 6 feet away from people who don’t live with you.*\n\
    •Avoid crowded areas and poorly ventilated spaces.*\n\
    •Wash your hands often with soap and water, or use hand sanitizer with at least 60\% alcohol.  "

print(introMessage)
enterMsg = str(input(disclaimer)).lower()
if enterMsg == "a":
    # user agree
    ask_Q0 = str(input(Q.Q0)).lower()
    # Q0 = yes
    # user is in nigeria
    ask_Q0A = str(input(Q.Q0A))
    ask_Q34 = str(input(Q.Q34))
    ask_Q4 = str(input(Q.Q4))
    ask_Q39 = str(input(Q.Q39)).lower()
    if ask_Q39 == "a":
        # Q39 == Yes
        # GOTO FULLY VACCINATED
        fully_vacinated.fullyVacinated(ask_Q39)
    else:
        # user is not fully vaccinated
        ask_Q2 = str(input(Q.Q2)).lower()
        if ask_Q2 =="a" or "b" or "c" or "d" or "e": 
            # if Q2 <18 Goto Pediatric enter screen
            ped = pediatric_enterScreen.pediatricAge(ask_Q2, ask_Q4)
            pediatric_enterScreen.pediatricMain(ped)
        else:
            # user age >= 18
            ask_Q5  = str(input(Q.Q5)).lower()
            ask_Q35 = str(input(Q.Q35)).lower()
            ask_Q36 = str(input(Q.Q36)).lower()
            ask_Q37 = str(input(Q.Q37)).lower()
            ask_Q1  = str(input(Q.Q1)).lower()
            if ask_Q1 =="a":
                # Q1 = Yes
                # ES-5
                print(M.MSG4)
            else:
                ask_Q3 = str(input(Q.Q3)).lower()
                if ask_Q3 =="a":
                    # Q3 = yes
                    ask_Q6  = str(input(Q.Q6)).lower()
                    ask_Q31 = str(input(Q.Q31)).lower()
                    if ask_Q6 != "b" and  ask_Q31 !="e":
                        # Q6 = Yes or I don't know and Q31 = e
                        # Go to Adult Symptomatic Exposed
                        adult_sym_exp.adultSympExposed(ask_Q6,ask_Q31)
                    elif ask_Q6 == "b" and  ask_Q31 !="e":
                        # Go to Adult Symptomatic NON-Exposed
                        adult_sym_Nexp.adultSymNonExposed(ask_Q6,ask_Q31)
                    elif ask_Q6 != None and ask_Q31=="e":
                        adult_sym_10D_test.adultSym10D(ask_Q6,ask_Q31)
                else:
                    # Q3 = No
                    # adult asym pathway
                    ask_Q25 = str(input(Q.Q25)).lower()
                    ask_Q38 = str(input(Q.Q38)).lower()
                    #adultETest = adult_asym_path.adultAsymPathwayE(ask_Q38)
                    #adult_asym_path.adultASymPathway(ask_Q25,ask_Q38)
                    adultETest = adult_asym_path.adultAsymPathwayE(ask_Q38) if ask_Q38=="e" else adult_asym_path.adultASymPathway(ask_Q25,ask_Q38) 

# user don't agree to discliamer
else:
    # ES-1
    print(M.MSG12)

# END MESSAGE 
print(endMessage)

# EXPERIENCE MESSAGE
user_experince_message = user_Ex.UX()
print(user_experince_message)
