string=input("enter a string to check the frequency of each char")

for i in string:
    for j in string:
        
        count=0
        if i==j:
            count+=1
        print(count)   
   