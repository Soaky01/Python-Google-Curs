"""
1
Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma
parametrilor care reprezintă numere întregi sau reale.

"""
def your_function(*args, **kwargs):
    suma=0
    for i in args:
        if type(i) == int or type(i) == float:
            suma += i
    return suma
# print(your_function(1, 5, -3 , "abc", [12,56,'cad']))

"""
2
Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
"""
suma = 0
suma_par = 0
suma_impar = 0
tip = input("Tipul sumei(0-suma tuturor nr , 1- suma nr pare, 2-suma nr impare):")
def suma_recurs(x, tip):
    if tip == 0
        if x <= 1 :
            return x
        else:
            return x + suma_recurs(x-1,tip)
    elif tip == 1
        if x <= 2:
            return x
        if x % 2 == 0:
            return x + suma_recurs(x - 1,tip)
        else:
            return suma_recurs(x - 1, tip)
    elif tip == 2:
        if x <= 1:
            return n
        if x % 2 != 0:
            return x + suma_recurs(x - 1, tip)
        else:
            return suma_recurs(x - 1, tip)

"""
3
Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un
 număr întreg, altfel returnează valoarea 0
"""
def intreg():
    x = input("Numar: ")
    if x.isdigit() is True:
        return x
    else:
        return 0
