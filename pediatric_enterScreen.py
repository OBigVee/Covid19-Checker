# From enter screen
import question as Q
import testmssg as T
import pediatric as P
import careMssg as M
import sys
import pediatric_asym_path 
import pediatric_sym_Nexp
import pediatric_sym_exp

def pediatricAge(Q2, Q4):
    if Q2 == "a".lower():
        # age < 2
        # PS-1
        print(M.MSG20+"\n")
        print("############ 1st #################")
        sys.exit()

    elif Q2 == "b".lower() or "c".lower() and Q4 == "a".lower():
        # age range 2 - 9  and assesment = self
        # PS -2 
        print("############ 2nd #################")
        print(M.MSG20+"\n")
        sys.exit()
    elif Q2 == 'd'.lower() and Q4 == "a".lower():
        # age 10 and assesment = self
        # PS -3
        return( print(M.MSG21+"\n") )
    else:
        print("####################################################")
        # age range 13 above and assesment = self
        # PS-4
        return(print(M.MSG22))


def pediatricMain(pediatricAge):
    #if pediatricAge ==
    ask_Q5_PED = str(input(P.Q5_PED)).lower()
    ask_Q35_PED = str(input(P.Q35_PED)).lower()
    ask_Q36_PED = str(input(P.Q36_PED)).lower()
    ask_Q37_PED = str(input(P.Q37_PED)).lower()
    ask_Q1_PED = str(input(P.Q1_PED)).lower()
    if ask_Q1_PED == "a".lower():
        # user have any of the disease
        # PS-7
        print(M.MSG4+"\n")
    else:
        ask_Q3_PED = str(input(P.Q3_PED)).lower()
        if ask_Q3_PED == "b":
            # user is not sick
            return pediatric_asym_path.pediatricAsymPathway(ask_Q3_PED)
        else:
            # user is sick
            ask_Q6_PED = str(input(P.Q6_PED)).lower()
            if ask_Q6_PED == "b".lower():
               return pediatric_sym_Nexp.pediatricSymNonExposed()
            elif ask_Q6_PED == "a".lower() or "c".lower():
                return pediatric_sym_exp.pediatricSymExposed()