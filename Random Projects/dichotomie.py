
PRECISION = 8 #nombres de chiffre après la virgule pour toute fonctions

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

def chiffre_par_chiffre(nb):

    if len(nb) == 3:
        for i in range(100,1000,100):
            if i**2 <= nb >= (i+100)**2:
                return i

