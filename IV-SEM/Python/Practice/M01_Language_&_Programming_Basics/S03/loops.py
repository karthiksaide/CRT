n=int(input())
for i in range(1,n+1):
    print(i, end =" ")

n=int(input())
i=1
while i<=n:
    print(i)
    i+=1


n=input()
k=len(n)
x=n[-1:-(k-1):1]
print(x)