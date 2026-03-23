def set2 () :
    d1 = {1 , 10 , 100}
    d2 = {2 , 20 , 100}
    d3 = d1.intersection(d2)
    d4 = d1.symmetric_difference(d2)
    d5 = len (d1 | d2)
    print("visitors IDs for two different days " ,d1,d2)
    print("visitors who visited both days : ",d3)
    print("visitors who visited only one of the days : ",d4)
    print("total unique visitors across both days : ",d5)

set2()
