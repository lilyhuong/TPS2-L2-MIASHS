#exercise3.1
from random import randint
def lancerDé(n):
    return [randint (1,6)]
print (lancerDé (1))
#Exercise 3.2
from random import randint
def lancersEnserie(n):
    res = []
    res2 = [0,0,0,0,0,0]
    i = 0
    for i in  range (0,n):
        #index = randint(1,6) - 1
        #res2[index] += 1
        res.append(randint(1,6))

    for i in range(0,6):
        res2[i] = res.count(i+1)
        
    return (res2)
print (lancersEnserie(1000000))


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
#Exercise4.1
def puissnant2(x):
    return x*x
def fonction2liste(carre,liste):
    return [carre(x) for x in liste]
list2 = [3,5,9]
print(fonction2liste(puissnant2,list2))

             
             
            
            
            

