N=int(input("enter nomber:"))
while N<=0:
    N=int(input("enter nomber:"))
print("the number divisors of",N,"are:")
for i in range(1,N+1):
    if(N%i==0):
        print(i)