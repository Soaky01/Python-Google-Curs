# cuvant = ' o n o m a t o p e e'
"""
daca litera de inceput si litera de sfarsit se gasesc in interiorul cuvantului,
litera trebuie sa fie vizibila
cuvant = 'o _ o _ _ _ o _ e e'
7 incercari
"""
import random
from cuvinte_spanzuratoarea import cuvinte_de_ghicit as lista_cuvinte
print(random.choice(lista_cuvinte))

cuvant_de_ghicit = "onomatopee".lower()
cuvant = list(cuvant_de_ghicit)
litere_incercate = set()


def parcurgere_cuvant(word: str, simbol_de_inlocuit: str, cuvant_ascuns: list, operatie: bool = True) -> list:
    """

    :param word: reprezinta cuvantul care trebuie ghicit
    :param simbol_de_inlocuit: simbolul cu care se inlocuieste
    :param cuvant_ascuns: cuvantu ascuns si modificat dupa fiecare introducere de caracter
    :return: cuvantul modificat
    """
    for index, valoare in enumerate(word):
        if simbol_de_inlocuit == "_" and word[0] != valoare and word[-1] != valoare:
            cuvant_ascuns[index] = simbol_de_inlocuit
        elif word[0] != valoare and word[-1] != valoare and valoare == simbol_de_inlocuit:
            cuvant_ascuns[index] = simbol_de_inlocuit
    return cuvant_ascuns


cuvant = parcurgere_cuvant(cuvant_de_ghicit, "_", cuvant)
cuvant_de_afisat = ' '.join(cuvant)
# print(f"Cuvantul de ghicit este: {cuvant_de_afisat}")
""" 
    sa nu fie cifra => string.isdigit()
    sa nu introduca mai mult de un caracter => len(string) > 1
    sa nu fie spatiu
"""

numar_incercari = 0

while numar_incercari < 7:

    if len(list(litere_incercate)):
        print(f'Literele incercate sunt: {",".join(litere_incercate)}')

    litera_de_incercat = input("Adauga o litera: ").lower()

    while litera_de_incercat.isalpha() is False or len(litera_de_incercat) > 1:
        if litera_de_incercat.isalpha() is False:
            print("Ai adaugat un alt caracter. Te rugam sa introduci un o litera")
        if len(litera_de_incercat) > 1:
            print(f"Ai adaugat mai multe caractere. Ai voie sa adaugi un singur caracter. ")
        litera_de_incercat = input("Adauga o litera: ").lower()
    if litera_de_incercat not in cuvant_de_ghicit:
        numar_incercari += 1
        litere_incercate.add(litera_de_incercat)
    elif litera_de_incercat in cuvant_de_ghicit and (cuvant_de_ghicit[0] != litera_de_incercat and
                                                     cuvant_de_ghicit[-1] != litera_de_incercat):
        parcurgere_cuvant(cuvant_de_ghicit, litera_de_incercat, cuvant)
        # for index, valoare in enumerate(cuvant_de_ghicit):
        #     if valoare == litera_de_incercat:
        #         cuvant[index] = litera_de_incercat

    if '_' not in cuvant:
        print("Ai castigat!")
        print(f"Cuvantul este : {cuvant_de_ghicit}")
        break
    elif numar_incercari == 7:
        print(f"Ai pierdut. Cuvantul initial era: {cuvant_de_ghicit}")
    else:
        print(f"Mai ai {7 - numar_incercari} incercari")
    # if (numar_incercari_ramase := 7 - numar_incercari) and numar_incercari_ramase > 0:
    #     print(f"Mai ai {7 - numar_incercari} incercari")
    print(" ".join(cuvant))
