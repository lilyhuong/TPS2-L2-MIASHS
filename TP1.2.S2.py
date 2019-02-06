#exercise3.1
from random import randint
def lancerDé(n):
    return [randint (1,6)]
print (lancerDé (1))

#exercise3.2
def lancersEnserie(n):
    res = []
    i = 0
    for i in  range (0,n):
        b = randint (1,6)
        res.append (b)
        res.count(1)
        res.count(2)
        res.count(3)
        res.count(4)
        res.count(5)
        res.count(6)
        i += 1
    return (res)
print (lancersEnserie(20))

#exercise3.3
def listesomme(l1,l2):
    output = []
    x = 0
    for i in l1:
        x = [i]
    for j in l2:
        x = [i] + [j]
        output += x
    return output
l11 = [1,5,6,7,8]
l22 = [2,5,6,8,7]
print (listesomme(l11,l22))

             
             
            
            
            

