import random
def set3() :
    lst = [random.randint(-5,5) for x in range (15)]
    print(lst)
    uniquelst = list(set(lst))
    print(uniquelst)

set3()
