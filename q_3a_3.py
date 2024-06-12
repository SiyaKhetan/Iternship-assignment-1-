def calculatefac(num):
    if num==0 or num==1:
        return 1 
       
    return num*calculatefac(num-1) 
num=int(input("enter a number: "))
print("the factorial of ", num,'is ',calculatefac(num))