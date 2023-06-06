r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
maxsum=0
for i in range(c):
    sum=0
    for j in range(r):
        sum+=mat[j][i]
    if sum>maxsum:
        maxsum=sum
print(maxsum)
        
        
    