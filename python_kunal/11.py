def sum(a,v,k):
    if a[v] > 0:

        for i in range(1,k+1):
            a[v] += a[v + i]
        return a[v]
    else:
        for i in range(1,k+1):
            a[v] += a[v - i]
        return a[v]
def sum2(a,v,k):
    if a[v] < 0:

        for i in range(1,k+1):
            a[v] += a[v + i]
        return a[v]
    else:
        for i in range(1,k+1):
            a[v] += a[v - i]
        return a[v]

a = input("enter the array")
k = int(input())
if k > 0:
    for i in range(len(a)):
        a[i] = sum(a,i,k)
if k < 0:
    for i in range(len(a)):
        a[i] = sum2(a,i,k)



