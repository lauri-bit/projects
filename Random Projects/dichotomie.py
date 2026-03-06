#Nous allons calculer la racine carrée d'un chiffre choisi selon deux méthodes différentes.

PRECISION = 12 #Nombre de chiffres après la virgule pour toutes fonctions

def dichotomie(nb):
    """
    Fonction qui va trouver la racine carrée de l'integer entré dans le paramètre nb de la fonction.
    En utilisant la méthode de dichotomie.
    """
    #Création des variables nécessaires pour calculer la racine
    bas_intervalle=0
    haut_intervalle=0

    #Utilisation des fonctions if/elif pour determiner l'intervalle nécessaire pour calculer la racine
    if nb >= 1:
        bas_intervalle=0
        haut_intervalle=nb

    elif nb > 0 and nb < 1:
        bas_intervalle=nb
        haut_intervalle=1

    #Vérification que le chiffre n'est pas zéro pour ne pas faire des calculs pour rien et aussi pour éviter une erreur plus tard.
    elif nb == 0:
        racine=0
        return racine

    #On s'assure qu'aucunes variable négatives peut être accepté pour ne pas causer d'erreur plus tard.
    elif nb < 0:
        raise ValueError("Le nombre doit être défini dans les réels")

    #Je crée un while loop qui va continuer de diviser la somme des extremités de l'intervalle jusqu'à temps que les deux extremités soit égale.
    #Lorsque les deux extremités sont égales, nous avons trouvé le juste milieu qui est la racine carrée.
    while round(bas_intervalle,PRECISION) != round(haut_intervalle,PRECISION):
        milieu=(bas_intervalle+haut_intervalle)/2

        #On vérifie la valeur obtenue par la division pour ensuite voir dans quel intervalle se trouve notre valeur cherchée.
        if milieu ** 2 < nb:
            bas_intervalle=milieu

        elif milieu ** 2 >= nb:
            haut_intervalle=milieu
    #On arrondit notre réponse à la précision définie en haut et on retourne la valeur trouvée de racine.
    racine=round(bas_intervalle,PRECISION)
    return racine


def chiffre_par_chiffre(nb):
    """
    Deuxième fonction pour trouver la racine carrée du chiffre entrée dans le paramètre nb de la fonction.
    Cette fonction trouve la racine carrée en regardant chiffre par chiffre, décimal par décimal pour finalement trouver la racine à la précision demandée.
    """
    #On commence par déterminer quel chiffre à la 2 se rapproche du nombre dans le paramètre nb
    unité=1
    while unité**2 < nb:
        unité +=1
    #Lorsqu'on trouve un chiffre à la 2 qui dépasse nb, on trouve maintenant la première unité de notre racine carrée, qui serait le chiffre juste avant. On passe maintenant aux décimales.
    racine = unité - 1

    #Je crée un loop pour calculer chaque décimal une à une, dans l'intervalle de 0 à la valeur determinée de la précision. Donc la loop s'arrêterait à PRÉCISION + 1.
    for i in range(PRECISION + 1):

        #Dans ce deuxième for loop, on vérifie la valeur de chaque décimal en regardant sa valeur possible entre 0 et 10 (non inclusivement).
        for j in range(1,10):

            #Nous calculons la valeur décimale de j en fonction de "i" (la valeur i va controller la position de j dans les décimales).
            décimal= j * (10 ** -(i + 1))

            #On additionne notre racine trouvée à la ligne 58 et le chiffre décimal obtenue, pour avoir notre racine temporaire.
            racine_temporaire= racine + décimal

            #On utilise cette racine temporaire pour comparer la valeur obtenue à la deux, à notre paramètre "nb". Donc tant que notre valeur racine_temporaire à la 2 est plus grande que la valeur de "nb".
            #Nous savons qu'il nous manque de la précision, donc le "j" continue d'augmenter sans qu'on active la condition sur la ligne 76.
            if racine_temporaire ** 2 > nb:
                #Lorsque nous trouvons une racine temporaire qui, à la 2, est plus grande que "nb", nous savons que la valeur cherchée pour ce point décimal i, est entre j et j - 1.
                #Donc, nous reculerons à j-1 et nous enregistrerons cette valeur décimale dans notre racine et nous irons chercher plus de précision dans le prochain la prochaine décimal i.
                if j != 1:
                   racine += (j - 1) * (10 ** -(i + 1))
                   #Après avoir ajouté la valeur décimale, nous sortons du for loop j, pour continue dans le for loop i. Nous continuons commme ça,jusqu'à temps qu'on se trouve à i = PRÉCISION.
                   break

    # On arrondit notre réponse à la précision définie en haut et on retourne la valeur trouvée de racine.
    racine = round(racine,PRECISION)
    return racine


print(dichotomie(8))
print(chiffre_par_chiffre(8))