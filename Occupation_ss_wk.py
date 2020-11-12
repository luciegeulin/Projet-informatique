#Puisqu'on a déterminé les week-end grâce au bruit, on peut enlever les week-ends des listes obtenues
def horaire_semaine(L_lum,L_date,L_noise):
    hor=occupation_bu(L_lum,L_date)
    wk,sem=weekend(L_noise,L_date)          #On dispose des jours de week-end grâce au programme écrit précédemment
    lh=len(hor)
    L=[]
    for i in range (lh):
        if int(hor[i][:2]) not in wk:       #Si le jour ne tombe pas un week-end
            L.append(hor[i])
    return L
