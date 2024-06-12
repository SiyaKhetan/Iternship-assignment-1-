def min_max(l):
    if not l :
        return None,None
    return min(l),max(l)
l=[1,532,5,6,32,78,8]
min,max=min_max(l)
print(min)
print(max)