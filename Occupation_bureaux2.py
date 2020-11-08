n=jourf-jourd+1 #nombre de jours
def horaire(luminosité,date):
    i=0
    occupe=[]
    for k in range (n):#parcourt les jours
        while luminosité[i]<150: #bureaux non occupés
            i=i+1
        occupe.append(date[i][0][8:19])#dès que les bureaux sont occupées, on ajoute le jour et l'heure
        while luminosité[i]>150:#bureaux occupés
            i=i+1
        occupe.append(date[i][0][8:19])#dès que les bureaux sont vidés, on ajoute le jour et l'heure
        print (i)
    return occupe