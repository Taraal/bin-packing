import time
import random
from main import nextFit, firstFitDecreasing, randomOrderRandomBin, lectureLigne

#### Procédure des tests
# Comparaison par instance et par algorithme
# Lancement de 10 instances de chaque type dans chaque algorithme
# On calcule la moyenne du temps d'exécution des 10 instances
###


#### FICHIER #### 

"""
Pour une instance lue dans un fichier, un fichier de test "input.txt"
est lu dans le dossier courant
"""
def lireFichier():
    with open("input.txt") as file:
        ligne = file.readline()
    
    return lectureLigne(ligne)
    
def testFichierNF():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = lireFichier()
        nextFit(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5) * 1000
    print(f"Résultat Fichier + NF : {moyenne} millisecondes")

def testFichierFFD():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = lireFichier()
        firstFitDecreasing(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5)  * 1000
    print(f"Résultat Fichier + FFD : {moyenne} millisecondes")

def testFichierRORB():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = lireFichier()
        randomOrderRandomBin(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5)  * 1000
    print(f"Résultat Fichier + RORB : {moyenne} millisecondes")


##### CLAVIER ####

"""
Pour une instance lue au clavier, on stocke l'instance dans un string
"""
def lireLigne():
    ligne = "10:0.3:0.2:0.5:0.8:0.1:0.4:0.7:0.6:0.2:0.9"

    return lectureLigne(ligne)

def testClavierNF():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = lireLigne()
        nextFit(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5) * 1000
    print(f"Résultat Clavier + NF : {moyenne} millisecondes")

def testClavierFFD():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = lireLigne()
        firstFitDecreasing(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5) * 1000
    print(f"Résultat Clavier + FFD : {moyenne} millisecondes")

def testClavierRORB():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = lireLigne()
        randomOrderRandomBin(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5) * 1000
    print(f"Résultat Clavier + RORB : {moyenne} millisecondes")



##### ALEATOIRE #####


"""
On génère aléatoirement 10 éléments par instance 
"""
def genererInstance():
    nb_elements = 10
    list_objets = []
    for element in range(nb_elements):
        element = round(random.random(), 2)
        list_objets.append(element)
    return list_objets

def testAleatoireNF():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = genererInstance()
        nextFit(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5) * 1000
    print(f"Résultat Aleatoire + NF : {moyenne} millisecondes")

def testAleatoireFFD():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = genererInstance()
        firstFitDecreasing(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5) * 1000
    print(f"Résultat Aleatoire + FFD : {moyenne} millisecondes")

def testAleatoireRORB():
    time_list = []
    for i in range(10):
        start_time = time.time()
        objets = genererInstance()
        randomOrderRandomBin(objets)
        
        time_list.append(time.time()- start_time)
    moyenne = round(sum(time_list) / len(time_list), 5) * 1000
    print(f"Résultat Aleatoire + RORB : {moyenne} millisecondes")

def main():

    testFichierNF()
    testFichierFFD()
    testFichierRORB()
    print()
    testClavierNF()
    testClavierFFD()
    testClavierRORB()
    print()
    testAleatoireNF()
    testAleatoireFFD()
    testAleatoireRORB()

if __name__ == "__main__":
    main()