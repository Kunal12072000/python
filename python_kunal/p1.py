
a = list(map(int,input().rstrip().split()))
c = [0 for i in range(101)]
for i in a:
    c[i] += 1
ans = 0
for i in range(0,100):
    ans = max(ans,c[i] + c[i+1])
print(ans)