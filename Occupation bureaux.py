## Détermination automatique des horaires d'occupation des bureaux

# Etude sur un seul capteur
def horaires (liste_luminosité, liste_dates):
    l=len(liste_luminosité)
    occupé=[]
    for i in range(0,l):
        if liste_luminosité[i]>150:          #correspond à un seuil choisi que nous avons choisi
            occupé.append(liste_dates[i][0][11:19])
    return occupé

