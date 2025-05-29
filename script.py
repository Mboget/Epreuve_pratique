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