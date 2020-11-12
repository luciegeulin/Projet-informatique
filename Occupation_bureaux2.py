n=jourf-jourd+1 #nombre de jours
##Avec la luminosité
def horaire2(luminosité,date):
    i=0
    occupe=[]
    for k in range (n):#parcourt les jours
        while luminosité[i]<150:#bureaux non occupés
            i=i+1
        if len(occupe)==0:
            occupe.append(date[i][8:19])
        elif occupe[-1][0:2]!=date[i][8:10]:
            occupe.append(date[i][8:19]) #Si c'est la première fois que le seuil est dépassé, on ajoute l'heure
        while luminosité[i]>=150:#bureaux occupés
            i=i+1
        if len(occupe)==1:
            occupe.append(date[i][8:19])
        else :
            if occupe[-2][0:2]==date[i][8:10]: #si c'est la deuxième fois qu'un horaire de sortie de bureaux est ajouté, on remplace l'ancien horaire de sortie par celui-là
                occupe[-1]=date[i][8:19]
            else :
                occupe.append(date[i][8:19])
    print(i)
    return occupe

