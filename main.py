objets = [2, 5, 4, 7, 1, 3, 8] 
taille_sacs = 10

def firstFit(objets, taille_sacs):

    sacs = [taille_sacs]

    for poids in objets:
        pas_de_place = True

        for i in range(len(sacs)):
            if sacs[i] >= poids:
                sacs[i] = sacs[i] - poids
                pas_de_place = False
                break

        if pas_de_place == True:
            sacs.append(taille_sacs - poids)
    
    return len(sacs)


def firstFitDecreasing(objets, taille_sacs):

    objets.sort(reverse=True)

    return firstFit(objets, taille_sacs)


def nextFit(objets, taille_sacs):
    # Minimum 1 sac
    nb_sacs = 1
    taille_restante = taille_sacs
    for poids in objets:
        if taille_restante >= poids:
            taille_restante -= poids
        else:
            nb_sacs += 1
            taille_restante = taille_sacs - poids
    
    return nb_sacs

def randomOrderRandomBin(objets, taille_sacs):
    return


print("FirstFit : ", firstFit(objets, taille_sacs))
print("FirstFit Dec : ", firstFitDecreasing(objets, taille_sacs))
print("NextFit : ", nextFit(objets, taille_sacs))