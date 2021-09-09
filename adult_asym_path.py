# From enter screen
import question as Q
import testmssg as T
import pediatric as P
import careMssg as M
import sys
import pediatric_asym_path 
import pediatric_sym_Nexp
import pediatric_sym_exp


def adultAsymPathwayE(Q38="e"):
    # Q38 = e
    ask_Q214 = str(input(Q.Q2)).lower()
    return ask_Q214

def adultASymPathway(Q25,Q38 ):
    Q214 = adultAsymPathwayE(Q38="e")
    ask_Q26 = str(input(Q.Q26)).lower()
    if ask_Q26 == "a".lower():
    # Q26 = Yes
        if Q25 == "b".lower() and ask_Q26 =="a".lower() and Q38 =="a".lower():
            # AA-6
            print(M.MSG202+"\n")
            print(T.T105+"\n")
        elif Q25 == "b".lower() and ask_Q26 =="a".lower() and Q38 =="b".lower():
            # AA-7
            print(M.MSG202+"\n")
            print(T.T105+"\n")
        elif Q25 == "b".lower() and ask_Q26 =="a".lower() and Q38 =="c".lower():
            # AA-8
            print(M.MSG202+"\n")
            print(T.T105+"\n")
        elif Q25 == "b".lower() and ask_Q26 =="a".lower() and Q38 =="d".lower():
            # AA-9
            print(M.MSG202+"\n")
            print(T.T105+"\n")
        elif Q25 == "b".lower() and ask_Q26 =="a".lower() and Q38 =="e".lower() and Q214 =="a".lower():
            # AA-10
            print(M.MSG202+"\n")
            print(T.T105+"\n")
        elif Q25 == "b".lower() and ask_Q26 =="a".lower() and Q38 =="e".lower() and Q214 =="b".lower():
            # AA-11
            print(M.MSG202+"\n")
            print(T.T105+"\n")
        elif Q25 == "a".lower() or "c".lower() and ask_Q26 =="a".lower() and Q38 =="a".lower():
            # AA-12
            print(M.MSG216+"\n")
            print(M.MSG202+"\n")
            print(M.MSG201+"\n")
            print(T.T105+"\n")
        elif Q25 == "a".lower() or "c".lower() and ask_Q26 =="a".lower() and Q38 =="b".lower():
            # AA-13
            print(M.MSG216+"\n")
            print(M.MSG202+"\n")
            print(T.T107+"\n")
            print(T.T105+"\n")
        elif Q25 == "a".lower() or "c".lower() and ask_Q26 =="a".lower() and Q38 =="c".lower():
            # AA-14
            print(M.MSG216+"\n")
            print(M.MSG202+"\n")
            print(T.T107+"\n")
            print(T.T105+"\n")
        elif Q25 == "a".lower() or "c".lower() and ask_Q26 =="a".lower() and Q38 =="d".lower():
            # AA-15
            print(M.MSG216+"\n")
            print(M.MSG202+"\n")
            print(T.T108+"\n")
            print(T.T105+"\n")
        elif Q25 == "a".lower() or "c".lower() and ask_Q26 =="a".lower() and Q38 =="c".lower() and Q214 == "a".lower():
            # AA-16
            print(M.MSG216+"\n")
            print(M.MSG202+"\n")
            print(T.T107+"\n")
            print(T.T101+"\n")
            print(T.T105+"\n")
        elif Q25 == "a".lower() or "c".lower() and ask_Q26 =="a".lower() and Q38 =="c".lower() and Q214 == "b".lower():
            # AA-17
            print(M.MSG216+"\n")
            print(M.MSG202+"\n")
            print(T.T107+"\n")
            print(T.T101+"\n")
            print(T.T105+"\n")
    else:
        # Q26 = NO
        ask_Q27 = str(input(Q.Q27)).lower()
        #Q27 = NO
        if ask_Q27 == "b".lower():
            if Q25 == "a".lower() or "c".lower() and Q38 == "a".lower():
                # AA - 18
                print(M.MSG201)
                print(T.T101)
                print(T.T105+"\n")
            elif Q25 == "a".lower() or "c".lower() and Q38 == "b".lower():
                # AA - 19
                print(M.MSG217)
                print(T.T105+"\n")
            elif Q25 == "a".lower() or "c".lower() and Q38 == "c".lower():
                # AA - 20
                print(M.MSG212)
                print(M.MSG215)
                print(M.MSG213)
                print(T.T107)
                print(T.T105+"\n")
            elif Q25 == "a".lower() or "c".lower() and Q38 == "d".lower():
                # AA - 21
                print(T.T108)
                print(M.MSG213)
                print(T.T105+"\n")
            elif Q25 == "a".lower() or "c".lower() and Q38 == "e".lower() and Q214 == "a".lower():
                # AA - 22
                print(M.MSG201)
                print(T.T101)
                print(T.T105+"\n")
            elif Q25 == "a".lower() or "c".lower() and Q38 == "e".lower() and Q214 == "b".lower():
                # AA - 23
                print(M.MSG213)
                print(T.T107)
                print(T.T101)
                print(T.T105+"\n")
            elif Q25 == "b".lower() and Q38 == "a".lower():
                # AA - 24
                print(M.MSG201)
                print(T.T105)
            elif Q25 == "b".lower() and Q38 == "b".lower():
                # AA - 25
                print(T.T109)
                print(T.T105)
            elif Q25 == "b".lower() and Q38 == "c".lower():
                # AA - 26
                print(M.MSG215)
                print(T.T105)
            elif Q25 == "b".lower() and Q38 == "d".lower():
                # AA - 27
                print(T.T105)
            elif Q25 == "b".lower() and Q38 == "e".lower() and Q214 =="a".lower():
                # AA - 28
                print(T.T109)
                print(T.T105)
            elif Q25 == "b".lower() and Q38 == "e".lower() and Q214=="b".lower():
                # AA - 29
                print(T.T109)
                print(T.T105)
        else:
            # Q27 = Yes
            ask_Q28 = str(input(Q.Q28)).lower()
            if Q25=="b".lower() and ask_Q28=="a".lower() and Q38 =="a".lower():
                # AA - 30
                print(M.MSG208)
                print(M.MSG201)
                print(T.T105)
            
            elif Q25=="b".lower() and ask_Q28=="a".lower() and Q38 =="b".lower():
                # AA - 31
                print(M.MSG208)
                print(M.MSG212)
                print(T.T105)
            elif Q25=="b".lower() and ask_Q28=="a".lower() and Q38 =="c".lower():
                # AA - 32
                print(M.MSG208)
                print(M.MSG212)
                print(T.T105)
            elif Q25=="b".lower() and ask_Q28=="a".lower() and Q38 =="d".lower():
                # AA - 33
                print(T.T109)

            elif Q25=="b".lower() and ask_Q28=="a".lower() and Q38 =="e".lower() and Q214=="a".lower():
                # AA - 34
                print(T.T109)
                print(T.T105)
            elif Q25=="b".lower() and ask_Q28=="a".lower() and Q38 =="e".lower() and Q214=="b".lower():
                # AA - 35
                print(T.T109)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="a".lower() and Q38 =="a".lower():
                # AA - 36
                print(M.MSG214)
                print(M.MSG201)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="a".lower() and Q38 =="b".lower():
                # AA - 37
                print(M.MSG214)
                print(M.MSG217)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="a".lower() and Q38 =="c".lower():
                # AA - 38
                print(M.MSG214)
                print(M.MSG215)
                print(M.MSG213)
                print(T.T107)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="a".lower() and Q38 =="d".lower():
                # AA - 39
                print(M.MSG214)
                print(T.T108)
                print(M.MSG213)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="a".lower() and Q38 =="a".lower() and Q214=="a".lower():
                # AA - 40
                print(M.MSG214)
                print(T.T101)
                print(T.T107)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="a".lower() and Q38 =="a".lower() and Q214=="b".lower():
                # AA - 41
                print(M.MSG214)
                print(M.MSG212)
                print(T.T101)
                print(T.T107)
                print(T.T105)

            elif Q25=="b".lower() and ask_Q28=="b".lower() and Q38 =="a".lower():
                # AA - 42
                print(M.MSG203) 
                print(T.T109)
                print(T.T105)
            elif Q25=="b".lower() and ask_Q28=="b".lower() and Q38 =="b".lower():
                # AA - 43
                print(M.MSG203) 
                print(M.MSG212)
                print(T.T105)
            elif Q25=="b".lower() and ask_Q28=="b".lower() and Q38 =="c".lower():
                # AA - 44
                print(M.MSG203)
                print(M.MSG215)
                print(M.MSG213)
                print(T.T105)
            elif Q25=="b".lower() and ask_Q28=="b".lower() and Q38 =="d".lower():
                # AA - 45 
                print(T.T109)
                print(M.MSG213)
            elif Q25=="b".lower() and ask_Q28=="b".lower() and Q38 =="e".lower() and Q214=="a".lower():
                # AA - 46
                print(M.MSG203) 
                print(T.T101)
                print(T.T105)
            elif Q25=="b".lower() and ask_Q28=="b".lower() and Q38 =="e".lower() and Q214=="b".lower():
                # AA - 47
                print(M.MSG203)
                print(M.MSG212) 
                print(T.T101)
                print(T.T105)

            elif Q25=="a".lower() or "c".lower() and ask_Q28=="b".lower() and Q38 =="a".lower():
                # AA - 48
                print(M.MSG214)
                print(M.MSG201)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="b".lower() and Q38 =="b".lower():
                # AA - 49
                print(M.MSG214)
                print(M.MSG217)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="b".lower() and Q38 =="c".lower():
                # AA - 50
                print(M.MSG214)
                print(M.MSG215)
                print(M.MSG213)
                print(T.T107)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="b".lower() and Q38 =="d".lower():
                # AA - 51
                print(M.MSG214)
                print(T.T108)
                print(M.MSG213)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="b".lower() and Q38 =="e".lower() and Q214 =="a".lower():
                # AA - 52
                print(M.MSG214)
                print(T.T101)
                print(T.T107)
                print(T.T105)
            elif Q25=="a".lower() or "c".lower() and ask_Q28=="b".lower() and Q38 =="a".lower() and Q214=="b".lower():
                # AA - 53
                print(M.MSG214)
                print(M.MSG201)
                print(T.T101)
                print(T.T107)
                print(T.T105)


            
            
                