import time
import random
from main import nextFit, firstFitDecreasing, randomOrderRandomBin

def getObjets(ligne):

    ligne = ligne.replace(" ", "")
    arg_list = ligne.split(":")
    objets = arg_list[:1]
    return objets

def lireFichier():
    with open("input.txt") as file:
        ligne = file.readline()
    
    return getObjets(ligne)
    
def testFichierNF():
    time_list = []
    for i in range(10):
        cpt1 = time.perf_counter()
        objets = lireFichier()
        nextFit(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Fichier + NF : {moyenne:0.4f} secondes")

def testFichierFFD():
    time_list = []
    for i in range(10):
        cpt1 = time.perf_counter()
        objets = lireFichier()
        firstFitDecreasing(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Fichier + FFD : {moyenne:0.4f} secondes")

def testFichierRORB():
    time_list = []
    for i in range(10):
        cpt1 = time.perf_counter()
        objets = lireFichier()
        randomOrderRandomBin(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Fichier + RORB : {moyenne:0.4f} secondes")


def lireLigne():
    ligne = "10:0.3:0.2:0.5:0.8:0.1:0.4:0.7:0.6:0.2:0.9"

    return getObjets(ligne)

def testClavierNF():
    time_list = []
    for i in range(10):
        cpt1 = time.perf_counter()
        objets = lireLigne()
        nextFit(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Clavier + NF : {moyenne:0.4f} secondes")

def testClavierFFD():
    time_list = []
    for i in range(10):
        cpt1 = time.perf_counter()
        objets = lireLigne()
        firstFitDecreasing(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Clavier + FFD : {moyenne:0.4f} secondes")

def testClavierRORB():
    time_list = []
    for i in range(10):
        cpt1 = time.perf_counter()
        objets = lireLigne()
        randomOrderRandomBin(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Clavier + FFD : {moyenne:0.4f} secondes")


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
        cpt1 = time.perf_counter()
        objets = genererInstance()
        nextFit(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Aleatoire + NF : {moyenne:0.4f} secondes")

def testAleatoireFFD():
    time_list = []
    for i in range(10):
        cpt1 = time.perf_counter()
        objets = genererInstance()
        firstFitDecreasing(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Aleatoire + NF : {moyenne:0.4f} secondes")

def testAleatoireRORB():
    time_list = []
    for i in range(10):
        cpt1 = time.perf_counter()
        objets = genererInstance()
        randomOrderRandomBin(objets)
        cpt2 = time.perf_counter()
        time_list.append(cpt2- cpt1)
    moyenne = sum(time_list) / len(time_list)
    print(f"Résultat Aleatoire + NF : {moyenne:0.4f} secondes")