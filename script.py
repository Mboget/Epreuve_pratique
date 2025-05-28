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


def dichotomie(tab, x):
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

