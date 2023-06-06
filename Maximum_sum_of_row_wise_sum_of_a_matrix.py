r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    a=sum(l)
    m.append(a)
print(max(m))