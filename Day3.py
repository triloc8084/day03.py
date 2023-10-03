num=int(input("k: "))
sum1=0
a=0
b=1
c=0
s=0
p=0
while(c<=num):
    print(c)
    a=b
    b=c
    if(p%2==0):
        s+=c
    p=p+1
    c=a+b

print("sum:",s)

n=int(input(" "))
y=(n**(1/3))
print("{0:.3f}".format(y))

n=int(input("enter: "))
tup=list()
for i in range(1,n+1):
    n=int(input("enterabc: "))
    n=n**3
    tuple=tup.append(n)
    print(tuple)

