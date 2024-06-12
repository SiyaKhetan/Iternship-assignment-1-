str1=input("enter 1 string")
str2=input("enter 2 string")
n1=len(str1)
n2=len(str2)
if(n1!=n2):
    print("these cannot be anagrams of each other")
if sorted(str1)==sorted(str2):
    print("these are anagrams ")