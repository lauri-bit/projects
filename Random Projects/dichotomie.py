
PRECISION = 12 #nombres de chiffre après la virgule pour toute fonctions

def dichotomie(nb):
    bas_intervalle=0
    haut_intervalle=0

    if nb >= 1:
        bas_intervalle=0
        haut_intervalle=nb

    elif nb > 0 and nb < 1:
        bas_intervalle=nb
        haut_intervalle=1

    elif nb == 0:
        racine=0
        return racine

    elif nb < 0:
        raise ValueError("Le nombre doit être défini dans les réels")

    while round(bas_intervalle,PRECISION) != round(haut_intervalle,PRECISION):
        milieu=(bas_intervalle+haut_intervalle)/2

        if milieu ** 2 < nb:
            bas_intervalle=milieu

        elif milieu ** 2 >= nb:
            haut_intervalle=milieu

    racine=round(bas_intervalle,PRECISION)
    return racine

print(dichotomie(8))

def chiffre_par_chiffre(nb):

    unité=1
    while unité**2 < nb:
        unité +=1
    racine = unité - 1

    for i in range(PRECISION + 1):

        for j in range(10):
            if j == 0:
                continue

            décimal= j * (10 ** -(i + 1))
            racine_test= racine + décimal

            if racine_test ** 2 > nb:
                if j != 1:
                   racine += (j - 1) * (10 ** -(i + 1))
                   break
    racine=round(racine,PRECISION)
    return racine

print(chiffre_par_chiffre(8))