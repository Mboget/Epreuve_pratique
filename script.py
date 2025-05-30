####################################### Sujet 1 #######################################

def voisins_entrants(adj, x):
    vois = []
    for i in range(len(adj)):
        if x in adj[i]:
            vois.append(i)
    return vois

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += str(compte) + chiffre 
            chiffre = s[i] 
            compte = 1
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat
print("------------------ TEST SUJET 1 ------------------")


####################################### Sujet 2 #######################################

def max_et_indice(tab):
    '''
    renvoie la valeur du plus grand élément de ce tableau ainsi
    que l’indice de sa première apparition dans ce tableau.
    '''
    val_max = tab[0]
    ind_max = 0
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            ind_max = i
    return (val_max, ind_max)

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = [] 

    for x in tab:
        if x < 1 or x > n or x in vus: 
            return False
        vus.append(x) 
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gènes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre) 
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < n - 1: 
        if ordre[i+1] - ordre[i] not in [-1, 1]: # l'écart n'est pas 1 
            nb = nb + 1
        i = i + 1
    if ordre[i] != n: # le dernier n'est pas n 
        nb = nb + 1
    return nb

print("------------------ TEST SUJET 2 ------------------")


####################################### Sujet 3 #######################################

def fibonacci(n):
    if n <= 2 :
        return 1   
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  []

    for i in range(len(eleves)) :
        if notes[i] == note_maxi :
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi, meilleurs_eleves)

print("------------------ TEST SUJET 3 ------------------")


####################################### Sujet 4 #######################################

def ecriture_binaire_entier_positif(n):
    if n == 0:
        return '0' 
    bin_n = '' 
    while n != 0 : 
        bin_n = str(n % 2) + bin_n 
        n = n // 2
    return bin_n

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n): 
        for j in range(n - 1 - i): 
            if tab[j] > tab[j+1]: 
                echange(tab, j, j+1)

print("------------------ TEST SUJET 4 ------------------")
tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
print(tab2)

####################################### Sujet 5 #######################################

def renverse(mot):
    sol = ''
    for lettre in mot:
        sol = lettre + sol
    return sol

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = 2*i 
            while multiple < n:
                tab[multiple] = False 
                multiple = multiple + i 
    return premiers

print("------------------ TEST SUJET 5 ------------------")

####################################### Sujet 6 #######################################

def liste_puissances(a,n):
    puissances = [a]
    for i in range(n-1):
        puissances.append(puissances[-1] * a)
    return puissances

def liste_puissances_borne(a, borne):
    lst = []
    val = a
    while val < borne:
        lst.append(val)
        val = val * a
    return lst

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


def codes_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    mot_est_parfait = code_concatene % code_additionne == 0
    return code_additionne, code_concatene, mot_est_parfait

print("------------------ TEST SUJET 6 ------------------")

####################################### Sujet 7 #######################################

def nbr_occurrences(chaine):
    nb_occ = {}
    for caractere in chaine:
        if caractere in nb_occ:
            nb_occ[caractere] += 1
        else:
            nb_occ[caractere] = 1
    return nb_occ

def fusion(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if tab1[i1] < tab2[i2]:
            tab12[i] = tab1[i1]
            i1 = i1 + 1
        else:
            tab12[i] = tab2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        tab12[i] = tab1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        tab12[i] = tab2[i2]
        i2 = i2 + 1
        i = i + 1
    return tab12

print("------------------ TEST SUJET 7 ------------------")

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

def fusion(tab1, tab2): # DUR A REVOIR AVANT #noqa
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
from random import randint  # noqa: E402

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

####################################### Sujet 21 #######################################

def indices_maxi(tableau:list[int])->(int,list[int]): # type: ignore
    indices = []
    maxi = tableau[0]

    for i in range(len(tableau)):
        if tableau[i] > maxi: 
            maxi = tableau[i]
            indices.append(i)

    return (maxi,indices)

def renverse(pile): #noqa
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = [] 
    while pile != []:
        pile_inverse.append(pile.pop())
    return pile_inverse


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = [] 
    while pile != []:
        element = pile.pop() 
        if element >= 0: 
            pile_positifs.append(element)
    return renverse(pile_positifs)

print("------------------ TEST SUJET 21 ------------------")

print(renverse([1, 2, 3, 4, 5]))
print(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]))

####################################### Sujet 22 #######################################

def recherche(elt:int,tab:list[int])->int:
    indice = None
    for i in range(len(tab)):
        if tab[i] == elt: 
            indice = i
    
    return indice

class AdresseIP: # DUR A REVOIR AVANT
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères 
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = ['192.168.0.0', '192.168.0.255'] 
        return self.adresse in reservees

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets()
        if octets[3] == 254: 
            return None
        octet_nouveau = octets[3] + 1 
        return AdresseIP('192.168.0.' + str(octet_nouveau))
    
print("------------------ TEST SUJET 22 ------------------")

print(recherche(1, [10, 12, 1, 56]))

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2') 
adresse3 = AdresseIP('192.168.0.3') 

print(adresse1.liste_octets())
print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)

####################################### Sujet 23 #######################################

def effectif_notes(tableau:list[int])->list[int]: # DUR A REVISER AVANT

    liste = [0]*11
    for element in tableau:
        liste[element]+=1

    return liste


def notes_triees(eff:list[int])->list[int]:
    for i in range(len(eff)-1):
        for j in range(i+1, len(eff)):
            if eff[j] < eff[i]:
                eff[j],eff[i] = eff[i],eff[j]
    
    return eff

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0 : 
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0': 
            return 0
        else:
            return 1 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

print("------------------ TEST SUJET 23 ------------------")

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
print(effectif_notes(notes_eval))

print(notes_triees(notes_eval))

print(dec_to_bin(25))
print(bin_to_dec('101010'))

####################################### Sujet 24 #######################################

def enumere(tab:list[int]):
    dico = {}

    for i in range(len(tab)): 
        element = tab[i]
        if element in dico: 
            dico[element]+=[i]
        else : 
            dico[element] = [i]
    return dico

class Noeud:
    """Classe représentant un noeud d'un arbre binaire"""
    def __init__(self, etiquette, gauche, droit):
        """Crée un noeud de valeur etiquette avec 
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre is not None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre is None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if cle < arbre.etiquette: 
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit,cle)
        return arbre

print("------------------ TEST SUJET 24 ------------------")

print(enumere([1, 2, 3]))
print(enumere([1, 1, 2, 3, 2, 1]))

a = Noeud(5, None, None)
a = insere(a, 2)
a = insere(a, 3)
a = insere(a, 7)
print(parcours(a, []))

a = insere(a, 1)
a = insere(a, 4)
a = insere(a, 6)
a = insere(a, 8)
print(parcours(a, []))

####################################### Sujet 25 #######################################

def annee_temperature_minimale(tab_temp,tab_annees):
    assert len(tab_temp) == len(tab_annees)
    
    mini_temp = tab_temp[0]
    annee_mini = tab_annees[0]

    for i in range (len(tab_temp)):
        if tab_temp[i] < mini_temp:
            mini_temp = tab_temp[i]
            annee_mini = tab_annees[i]
    
    return (mini_temp,annee_mini) 

def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = '' 
    for caractere in chaine:
        resultat = caractere + resultat 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return chaine == inverse 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre) 
    return est_palindrome(chaine)

print("------------------ TEST SUJET 25 ------------------")

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(annee_temperature_minimale(t_moy, annees))

print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))

print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))

####################################### Sujet 26 #######################################

def ajoute_dictionnaires(d1, d2):
    d = {}
    for cle in d1:
        d[cle] = d1[cle]
    for cle in d2:
        if cle in d:
            d[cle] += d2[cle]
        else:
            d[cle] = d2[cle]
    return d

from random import randint #noqa E402 #noqa F811  

def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [ False ] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 0 
    while nombre_cases_vues < nombre_cases: 
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nombre_cases 
        if not cases_vues[case_en_cours]: 
            cases_vues[case_en_cours] = True
            nombre_cases_vues = nombre_cases_vues + 1 
        n = n + 1 
    return n


print("------------------ TEST SUJET 26 ------------------")

print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))


####################################### Sujet 27 #######################################

def verifie(tab):
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            return False
    return True

def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax: 
            nmax = election[candidat] 
    liste_finale = [ nom for nom in election if election[nom] == nmax ]
    return liste_finale


print("------------------ TEST SUJET 27 ------------------")

print(verifie([0, 5, 8, 8, 9]))

urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
election = depouille(urne)

print(election)
print(vainqueurs(election))

####################################### Sujet 28 #######################################

def a_doublon(tab):
    for i in range(len(tab)-1):
        if tab[i] == tab[i+1]:
            return True
    return False

def voisinage(n, ligne, colonne):
    """ Renvoie la liste des coordonnées des voisins de la case
    (ligne, colonne) en gérant les cases sur les bords. """
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):  # noqa: E741
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins


def incremente_voisins(grille, ligne, colonne):
    """ Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins: # noqa: E741
        if grille[l][c] != -1: # si ce n'est pas une bombe
            grille[l][c] += 1  # on ajoute 1 à sa valeur



def genere_grille(bombes):
    """ Renvoie une grille de démineur de taille nxn où n est
    le nombre de bombes, en plaçant les bombes à l'aide de
    la liste bombes de coordonnées (tuples) passée en
    paramètre. """
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1 # place la bombe
        incremente_voisins(grille, ligne, colonne) # incrémente ses voisins

    return grille

print("------------------ TEST SUJET 28 ------------------")

print(a_doublon([2, 5, 7, 7, 7, 9]))

print(genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]))

####################################### Sujet 29 #######################################

def selection_enclos(animaux, num_enclos):
    table = []
    for animal in animaux:
        if animal['enclos'] == num_enclos:
            table.append(animal)
    return table

def trouver_intrus(tab, g, d):
    '''
    Renvoie la valeur de l'intrus situé entre les indices g et d 
    dans la liste tab où :
    tab vérifie les conditions de l'exercice,
    g et d sont des multiples de 3.
    '''
    if g == d:
        return tab[g]

    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] != tab[indice + 1] :
            return trouver_intrus(tab, g, indice)
        else:
            return trouver_intrus(tab, indice + 3, d)
        

print("------------------ TEST SUJET 29 ------------------")

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
            {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
            {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
            {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
            {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

print(selection_enclos(animaux, 5))

tab_a = [3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8, 5, 5, 5]
print(trouver_intrus(tab_a,0, 21))

tab_b = [8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3]
print(trouver_intrus(tab_b,0,12))

tab_c = [5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8]
print(trouver_intrus(tab_c,0,15))

####################################### Sujet 30 #######################################

def delta(tab):
    diff = [tab[0]]
    for i in range(1, len(tab)):
        diff.append(tab[i] - tab[i-1])
    return diff

class Expr:
    """Classe implémentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérande ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = '' 
        if self.gauche is not None:
            s = '(' + s + self.gauche.infixe() 
        s = s + str(self.valeur) 
        if self.droite is not None: 
            s = s + self.droite.infixe() + ')' 
        return s


print("------------------ TEST SUJET 30 ------------------")

print(delta([1000, 800, 802, 1000, 1003]))

a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))
print(a.infixe())

b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)), '*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None)))
print(b.infixe())

####################################### Sujet 31 #######################################

def recherche_motif(motif, texte):
    sol = []
    i = 0
    while i <= len(texte) - len(motif):
        j = 0
        while j < len(motif) and motif[j] == texte[j+i]:
            j += 1
        if j == len(motif):
            sol.append(i)
        i += 1
    return sol

adj = [[1, 2], [0, 3], [0], [1], [5], [4]]

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc

print("------------------ TEST SUJET 31 ------------------")

print(recherche_motif("ab", "abracadabra"))
print(recherche_motif("ab", "abracadabraab"))

print(accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 0))
print(accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 4))

####################################### Sujet 32 #######################################

def occurrences(caractere, chaine):
    somme = 0
    for lettre in chaine:
        if lettre == caractere:
            somme += 1
    return somme

valeurs = [100,50,20,10,5,2,1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre, rang + 1)

print("------------------ TEST SUJET 32 ------------------")

print(rendu_glouton(67, 0))
print(rendu_glouton(291,1))

####################################### Sujet 33 #######################################

def insertion_abr(a, cle): 
    if a is None:
        return (None, cle, None)
    elif cle > a[1]:
        return (a[0], a[1], insertion_abr(a[2], cle))
    elif cle < a[1]:
        return (insertion_abr(a[0], cle), a[1], a[2])
    return a

def empaqueter(liste_masses, c):
    """Renvoie le nombre minimal de boîtes nécessaires pour
    empaqueter les objets de la liste liste_masses, sachant
    que chaque boîte peut contenir au maximum c kilogrammes"""
    n = len(liste_masses)
    nb_boites = 0
    boites = [ 0 for _ in range(n) ]
    for masse in liste_masses: 
        i = 0
        while i < nb_boites and boites[i] + masse > c: 
            i = i + 1
        if i == nb_boites:
            nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse 
    return nb_boites

print("------------------ TEST SUJET 33 ------------------")

n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

print(insertion_abr(abr1, 4))

print(empaqueter([1, 2, 3, 4, 5], 10))

####################################### Sujet 34 #######################################

def tri_selection(tab):
    for i in range(len(tab)-1):
        indice_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[indice_min]:
                indice_min = j
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab

from random import randint  # noqa: E402, F811

def plus_ou_moins():
    nb_mystere = randint(1,99)
    nb_test = int(input('Proposez un nombre entre 1 et 99 : '))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input('Trop petit ! Testez encore : '))
        else:
            nb_test = int(input('Trop grand ! Testez encore : '))

    if nb_mystere == nb_test:
        print ('Bravo ! Le nombre était ', nb_mystere)
        print('Nombre d essais: ', compteur)
    else:
        print ('Perdu ! Le nombre était ', nb_mystere)

print("------------------ TEST SUJET 34 ------------------")
tab = [1, 52, 6, -9, 12]
print(tri_selection(tab))

####################################### Sujet 35 #######################################

def max_dico(dico):
    cle_max = ''
    val_max = 0
    for cle in dico:
        if dico[cle] > val_max:
            val_max = dico[cle]
            cle_max = cle
    return (cle_max, val_max)

class Pile: # noqa: F811
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()

print("------------------ TEST SUJET 35 ------------------")

####################################### Sujet 36 #######################################

def nombre_de_mots(phrase):
    nb_mots = 0
    for caractere in phrase:
        if caractere == ' ' or caractere == '.':
            nb_mots += 1
    return nb_mots

class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche is not None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit is not None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)

print("------------------ TEST SUJET 36 ------------------")

####################################### Sujet 37 #######################################

def gb_vers_entier(tab):
    somme = 0
    for i in range(len(tab)):
        if tab[i]:
            somme += 2**(len(tab)-1-i)
    return somme

def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer 
        # où placer la valeur à ranger
        j = i 
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]: 
            tab[j] = tab[j-1]
            j = j - 1 
        tab[j] = valeur_insertion

print("------------------ TEST SUJET 37 ------------------")


####################################### Sujet 38 #######################################

def moyenne(tab):
    somme = 0
    for val in tab:
        somme += val
    return somme / len(tab)

def binaire(a): # noqa: F811
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0' 
    bin_a = '' 
    while a != 0 : 
        bin_a = str(a % 2) + bin_a 
        a = a // 2
    return bin_a

print("------------------ TEST SUJET 38 ------------------")

####################################### Sujet 39 #######################################

def moyenne(tab):
    if tab == []:
        print('Le tableau donné est vide')
        return None
    else:
        somme = 0
        for elt in tab:
            somme += elt
        return somme / len(tab)
    
def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée 
    j = len(tab) - 1 # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = i + 1 
        else:
            tab[i],tab[j] = tab[j],tab[i]
            j = j -1

print("------------------ TEST SUJET 39 ------------------")

####################################### Sujet 40 #######################################

def recherche_indices_classement(elt, tab):
    ind_inf = []
    ind_egal = []
    ind_sup = [] 
    for i in range(len(tab)):
        if tab[i] < elt:
            ind_inf.append(i)
        elif tab[i] > elt:
            ind_sup.append(i)
        else:
            ind_egal.append(i)
    return (ind_inf, ind_egal, ind_sup)

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
    resultats. Si nom n'est pas dans le dictionnaire, 
    la fonction renvoie None.'''
    if nom in resultats: 
        notes = resultats[nom]
        if notes == {}: # pas de notes 
            return 0
        total_points = 0 
        total_coefficients = 0 
        for valeurs in notes.values(): 
            note, coefficient = valeurs
            total_points = total_points + note * coefficient 
            total_coefficients = total_coefficients + coefficient 
        return round( total_points / total_coefficients, 1 ) 
    else:
        return None

print("------------------ TEST SUJET 40 ------------------")

####################################### Sujet 41 #######################################

def ou_exclusif(tab1, tab2):
    resultat = []
    taille = len(tab1)
    for i in range(taille):
        resultat.append(tab1[i] ^ tab2[i])
    return resultat

class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)

        #test de la somme de chaque ligne
        for i in range(self.ordre):
            if self.somme_ligne(i) != s:
                return False

        #test de la somme de chaque colonne
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False

        return True

print("------------------ TEST SUJET 41 ------------------")

####################################### Sujet 42 #######################################

def nb_repetitions(elt, tab):
    nb = 0
    for element in tab:
        if element == elt:
            nb += 1
    return nb

def binaire(a): #noqa F811
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0' 
    bin_a = '' 
    while a != 0 : 
        bin_a = str(a % 2) + bin_a 
        a = a // 2
    return bin_a


print("------------------ TEST SUJET 42 ------------------")

####################################### Sujet 43 #######################################

def couples_consecutifs(tab):
    solution = []
    for i in range(len(tab)-1):
        if tab[i] + 1 == tab[i+1]:
            solution.append((tab[i], tab[i+1]))
    return solution

def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage à gauche
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage à droite 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0: # propage en haut 
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M[i]): # propage en bas 
        colore_comp1(M, i, j+1, val)

print("------------------ TEST SUJET 43 ------------------")

####################################### Sujet 44 #######################################

def moyenne(tab):
    somme = 0
    coeffs = 0
    for couple in tab:
        somme += couple[0] * couple[1]
        coeffs += couple[1]
    if coeffs == 0:
        return None
    return somme / coeffs

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
    des " *" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart, k):
    '''renvoie une liste contenant k fois chaque 
    élément de liste_depart'''
    liste_zoomee = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee

def dessin_zoom(grille, k):
    '''renvoie une grille où les lignes sont zoomées k fois 
    ET répétées k fois'''
    grille_zoomee = []
    for ligne in grille:
        liste_zoomee = liste_zoom(ligne, k)
        for i in range(k):
            grille_zoomee.append(liste_zoomee)
    return grille_zoomee

print("------------------ TEST SUJET 44 ------------------")

####################################### Sujet 45 #######################################

def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1

    return nb_destinaires == len(plan)

print("------------------ TEST SUJET 45 ------------------")

print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}))
print(est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}))
print(est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}))
print(est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}))

####################################### Sujet 46 #######################################

def compte_occurrences(x, tab):
    nb = 0
    for element in tab:
        if element == x:
            nb += 1
    return nb

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = [] 
    a_rendre = somme_versee - somme_due 
    i = len(pieces) - 1
    while a_rendre > 0: 
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(pieces[i]) 
        a_rendre = a_rendre - pieces[i] 
    return rendu

print("------------------ TEST SUJET 46 ------------------")

####################################### Sujet 47 #######################################

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}


def taille(arbre, lettre):
    if lettre == '':
        return 0
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

def echange(tab, i, j): #noqa
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N): 
        imin = k 
        for i in range(k + 1, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin)

print("------------------ TEST SUJET 47 ------------------")

####################################### Sujet 48 #######################################

def recherche(tab, n):
    indice_solution = None
    for i in range(len(tab)):
        if tab[i] == n:
            indice_solution = i
    return indice_solution

def distance_carre(point1, point2):
    """ Calcule et renvoie la distance au carre entre 
    deux points."""
    return (point1[0] - point2[0])**2 + ((point1[1] - point2[1]))**2

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se 
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = distance_carre(min_point, depart) 
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < min_dist: 
            min_point = tab[i] 
            min_dist = distance_carre(tab[i], depart) 
    return min_point

print("------------------ TEST SUJET 48 ------------------")
