def func1(str) :
    d = {'u' : 0 , 'l' : 0 }
    for x in str :
       if x.isupper() == True:
           d ['u'] += 1
       elif x.islower() == True:
           d['l'] += 1
    return d
        
st = "PDeu-SoT"
a = func1(st)
print(st,a)
        
    
