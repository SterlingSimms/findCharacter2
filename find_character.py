def find_character(aList, a):
    newList = []
    for x in aList:
        for y in x:
            if y == a:
                newList.append(x)
    print newList          
find_character(['hello','world','my','name','is','Anna'], "o")