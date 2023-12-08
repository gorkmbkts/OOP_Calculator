import div
import diff
import mul

from add import adding
from diff import diffing
from div import diving
from mul import mulling
from complex import complexcalc

res=0

op=int(input("---Welcome to best calculator---\nplease enter the operation that you wish\n1 for addition\n2 for subtraction\n"
             "3 for multiplication\n4 for division\n5 for line expression\n\n-> "))

if op==5:
    strcalc=input("please enter the expression\n\n->")
    res=complexcalc(strcalc).calc()


else:

    var1=int(input("\nplease enter the first number required for the calculation\n\n-> "))
    var2=int(input("\nplease enter the second number required for the calculation\n\n-> "))



    if op==1:

        res=adding(var1,var2).adder()
    elif op==2:

        res=diffing(var1,var2).differ()

    elif op==3:

        res=mulling(var1,var2).muller()


    elif op==4:

        if var1 == 0:
            print("unfortunately this calculator could not do this operation with current math")
        else:
            res=diving(var1,var2).diver()









print(res)






