# From Pediatric - Enter Screening


import question as Q
import testmssg as T
import pediatric as P
import careMssg as M


def adultSym10D(Q6,Q31="e"):
    ask_Q201 = str(input(Q.Q201)).lower()
    if ask_Q201 == "a".lower():
        # Q201 = YES
        ask_Q202 = str(input(Q.Q202)).lower()
        ask_Q203 = str(input(Q.Q203)).lower()
        if Q6=="b" and ask_Q202 != None and ask_Q203 == "r":
            # AS-113
            print(T.T100)
            print(T.T105)
        elif Q6=="a" or "c" and ask_Q202 != None and ask_Q203 == "r":
            # AS-114
            print(T.T107)
            print(M.MSG212)
            print(T.T105)
        ask_Q204 = str(input(Q.Q204)).lower()
        ask_Q205 = str(input(Q.Q205)).lower()
        if ask_Q205 == "a":
            # Q205 = YES
            if Q6=="b" and ask_Q205=="a" and  ask_Q202=="a" and ask_Q204=="a":
                # AS-115
                print(M.MSG202)
                print(T.T102)
            elif Q6=="b" and ask_Q205=="a" and  ask_Q202!="a" and ask_Q204=="a":
                # AS-116
                print(M.MSG202)
                print(T.T102)
            elif Q6=="b" and ask_Q205=="a" and  ask_Q202=="a" or "b" and ask_Q204=="b":
                # AS-117
                print(M.MSG205)
                print(M.MSG210)
                print(T.T103)
            elif Q6=="b" and ask_Q205=="a" and  ask_Q202!="a" and ask_Q204=="b":
                # AS-118
                print(M.MSG205)
                print(M.MSG211)
                print(T.T103)
            elif Q6=="b" and ask_Q205=="a" and  ask_Q202=="a" or "b" and ask_Q204=="c":
                # AS-119
                print(M.MSG209)
                print(M.MSG211)
                print(T.T103)
            elif Q6=="b" and ask_Q205=="a" and  ask_Q202!="a"  and ask_Q204=="c":
                # AS-120
                print(M.MSG209)
                print(M.MSG211)
                print(T.T103)
            elif Q6=="a" or "c" and ask_Q205=="a" and  ask_Q202=="a" or "b" and ask_Q204=="a":
                # AS-121
                print(M.MSG216)
                print(T.T101)
                print(T.T102)
            elif Q6=="a" or "c" and ask_Q205=="a" and  ask_Q202!="a" and ask_Q204=="a":
                # AS-122
                print(M.MSG216)
                print(T.T107)
                print(T.T101)
                print(T.T102)
            elif Q6=="a" or "c" and ask_Q205=="a" and  ask_Q202=="a" or "b" and ask_Q204=="b":
                # AS-123
                print(M.MSG205)
                print(M.MSG210)
                print(T.T103)
            elif Q6=="a" or "c" and ask_Q205=="a" and  ask_Q202!="a" and ask_Q204=="b":
                # AS-124
                print(M.MSG205)
                print(M.MSG211)
                print(T.T107)
                print(T.T103)
            elif Q6=="a" or "c" and ask_Q205=="a" and  ask_Q202=="a" or "b" and ask_Q204=="c":
                # AS-125
                print(M.MSG209)
                print(M.MSG211)
                print(T.T103)
            elif Q6=="a" or "c" and ask_Q205=="a" and  ask_Q202!="a" and ask_Q204=="c":
                # AS-126
                print(M.MSG209)
                print(M.MSG211)
                print(T.T107)
                print(T.T103)
        else:
            # Q205 = NO
            ask_Q206 = str(input(Q.Q206)).lower()
            if ask_Q206 == "a":
                if Q6=="b" and ask_Q206=="a" and  ask_Q202=="a" or "b" and ask_Q204=="a":
                    # AS-127
                    print(M.MSG203)
                    print(T.T102)
                elif Q6=="b" and ask_Q206=="a" and  ask_Q202!="a" and ask_Q204=="a":
                    # AS-128
                    print(M.MSG203)
                    print(T.T102)
                elif Q6=="b" and ask_Q206=="a" and  ask_Q202=="a" or "b" and ask_Q204=="b":
                    # AS-129
                    print(M.MSG206)
                    print(M.MSG210)
                    print(T.T103)
                elif Q6=="b" and ask_Q206=="a" and  ask_Q202!="a" and ask_Q204=="b":
                    # AS-130
                    print(M.MSG206)
                    print(M.MSG211)
                    print(T.T103)
                elif Q6=="b" and ask_Q206=="a" and  ask_Q202=="a" or "b" and ask_Q204=="c":
                    # AS-131
                    print(M.MSG206)
                    print(M.MSG211)
                    print(T.T103)
                elif Q6=="b" and ask_Q206=="a" and  ask_Q202!="a" and ask_Q204=="c":
                    # AS-132
                    print(M.MSG206)
                    print(M.MSG211)
                    print(T.T103)
                elif Q6=="a" or "b" and ask_Q206=="a" and  ask_Q202=="a" or "b" and ask_Q204=="a":
                    # AS-133
                    print(M.MSG214)
                    print(T.T101)
                    print(T.T102)
                elif Q6=="a" or "b" and ask_Q206=="a" and  ask_Q202!="a"  and ask_Q204=="a":
                    # AS-134
                    print(M.MSG214)
                    print(T.T107)
                    print(T.T101)
                    print(T.T102)
                elif Q6=="a" or "b" and ask_Q206=="a" and  ask_Q202=="a" or "b" and ask_Q204=="b":
                    # AS-135
                    print(M.MSG214)
                    print(M.MSG210)
                    print(T.T103)
                elif Q6=="a" or "b" and ask_Q206=="a" and  ask_Q202!="a" and ask_Q204=="b":
                    # AS-136
                    print(M.MSG214)
                    print(M.MSF211)
                    print(T.T107)
                    print(T.T103)
                elif Q6=="a" or "b" and ask_Q206=="a" and  ask_Q202=="a" or "b" and ask_Q204=="c":
                    # AS-137
                    print(M.MSG214)
                    print(M.MSG211)
                    print(T.T103)
                elif Q6=="a" or "b" and ask_Q206=="a" and  ask_Q202!="a" and ask_Q204=="d":
                    # AS-138
                    print(M.MSG214)
                    print(M.MSG211)
                    print(T.T107)
                    print(T.T103)
            else:
                if Q6 == "b" and ask_Q206 =="b" and ask_Q202 =="a" or "b" and ask_Q204 == "a":
                    # AS-139
                    print(T.T109)
                    print(T.T102)
                elif Q6 == "b" and ask_Q206 =="b" and ask_Q202 !="a" and ask_Q204 == "a":
                    # AS-140
                    return(
                        print(T.T109),
                        print(T.T102)
                    )
                    
                elif Q6 == "b" and ask_Q206 =="b" and ask_Q202 =="a" or "b" and ask_Q204 == "b":
                    # AS-141
                    return (
                    print(M.MSG210),
                    print(T.T103)
                    )

                elif Q6 == "b" and ask_Q206 =="b" and ask_Q202 !="a" and ask_Q204 == "b":
                    # AS-142
                    return (
                        print(M.MSG211),
                        print(T.T103)
                    )
                    
                elif Q6 == "b" and ask_Q206 =="b" and ask_Q202 =="a" or "b" and ask_Q204 == "c":
                    # AS-143
                    return(
                        print(M.MSG208),
                        print(M.MSG211),
                        print(T.T103)
                    )
                    
                elif Q6 == "b" and ask_Q206 =="b" and ask_Q202 !="a" and ask_Q204 == "c":
                    # AS-144
                    return (
                        print(M.MSG208),
                        print(M.MSG211),
                        print(T.T103),
                    )
                    
                elif Q6!="b" and ask_Q206=="b" and ask_Q202=="a" or "b" and ask_Q204=="a":
                    # AS-145
                    return(
                        print(T.T101),
                        print(T.T102)
                    )
                    
                elif Q6!="b" and ask_Q206=="b" and ask_Q202!="a" and ask_Q204=="a":
                    # AS-146
                    return(
                        print(T.T107),
                        print(T.T101),
                        print(T.T102)
                    )
                    
                elif Q6!="b" and ask_Q206=="b" and ask_Q202=="a" or "b" and ask_Q204=="b":
                    # AS-147
                    return(
                        print(M.MSG210),
                        print(T.T103)
                    )

                elif Q6!="b" and ask_Q206=="b" and ask_Q202!="a" and ask_Q204=="b":
                    # AS-148
                    return(
                        print(M.MSG211),
                        print(T.T107),
                        print(T.T103),
                    )
                elif Q6!="b" and ask_Q206=="b" and ask_Q202=="a" or "b" and ask_Q204=="c":
                    # AS-149
                    return(
                        print(M.MSG210),
                        print(T.T103)
                     )
                    
                elif Q6!="b" and ask_Q206=="b" and ask_Q202!="a" and ask_Q204=="c":
                    # AS-150
                    return(
                        print(M.MSG208),
                        print(M.MSG211),
                        print(T.T107),
                        print(T.T103),
                    )
        
    else:
        ask_Q208 = str(input(Q.Q208)).lower()
        ask_Q209 = str(input(Q.Q209)).lower()
        if ask_Q209 == "r":
            # AS - 151
            print(T.T101)
            print(T.T015)
        else:
            ask_Q210 = str(input(Q.Q210)).lower()
            ask_Q211 = str(input(Q.Q211)).lower()
            if ask_Q211 == "a":
                # Q211 = YES
                if Q6 == "b" and ask_Q208=="a" or "b" and ask_Q210=="a":
                    # AS-152
                    print(M.MSG202)
                    print(T.T105)
                elif Q6 == "b" and ask_Q208!="a"  and ask_Q210=="a":
                    # AS-153
                    print(M.MSG202)
                    print(T.T105)
                elif Q6 == "b" and ask_Q208=="a" or "b" and ask_Q210=="b":
                    # AS-154
                    print(M.MSG205)
                    print(M.MSG210)
                    print(T.T105)
                elif Q6 == "b" and ask_Q208!="a"  and ask_Q210=="b":
                    # AS-155
                    print(M.MSG205)
                    print(M.MSG211)
                    print(T.T105)
                elif Q6 == "b" and ask_Q208=="a" or "b"  and ask_Q210=="c":
                    # AS-156
                    print(M.MSG209)
                    print(M.MSG211)
                    print(T.T103)
                elif Q6 == "b" and ask_Q208!="a"  and ask_Q210=="c":
                    # AS-157
                    print(M.MSG209)
                    print(M.MSG211)
                    print(T.T103)
                elif Q6 != "b" and ask_Q208=="a" or "b"  and ask_Q210=="a":
                    # AS-158
                    print(M.MSG216)
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6 != "b" and ask_Q208 !="a"  and ask_Q210=="a":
                    # AS-159
                    print(M.MSG216)
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6 != "b" and ask_Q208=="a" or "b"  and ask_Q210=="b":
                    # AS-160
                    print(M.MSG216)
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6 != "b" and ask_Q208!="a" and ask_Q210=="b":
                    # AS-161
                    print(M.MSG216)
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)

                elif Q6 != "b" and ask_Q208=="a" or "b"  and ask_Q210=="c":
                    # AS-162
                    print(M.MSG209)
                    print(T.T107)
                    print(T.T103)
                elif Q6 != "b" and ask_Q208!="a" and ask_Q210=="c":
                    # AS-163
                    print(M.MSG209)
                    print(T.T107)
                    print(T.T103)
            
            else:
                ask_Q212 = str(input(Q.Q212)).lower()
                if Q6=="b" and ask_Q212=="a" and ask_Q208=="a" or "b" and ask_Q210=="a":
                    # AS-164
                    print(M.MSG203)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="a" and ask_Q208!="a" and ask_Q210=="a":
                    # AS-165
                    print(M.MSG203)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="a" and ask_Q208=="a" or "b" and ask_Q210=="b":
                    # AS-166
                    print(M.MSG206)
                    print(M.MSG210)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="a" and ask_Q208!="a"  and ask_Q210=="b":
                    # AS-167
                    print(M.MSG206)
                    print(M.MSG211)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="a" and ask_Q208=="a" or "b" and ask_Q210=="c":
                    # AS-168
                    print(M.MSG206)
                    print(M.MSG211)
                    print(T.T103)
                elif Q6=="b" and ask_Q212=="a" and ask_Q208!="a" and ask_Q210=="c":
                    # AS-169
                    print(M.MSG206)
                    print(M.MSG211)
                    print(T.T103)
                elif Q6!="b" and ask_Q212=="a" and ask_Q208=="a" or "b" and ask_Q210=="a":
                    # AS-170
                    print(M.MSG203)
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="a" and ask_Q208!="a" and ask_Q210=="a":
                    # AS-171
                    print(M.MSG203)
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="a" and ask_Q208=="a" or "b" and ask_Q210=="b":
                    # AS-172
                    print(M.MSG206)
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="a" and ask_Q208!="a" and ask_Q210=="b":
                    # AS-173
                    print(M.MSG206)
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="a" and ask_Q208=="a" or "b" and ask_Q210=="c":
                    # AS-174
                    print(M.MSG206)
                    print(T.T107)
                    print(T.T103)
                elif Q6!="b" and ask_Q212=="a" and ask_Q208!="a" and ask_Q210=="c":
                    # AS-175
                    print(M.MSG206)
                    print(T.T107)
                    print(T.T103)
                elif Q6=="b" and ask_Q212=="b" and ask_Q208=="a" or "b" and ask_Q210=="a":
                    # AS-176
                    print(T.T109)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="b" and ask_Q208!="a"and ask_Q210=="a":
                    # AS-177
                    print(T.T109)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="b" and ask_Q208=="a" or "b" and ask_Q210=="b":
                    # AS-178
                    print(M.MSG210)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="b" and ask_Q208!="a" and ask_Q210=="b":
                    # AS-179
                    print(M.MSG210)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="b" and ask_Q208=="a" or "b" and ask_Q210=="c":
                    # AS-180
                    print(M.MSG208)
                    print(T.T105)
                elif Q6=="b" and ask_Q212=="b" and ask_Q208!="a" and ask_Q210=="a":
                    # AS-181
                    print(M.MSG208)
                    print(T.T103)
                elif Q6!="b" and ask_Q212=="b" and ask_Q208=="a" or "b" and ask_Q210=="a":
                    # AS-182
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="b" and ask_Q208!="a" and ask_Q210=="a":
                    # AS-183
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="b" and ask_Q208=="a" or "b" and ask_Q210=="b":
                    # AS-184
                    print(T.T107)
                    print(T.T104)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="b" and ask_Q208!="a" and ask_Q210=="b":
                    # AS-185
                    print(T.T107)
                    print(T.T109)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="b" and ask_Q208=="a" or "b" and ask_Q210=="c":
                    # AS-186
                    print(M.MSG208)
                    print(T.T109)
                    print(T.T105)
                elif Q6!="b" and ask_Q212=="b" and ask_Q208!="a" and ask_Q210=="c":
                    # AS-187
                    print(M.MSG208)
                    print(T.T109)
                    print(T.T105)
                    