l=[1,2,3,4,5,6,7,8,9]
def sum(l):
    total=0
    for i in l:
        from math import pow
        total+=pow(i,2)
    total=int(total)
    print("sum of squiares of list :" +str(total))

sum(l)
