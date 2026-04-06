def palindrome_checker():
    lst = [ 'madam' , 'Python' , 'malayalam' , 12321]
    newlst = list(filter(lambda x: str(x)==(str(x)[ : :-1]) , lst))
    print (lst,newlst,sep='\n')

palindrome_checker()
