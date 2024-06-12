string=input("enter a string ")
prefix=input("enter the prefix you wanted to check")
if string[0] or string[-1]==prefix:
    print("yes it starts or ends with ",prefix)
else:
    print("no it does not takes the starting and ending position")    