import random
def list3():
    list3 = [random.randrange(1,30) for x in range(50)]
    print(list3)
    newlist = []
    for v in list:
        if v not in newlist:
            newlist.append(v)
    print(newlist)

list3()
