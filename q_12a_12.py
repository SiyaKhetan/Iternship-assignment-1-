a=int(input("enter a number: "))
count=0
while(a>0):
    lastdigit=a%10
    count+=lastdigit
    a//=10
print(count)   
