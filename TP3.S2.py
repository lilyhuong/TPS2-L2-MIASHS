def printDico(dico):
    for clef in dico:
        print(clef,dico[clef])

mondico = {"chene": 1, "boule": 2, "saule": 5}
print (printDico(mondico))        
def nb0ccurences(text):
    res = {}
    for x in text:
        res[x]= res.get(x,0) + 1
        return res
#Exercise 3

def age(d,prenom):
        if  prenom in d:
            return d[prenom][1]



mondico2={"lea": (2,45,176,70), "louis": (1,45,156,62)}
print("age de louis : ", age(mondico2,"louis"))



def mesdames(d):
    prenoms = ""
    for clef in d:
        if d[clef][0] == 2:
            prenoms += clef
            print(prenoms)
print(mesdames(mondico2))

def plus_taille(d,n):
    res = 0
    for clef in d:
        if d[clef][2] > 170:
            res += 1
        return res

def moyenne_taille (d):
    res = 0
    x = 0
    for clef in d:
        
        
