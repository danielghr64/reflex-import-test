
import math
import matplotlib.pyplot as plt

def func_e(t: float):
    return math.exp((-(t**2))/2)

def function(a: float):
    if a > 0:
        return math.sqrt(a)
    else:
        raise ValueError("Que des nombres positifs")

def left_rect(_function=None, a:float=0, b:float=0, n:int=1):
    if _function:
        if n < 1:
            raise ValueError("Le nombre de subdivision doit être supérieur ou égal à 1")

        h = abs(b - a) / n
        a = min(a, b)
        res = 0

        for k in range(n):
            a_k = a + k*h
            res += _function(a_k)

        return h*res

    else:
        raise ValueError("You need a function to continue")
    
def right_rect(_function=None, a:float=0, b:float=0, n:int=1):
    if _function:
        if n < 1:
            raise ValueError("Le nombre de subdivision doit être supérieur ou égal à 1")

        h = abs(b - a) / n
        a = min(a, b)
        res = 0
        
        for k in range(1, n+1):
            a_k = a + k*h
            res += _function(a_k)

        return h*res

    else:
        raise ValueError("You need a function to continue")

def trapeze(_function=None, a:float=0, b:float=0, n:int=1):
    if _function:
        if n < 1:
            raise ValueError("Le nombre de subdivision doit être supérieur ou égal à 1")

        h = abs(b - a) / n
        a = min(a, b)
        res = 0
        
        for k in range(n):
            a_k = a + k*h
            a_k1 = a + (k+1)*h
            res += (_function(a_k) + _function(a_k1))

        return (h / 2)*res

    else:
        raise ValueError("You need a function to continue")

def simpson(_function=None, a:float=0, b:float=0, n:int=1):
    if _function:
        if n < 1:
            raise ValueError("Le nombre de subdivision doit être supérieur ou égal à 1")

        h = abs(b - a) / n
        a = min(a, b)
        res = 0
        
        for k in range(n):
            a_k = a + k*h
            a_k1 = a + (k+1) * h
            z_k = (a_k1 + a_k) / 2
            res += (_function(a_k) + 4*_function(z_k) + _function(a_k1))

        return (h/6)*res

    else:
        raise ValueError("You need a function to continue")


# Par la suite, on utilisera la méthode de Richardson pour évaluer l'erreur sur l'estimation de l'intégrale

def erreur(_function=None, a: float=0, b: float=0, n: int=1, _methode=None):
    k: int # Ordre de convergence lié à la méthode utilisé
    if _function:
        if n < 1:
            raise ValueError("Le nombre de subdivision doit être supérieur ou égal à 1")

        if _methode == left_rect or _methode == right_rect:
            k = 1
        
        elif _methode == trapeze:
            k = 2

        elif _methode == simpson:
            k = 4

        else:
            raise ValueError("Methode d'estimation non reconnue dans l'estimation de l'erreur")
        
        err = abs(_methode(_function, a, b, n) - _methode(_function, a, b, 2*n)) / ((2**k) - 1)

        return err
    
    else:
        raise ValueError("You need a function to estimate de error")


def min_subdivision(_function=None, a: float=0, b: float=0, Err: float=1, _methode=None):
    if _function:
        if _methode not in (left_rect, right_rect, trapeze, simpson):
            raise ValueError("Methode d'estimation non reconnue dans l'évaluation du nombre de subdivision")
        
        n = 2
        error = erreur(_function, a, b, n, _methode)

        while error > Err:
            n+=1
            error = erreur(_function, a, b, n, _methode)

        return n        
    
    else:
        raise ValueError("You need a function to estimate de error")    

def courbe():
    # plt.plot(x, y, label=f"y = {a}x + {b}")

    # Ajouter des labels et une légende
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Courbe affine")
    plt.legend()

    # Afficher le graphique
    plt.grid()
    plt.show()
# print(left_rect(func_e, 0, 1, 100))
# print(right_rect(func_e, 0, 1, 100))
# print(trapeze(func_e, 0, 1, 100))
# print(simpson(func_e, 0, 1, 100))

for i, methode in enumerate((left_rect, right_rect, trapeze, simpson)):
    print(f"erreur {i}: {erreur(func_e, 0, 1, 100, methode)}")
    print(f"min_subdivision {i}: {min_subdivision(func_e, 0, 1, 1e-4, methode)}")

#2. Remarque: La methode de Simpson donne une valeur beaucoup plus proche de la valeur théorique que les autres méthodes
