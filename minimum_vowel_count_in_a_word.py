def fun(n):
    c=0
    for i in n:
        if i in 'aeiouAAEIOU':
            c=c+1
    return c
n=list(input().split())
l=[]
for i in n:
    l.append(fun(i))
print(min(l))