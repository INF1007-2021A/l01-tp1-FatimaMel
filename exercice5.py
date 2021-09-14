def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    position_initial1 = 0
    position_initial2 = distance
    v1 = v1
    v2 = v2

    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    temps_pris = (position_initial2 - position_initial1)/(v1 + v2)


    positionRencontre = position_initial1 + (v1*temps_pris)

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
