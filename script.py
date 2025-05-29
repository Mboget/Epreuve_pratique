####################################### Sujet 8 #######################################

def maximum_tableau(tableau): 
    maxi = tableau[0]

    for element in tableau:
        if maxi < element:
            maxi = element 


    return maxi


class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()
    
def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch 
    est bien parenthésée"""
    p = Pile()
    for c in ch:
        if c == '(': 
            p.empiler(c)
        elif c == ')': 
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()

print("------------------ TEST SUJET 8 ------------------")

print( maximum_tableau([98, 12, 104, 23, 131, 9]))
print(maximum_tableau([-27, 24, -3, 15]))

print(bon_parenthesage("((()())(()))"))
print(bon_parenthesage("())(()"))
print(bon_parenthesage("(())(()"))

####################################### Sujet 9 #######################################

def multiplication(n1:int,n2:int)->int:
    """
    Fait une multiplication sans utiliser l'opérateur *
    """
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)

    resultat = 0

    for _ in range(n2):
        resultat += n1

    return resultat


def dichotomie(tab, x): # DUR A REVOIR AVANT
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m =  (debut+fin)//2
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1 
    return False


print("------------------ TEST SUJET 9 ------------------")

print(multiplication(3,5))
print( multiplication(-4, -8))

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))


####################################### Sujet 10 #######################################

def recherche(tableau,n): # DUR A REVOIR AVANT

    debut = 0

    fin = len(tableau)-1

    while debut <= fin :
        m = (debut+fin)//2

        if n == tableau[m]:
            return m
        if n < tableau[m]:
            fin = m -1

        else : 
            debut = m + 1
    return None 

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for lettre in message: 
        if 'A' <= lettre and lettre <= 'Z':
            indice = (position_alphabet(lettre)+decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat += lettre 
    return resultat



print("------------------ TEST SUJET 10 ------------------")

print( recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))


####################################### Sujet 11 #######################################

def parcours_largeur(arbre): # DUR A REVOIR AVANT
    parcours = []
    file = [arbre]
    while file != []:
        a = file.pop(0)
        parcours.append(a[1])
        if a[0] is not None:
            file.append(a[0])
        if a[2] is not None:
            file.append(a[2])
    return parcours

def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if sommes_max[i-1] + tab[i] > tab[i]:
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i]  > sommes_max[maximum]:
            maximum = i
    return sommes_max[maximum]

print("------------------ TEST SUJET 11 ------------------")

arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )
print(parcours_largeur(arbre))


####################################### Sujet 12 #######################################

def fusion(tab1, tab2): # DUR A REVOIR AVANT
    tab_fusion = []
    i1 = 0
    i2 = 0
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab_fusion.append(tab1[i1])
            i1 += 1
        else:
            tab_fusion.append(tab2[i2])
            i2 += 1

    if i1 == len(tab1):
        while i2 < len(tab2):
            tab_fusion.append(tab2[i2])
            i2 += 1
    else:
        while i1 < len(tab1):
            tab_fusion.append(tab1[i1])
            i1 += 1        

    return tab_fusion

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """ Renvoie l’écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]

print("------------------ TEST SUJET 12 ------------------")
print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))
print(fusion([], []))
print(fusion([1, 2, 3], []))

print(traduire_romain("XIV"),"\n",traduire_romain("CXLII"),"\n",traduire_romain("MMXXIV"))

####################################### Sujet 13 #######################################

def recherche (elt,tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return None 

def recherche2(elt,tab):
    try: 
        tab.index(elt)
    except ValueError:
        return None 

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab[i]: 
        tab_a[i] = tab[i] 
        tab_a[i+1] = a
        i += 1 
    return tab_a

print("------------------ TEST SUJET 13 ------------------")

print(recherche(1,[2,3,4]))
print(recherche2(1,[2,3,4]))

#print([2,3,4].index(1))

print(insere([1, 2, 4, 5], 3))

####################################### Sujet 14 #######################################
from random import randint
from turtle import pos  # noqa: E402

def lancer(n:int)->list[int]:
    tab = []
    for i in range(n):
        tab.append(randint(1,6))
    return tab

def paire_6(tableau:list[int])->bool:
    """Renvoie True s'il y a plus de deux 6 dans le tableau"""
    c = 0 

    for element in tableau:
        if element == 6:
            c+=1 
    
    if c >= 2 : 
        return True 
    
    else : 
        return False 

def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image) 

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return len(image[0]) 

def negatif(image): # DUR A REVOIR AVANT 
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            nouvelle_image[i][j] = 255 - image[i][j] 
    return nouvelle_image

def binaire(image, seuil): # DUR A REVOIR AVANT
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 1 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            if image[i][j] < seuil : 
                nouvelle_image[i][j] = 0 
            else:
                nouvelle_image[i][j] = 255 
    return nouvelle_image

print("------------------ TEST SUJET 14 ------------------")
for _ in range(1):
    a = lancer(5)
    print(a)
    print(paire_6(a))

####################################### Sujet 15 #######################################

def multiplication2 (n1,n2):
    if n1 < 0:
        return -multiplication2(-n1,n2) 
    elif n2 < 0 : 
        return -multiplication2(n1,-n2)
    res = 0 
    for _ in range(n2):
        res += n1

    return res

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x: 
        return chercher(tab, x, m+1 , j) 
    elif tab[m] > x:
        return chercher(tab, x, i , m-1) 
    else:
        return m

print("------------------ TEST SUJET 15 ------------------")

print(multiplication2(4,-8))

print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))

####################################### Sujet 16 #######################################

def moyenne(notes:list[(float,int)])->float:
    assert notes != []
    numerateur = 0 
    denominateur = 0
    for (note,coef) in notes:
        numerateur += note*coef
        denominateur += coef

    return numerateur / denominateur

def ligne_suivante(ligne): #DUR A REVOIR AVANT
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [ligne[0]] 
    for i in range(1,len(ligne)): 
        ligne_suiv.append(ligne[i-1]+ligne[i]) 
    ligne_suiv.append(ligne[-1]) 
    return ligne_suiv

def pascal(n): #DUR A REVOIR AVANT
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [[1]]
    for k in range(n): 
        ligne_k = ligne_suivante(triangle[-1]) 
        triangle.append(ligne_k)
    return triangle

print("------------------ TEST SUJET 16 ------------------")

print(moyenne([(15.0,2),(9.0,1),(12.0,3)]))

print(pascal(6))

####################################### Sujet 17 #######################################

class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

def hauteur(arbre):
    if arbre is None:
        return -1
    
    else : 
        return 1 + max(hauteur(arbre.gauche),hauteur(arbre.droit))
    
def taille(arbre):
    if arbre is None: 
        return 0
    
    else : 
        return 1 + taille(arbre.gauche) + taille(arbre.droit)

def ajoute(indice, element, tab): #DUR A REVOIR AVANT 
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i]
    tab_ins[indice] = element 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1]
    return tab_ins

print("------------------ TEST SUJET 17 ------------------")

print(hauteur(a))
print(taille(a))

print(ajoute(1, 4, [7, 8, 9]))

####################################### Sujet 18 #######################################

def moyenne(tableau):

    numerateur = 0 

    for element in tableau:
        numerateur += element

    return numerateur / len(tableau)

def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        m = (debut+fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1 
        else:
            fin = m - 1 
    return False

print("------------------ TEST SUJET 18 ------------------")

print(moyenne([1,2]))
print(dichotomie([15, 16, 18, 19, 23, 24, 28], 28))

####################################### Sujet 19 #######################################

def recherche_min(tableau:list[int])->int:
    mini = tableau[0]
    indice = 0 

    for element in tableau: 
        if element < mini:
            mini = element 
            indice = tableau.index(element)

    return indice

def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab)-1 
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche += 1 
        else :
            tab[gauche] = tab[droite] 
            tab[droite] = 1 
            droite -= 1 
    return tab

print("------------------ TEST SUJET 19 ------------------")

print(recherche_min([5, 3, 2, 2, 4]))
print(separe([1, 0, 1, 0, 1, 0, 1, 0]))

####################################### Sujet 20 #######################################

def min_et_max(tableau):
    dico = {'min':tableau[0],'max':tableau[0]}

    for element in tableau : 

        if element < dico['min']:
            dico['min'] = element 

        if element > dico["max"]:
            dico["max"] = element

    return dico 

class Carte:
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
            rangés par valeurs croissantes en commençant par pique, puis coeur,
            carreau et tréfle. """
        self.contenu = []
        for couleur in range(1,5):
            for valeur in range(1,14):
                self.contenu.append(Carte(couleur,valeur))

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos (entier compris entre 0 et 51). """
        assert (pos >= 0 and pos <= 51), 'on est dans un paquet de 52 cartes ducon !'
        
        return self.contenu[pos]

print("------------------ TEST SUJET 20 ------------------")

print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
jeu = Paquet_de_cartes()
carte1 = jeu.recuperer_carte(20)

print(carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur())
