r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(c):
    s=0
    for j in range(r):
        s=s+m[j][i]
    print(s,end=' ')