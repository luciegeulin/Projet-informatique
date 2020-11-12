def bruit_jour(L1, L1_t):#Sépare la liste des bruits par jours
    L_indj=[0]#Future liste comportant les indices, lorsque la liste des temps change de jour.
    noise_jour=[]#Future liste de liste séparée par jour
    a=jourd#Jour de départ
    for x in L1_t:#Boucle sur la liste des dates.
        if int(x[8:11])==a:#Condition déterminant si le jour est le même que le précédent
            a=int(x[8:11])#a prend la nouvelle valeur du jour
        else:
            a=int(x[8:11])
            L_indj.append(L1_t.index(x))#Si la date du jour est différente de la date précédente, on ajoute son indice dans la liste.
    L_indj.append(len(L1))#On ajoute le dernier indice de la liste des temps
    for i in range(len(L_indj)-1):
        i_d=L_indj[i]
        i_f=L_indj[i+1]
        noise_jour.append(L1[i_d:i_f])#A l'aide de la liste des indices, on sépare la liste L1 suivant les différents jours.
    return noise_jour

def moye_bruit(L_bruit, L_date):
    bruit=bruit_jour(L_bruit,L_date)
    M=[]
    l=len(bruit)
    for i in range (l):
        m=moyenne(bruit[i])
        M.append(m)
    return M

def weekend(L_bruit,L_date):
    semaine=[]
    week_end=[]
    M=moye_bruit(L_bruit,L_date)
    j=int(L_date[0][8:10])#on récupère le premier jour
    n=len(M) #on récupère le nombre de jours
    for i in range (n):
        if M[i]>29.5:
            semaine.append(j)
        else :
            week_end.append(j)
        j=j+1
    return 'Les jours suivants sont les week-ends', week_end,'Les jours suivants tombent en semaine ', semaine




