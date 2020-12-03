import random


"""
Dans cet algorithme, pour chaque élément :
    - on parcourt la liste des sacs non-vides jusqu'à trouver un sac
        capable de recevoir l'élément
    - si aucun sac ne convient, on place l'élément dans un nouveau sac vide
"""
def firstFit(objets):

    sacs = []

    for poids in objets:
        pas_de_place = True

        for i in range(len(sacs)):
            if sacs[i] >= poids:
                sacs[i] = round(sacs[i] - poids, 1)
                pas_de_place = False
                break

        if pas_de_place == True:
            sacs.append(round(1 - poids, 1))
    
    return len(sacs)

"""
Même chose mais en classant la liste d'éléments par ordre décroissant
"""
def firstFitDecreasing(objets):

    objets.sort(reverse=True)

    return firstFit(objets)


"""
Dans cet algorithme, pour chaque élément :
    - On vérifie si le sac actuel peut contenir l'élément
    - Sinon, on ajoute l'élément à un nouveau sac
"""
def nextFit(objets):
    # Minimum 1 sac
    nb_sacs = 1
    taille_restante = 1
    for poids in objets:
        if round(taille_restante, 1) >= poids:
            taille_restante -= round(poids, 1)
        else:
            nb_sacs += 1
            taille_restante = round(1 - poids, 1)
    
    return nb_sacs


"""
# TODO
"""
def randomOrderRandomBin(objets):
    return 0

def lectureLigne(ligne):
    # On sépare chaque élément par un ":"
    ligne = ligne.replace(" ", "")
    arg_list = ligne.split(":")
    objets = arg_list[1:]

    # Retourne les poids des éléments
    return [float(i) for i in objets]

def lectureFichier():

    filename = input("Entrez le nom du fichier à lire : ")
    with open(filename) as file:
        ligne = file.readline()
    
    objets = lectureLigne(ligne)

    affichageResultat(objets)

def lectureInstance():
    
    ligne = input("Entrez votre instance : ")
    objets = lectureLigne(ligne)

    affichageResultat(objets)

    return

def generationInstances():
    try:
        nb_instances = int(input("Entrez le nombre d'instances à générer : "))
        nb_elements = int(input("Entrez le nombre d'éléments dans chaque instance : "))
    except ValueError as e:
        print(e)
        print("Veuillez entrer un chiffre correct")
        return

    # Somme des ratios pour NF, FFD et RORB
    sum_nf = 0
    sum_ffd = 0
    sum_rorb = 0

    for instance in range(nb_instances):
        list_objets = []
        # Création de nb_elements éléments aléatoires dans chaque instance
        for element in range(nb_elements):
            element = round(random.random(), 2)
            list_objets.append(element)

        borne_inferieure = sum(list_objets)

        ### Lancement des algorithmes
        res_nf = nextFit(list_objets)
        ratio_nf = res_nf / borne_inferieure
        sum_nf += ratio_nf


        res_ffd = firstFitDecreasing(list_objets)
        ratio_ffd = res_ffd / borne_inferieure
        sum_ffd += ratio_ffd

        res_rorb = randomOrderRandomBin(list_objets)
        ratio_rorb = res_rorb / borne_inferieure
        sum_rorb += ratio_rorb

    # Affichage des moyennes par algorithme
    print("Ratio moyen NF : ", sum_nf / nb_instances)
    print("Ratio moyen FFD : ", sum_ffd / nb_instances)
    print("Ratio moyen RORB : ", sum_rorb / nb_instances)


def affichageResultat(objets):

    res_nf = nextFit(objets)
    res_ffd = firstFitDecreasing(objets)
    res_rorb = randomOrderRandomBin(objets)
    borne_inferieure = sum(objets)


    print("Borne inférieure : ", borne_inferieure)
    print()
    print("Résultat NF : ", res_nf)
    print("Ratio NF : ", res_nf/borne_inferieure)
    print()
    print("Résultat FFD : ", res_ffd)
    print("Ratio FFD : ", res_ffd/borne_inferieure)
    print()
    print("Résultat RORB : ", res_rorb)
    print("Ratio RORB : ", res_rorb/borne_inferieure)


def main():

    options = {
        '1': lectureFichier,
        '2': lectureInstance,
        '3': generationInstances
    }

    while True:
        print("-----Projet Bin Packing-----")
        print("Choisissez votre mode d'entrée : ")
        print("1 - Entrer un fichier")
        print("2 - Entrer une instance")
        print("3 - Génération aléatoire d'instance(s)")
        choice = input("Votre choix : ")

        options[choice]()    

if __name__ == "__main__":
    main()