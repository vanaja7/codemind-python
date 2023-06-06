r,c=map(int,input().split())
e,o=0,0
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(len(m)):
    for i in m[i]:
        if i%2==0:
            e=e+i
        else:
            o=o+i
print(e,o)