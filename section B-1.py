m,n=input().split()
m,n=int(m),int(n)
k=input()
L=[]
for i in range(m):
    l=input().split()
    L.append(l)
print(L)
c=0
for i in range(m):
    for j in range(n):
        if k==L[i][j]:
            print("True")
            print(i,j)
            c=1
            break
if c==0:
    print("False")
