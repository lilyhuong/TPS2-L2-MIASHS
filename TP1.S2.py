def copierListeMoinsElt(e,lis):
    output = []
    for x in lis:
        if x != e:
            output += [x]
    return output
    
list1 = [1,2,6,7,8,9,8,8,8]
print(copierListeMoinsElt(8,list1))
def fairelisteMoinsElt(e,lis):
    
    for x in lis:
        if x == e:
            del lis [x]
            x += 1
    return lis
    
list4 = [1,2,3,5,4,5,6,7,8,8]
print(fairelisteMoinsElt(8,list4))
def remove(e,lis):
    for i in lis:
        if i == e:
            lis.remove(e);
            i += 1
    return lis

list4 = [1,2,3,5,4,5,6,7,8,8]
print(remove(8,list4))
from random import randint
def creerliste(n):
    output = []
    i = 0
    while i < n:
        b = randint(1,1000)
        i += 1
        output += [b]
    return output
print(creerliste(3))

def creer(b):
    out = []
    i = 0
    while i < b:
        h = randint(0,1000)
        i += 1
        out.append (h)
    return out
print(creer(6))
def creer1(n):
    return [randint(1,1000) for i in range(0,n)]
print(creer1(4))
