
#11fibonacci
def fibonacci(num):
    a=0
    b=1
    fib_sequence=[]
    for i in range(num):
        fib_sequence.append(a)
        a,b=b,a+b
    return fib_sequence
num=int(input("enter a number upto which you need the series:"))         
fib_sequence=fibonacci(num)
print("the fibonacci series is :")
for j in fib_sequence:
    print(j)








          
