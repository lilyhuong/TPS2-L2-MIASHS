def calculate (texte):
    cpt = 0
    fic = open ("texte.txt", "r")
    for x in texte:
        if x == "":
            cpt += 1
    fic.close ()
    return cpt
def  ajouter_des_lignes(texte):
    fic = open ("texte.txt","a")
    fic. write ("bonjour")
    fic.close ()
    return
def affiche_le_contenu (texte):
    fic = open ("text.txt", "w+" )
    fic.close ()
    return
def les_propriétés (texte):
    nbdelignes = 0
    nbdemots = 0
    nbdecarartère = 0
    fic = open ("texte.txt", "r")
    for l in texte:
        if l == "":
            nbdecaractère += 1
        x = l.plit ()
        if x == "":
            nbdemots += 1
    nbdelignes = sum(1 for line in open("texte.txt", "r+"))
    fic.close ()
    
         
                
