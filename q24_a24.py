num1=float(input("enter a number 1:"))
num2=float(input("enter a number 2:"))
operator=input("enter the operator '+','-','*','/' ")
if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)  
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
else:
    print("please enter a valid operator from that 4 ")        
    
