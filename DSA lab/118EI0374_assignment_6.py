a = {'+':1,'-':1,'*':2,'/':2,'^':3}
b = a.keys()
A = []
def enterval(A):

    while(True):
        v = input()
        if len(v) <= 0:
            break
        A.append(v)
    return A
def check(A):
    if len(A) <= 2:
        return (0)
    for i in range(0,len(A)-1):
        if ((A[i] in b) and (A[i+1] in b)) or ( A.count('(') != A.count(')')):
            return (0)
        else:continue
    return (1)
def post(A):
    R = []

    a = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    B = []
    for i in range(len(A)):

        if A[i].isdigit():
            R.append(A[i])
        elif A[i] == "(":
            B.append(A[i])
        elif A[i] == ")":
           while  len(B) != 0 and B[-1] != "(" :
               R.append(B.pop())
           B.pop()


        else:
            if len(B) != 0:
                if B[-1] == "(":
                    B.append(A[i])
                elif (a[A[i]] <= a[B[-1]]) :

                    while len(B) != 0 and a[A[i]] <= a[B[-1]]  :
                        R.append(B.pop())
                    B.append(A[i])
                else:
                    B.append(A[i])
            else:
                B.append(A[i])
    while len(B) != 0:
        R.append(B.pop())
    return (R)

def evaluate(A):
    if len(A) == 0:
        return 0

    a = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    B = []
    for i in range(len(A)):
        if A[i].isdigit():
            B.append(A[i])
        else:
            a1 = int(B.pop())
            a2 = int(B.pop())
            if (A[i] == "-"):
                v = a2 - a1
            elif(A[i] == "*"):
                v = a2 * a1
            elif (A[i] == "/"):
                v = a2 / a1
            elif (A[i] == "+"):
                v = a2 + a1
            elif (A[i] == "^"):
                v = a2 ^ a1
            B.append(v)
    R = B.pop()
    return R



print("ENTER THE VALUE ONE BY ONE")
enterval(A)
print("PRINTINT THE INFIX EXPRESSION---->")
print(*A)
check = check(A)
if check == 0:
    print("ERROR THE EXPRESSION IS NOT CORRECT  :-( ")
    exit(0)
else:
    print("YOU ARE GOOD TO GO  :-) ")

K = post(A)
print(("PRINTING THE POSTFIX EXPRESSION---->"))
print(*K)
print("EVALUATIING POSTFIX EXPRESSION ------")
print(evaluate(K))