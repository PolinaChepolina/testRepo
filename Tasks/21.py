 n = int(input())
sumn = (n*(n+1))//2
for i in range (1,n-1):
    tmp=int(input()) 
    sumn= sumn- tmp
print(sumn)
   
