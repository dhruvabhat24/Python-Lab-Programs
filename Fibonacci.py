def F(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return F(n-1)+F(n-2)
n=int(input("Enter a value for n (where n>0) :"))
if n<=0:
    print("Error: n must be greater than 0")
else:
    result=F(n)
    print("The",n,"th Fibbonacci number is :",result)
    
