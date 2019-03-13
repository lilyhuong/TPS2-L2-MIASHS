def recopier(exercise,nouvelle):
    fic1 = open (exercise, "r" )
    fic2 = write (nouvelle, "w")
    while (True):
        x = exercise.read (1)
        if x == "":
            break
            fic2.write (x)
    fic1.close ()
    fic2.close ()
    return

        
