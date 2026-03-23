def set1() :
    A = {'Math','Physics','Chemistry'}
    B = {'Physics','Biology','Math'}
    comsub = A.intersection(B)
    of = A.difference(B)
    os = B.difference(A)
    us = of.union(os)
    print("common subjects are : ", comsub)
    print("subject taken by only first student :" , of)
    print("subject taken by only second student" , os)
    print("total unique subjects are : " , len(us))
    
set1()
    
