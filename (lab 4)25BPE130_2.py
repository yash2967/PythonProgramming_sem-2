import random
def list2():
    list1 = [random.randrange(1,99) for x in range(20)]
    print(list1)
    n = int(input("Enter a Number:"))
    if n in list1:
        print(f"Number {n} found at index position")
        for i,v in enumerate(list1):
            if v == n:
                print(i)
    else:
                print("Not found", n)

list2()
