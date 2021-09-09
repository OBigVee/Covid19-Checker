# From All Branches

import userX as X
import sys

def UX():
    print("\n\n")
    ask_UX1 = str(input(X.UX1)).lower()
    if ask_UX1 == "a".lower():
        ask_UX2 = str(input(X.UX2)).lower()
        ask_UX3  = str(input(X.UX3)).lower()
    else:
        sys.exit()