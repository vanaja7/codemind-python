n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in l:
    if i<a or i>b:
        k.append(i)
print(sum(k))
    