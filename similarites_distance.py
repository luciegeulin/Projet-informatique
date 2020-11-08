# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:16:11 2020

@author: mario
"""

from math import log
from math import exp,sqrt
import matplotlib.pyplot as plt
import numpy as np



f=open('Données_california.txt','r')

donnees=[]
colonnes=6
#Liste de listes avec des donnees
ligne=f.readlines()#lecture de toutes les lignes du fichier de départ
n=len(ligne)
for i in range(1,n):#La première ligne n'est pas prise en compte car elle contient les titres des colonnes.
    L=ligne[i].split('\t')# Coupe la liste suivant le séparateur '\t'
    donnees.append(L)


#Récupération des données par capteurs
l=len(donnees)
c=len(donnees[1])
  
c1,c2,c3,c4,c5,c6=[],[],[],[],[],[]
for i in range(0,l):
    if int(donnees[i][0])==1:#Récupération des données seulement du capteur 1.
        c1.append(donnees[i])
    elif int(donnees[i][0])==2:
        c2.append(donnees[i])
    elif int(donnees[i][0])==3:
        c3.append(donnees[i])
    elif int(donnees[i][0])==4:
        c4.append(donnees[i])
    elif int(donnees[i][0])==5:
        c5.append(donnees[i])
    elif int(donnees[i][0])==6:
        c6.append(donnees[i])

#Données capteur1       
c1_n=[float(x[1]) for x in c1]#Récupération de la première colonne des données du capteur 1, ici, le bruit. 
c1_t=[float(x[2]) for x in c1]#Récupération de la température du capteur 1.
c1_h=[float(x[3]) for x in c1]#Récupération de l'humidité du capteur 1.
c1_l=[float(x[4]) for x in c1]#Récupération de la lumière du capteur 1.
c1_c=[float(x[5]) for x in c1]#Récupération du CO2 du capteur 1.
c1_d=[x[6].strip().split('\n' and '+0200') for x in c1]#Lucie, je te laisse l'expliquer.
for x in c1_d :
    del x[1]



#Données capteur2
c2_n=[float(x[1]) for x in c2]
c2_t=[float(x[2]) for x in c2]
c2_h=[float(x[3]) for x in c2]
c2_l=[float(x[4]) for x in c2]
c2_c=[float(x[5]) for x in c2]
c2_d=[x[6].strip().split('\n' and '+0200') for x in c2]
for x in c2_d :
    del x[1]


#Données capteur3
c3_n=[float(x[1]) for x in c3]
c3_t=[float(x[2]) for x in c3]
c3_h=[float(x[3]) for x in c3]
c3_l=[float(x[4]) for x in c3]
c3_c=[float(x[5]) for x in c3]
c3_d=[x[6].strip().split('\n' and '+0200') for x in c3]
for x in c3_d :
    del x[1]

#
c4_n=[float(x[1]) for x in c4]
c4_t=[float(x[2]) for x in c4]
c4_h=[float(x[3]) for x in c4]
c4_l=[float(x[4]) for x in c4]
c4_c=[float(x[5]) for x in c4]
c4_d=[x[6].strip().split('\n' and '+0200') for x in c4]
for x in c4_d :
    del x[1]


#Données capteur 5
c5_n=[float(x[1]) for x in c5]
c5_t=[float(x[2]) for x in c5]
c5_h=[float(x[3]) for x in c5]
c5_l=[float(x[4]) for x in c5]
c5_c=[float(x[5]) for x in c5]
c5_d=[x[6].strip().split('\n' and '+0200') for x in c5]
for x in c5_d :
    del x[1]


#Données capteur 6
c6_n=[float(x[1]) for x in c6]
c6_t=[float(x[2]) for x in c6]
c6_h=[float(x[3]) for x in c6]
c6_l=[float(x[4]) for x in c6]
c6_c=[float(x[5]) for x in c6]
c6_d_anomalie=[x[6].strip().split('\n' and '+0200') for x in c6]
for x in c6_d_anomalie:
    del x[1]

n=len(c6_d_anomalie)
c6_d=[['2020-09''-'+c6_d_anomalie[i][0][8:]] for i in range (n)]




#Bonus: Spécifier un intervalle de temps
debut=str(input('start_date:aaaa-mm-jj '))#Demande de la date de départ
fin=str(input('end_date:aaaa-mm-jj '))#Demande de la date de fin



anneed=int(debut[:4])
moisd=int(debut[5:7])
jourd=int(debut[8:])#Récupération du jour de départ (Seule donnée utile par rapport à la référence car toutes les mesures sont faites au mois de septembre 2020)

anneef=int(fin[:4])
moisf=int(fin[5:7])
jourf=int(fin[8:])



assert anneed==2020 and anneef==2020, "Vous devez saisir l'année 2020"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées en 2020, le assert permet de vérifier que l'utilisateur entre bien l'année 2020
assert moisd==9 and moisf==9, "Vous devez saisir le mois de septembre"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées en septembre, le assert permet de vérifier que l'utilisateur entre bien le mois de septembre.
assert  11<=jourd<=25 and 11<=jourf<=25, "La jour doit être compris entre le 11 et le 25"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées entre le 11 et le 25, le assert permet de vérifier que l'utilisateur entre bien des dates entre le 11 et le 25.

c1_date=[elm for elm in c1_d if jourd<=int(elm[0][8:10])<=jourf]
c2_date=[elm for elm in c2_d if jourd<=int(elm[0][8:10])<=jourf]
c3_date=[elm for elm in c3_d if jourd<=int(elm[0][8:10])<=jourf]
c4_date=[elm for elm in c4_d if jourd<=int(elm[0][8:10])<=jourf]
c5_date=[elm for elm in c5_d if jourd<=int(elm[0][8:10])<=jourf]
c6_date=[elm for elm in c6_d if jourd<=int(elm[0][8:10])<=jourf]





def date_convertie(L):
    n=len(L)
    Lc=[]
    for i in range(n):
        j=j=int(L[i][0][8:10])-11#Récupération du jour. La référence prise est le 11 septembre, ce qui exlique le -11.
        h=int(L[i][0][11:13])#Récupération de l'heure
        m=int(L[i][0][14:16])#Récupération du nombre de minutes
        s=int(L[i][0][17:19])#Récupération du nombre de secondes
        conv=j*24*(60**2)+h*(60**2)+m*60+s#Date convertie en seconde avec comme référence (0s), pour le 11 septembre 2019 à 0h00
        Lc.append(conv)
    return Lc

temps_c1=date_convertie(c1_date)#Liste avec les dates de mesures converties en secondes.
temps_c2=date_convertie(c2_date)
temps_c3=date_convertie(c3_date)
temps_c4=date_convertie(c4_date)
temps_c5=date_convertie(c5_date)
temps_c6=date_convertie(c6_date)



#Données en fonction de cette nouvelle plage de temps
ind_d1,ind_f1=int(c1_d.index(c1_date[0])),int(c1_d.index(c1_date[-1]))#Récupération des indices des dates compris dans les dates demandées, afin que la liste de temps et celle de données soient de même taille.
ind_d2,ind_f2=int(c2_d.index(c2_date[0])),int(c2_d.index(c2_date[-1]))
ind_d3,ind_f3=int(c3_d.index(c3_date[0])),int(c3_d.index(c3_date[-1]))
ind_d4,ind_f4=int(c4_d.index(c4_date[0])),int(c4_d.index(c4_date[-1]))
ind_d5,ind_f5=int(c5_d.index(c5_date[0])),int(c5_d.index(c5_date[-1]))
ind_d6,ind_f6=int(c6_d.index(c6_date[0])),int(c6_d.index(c6_date[-1]))


c1_noise=c1_n[ind_d1:ind_f1+1]#Liste ne comprenant que les données dans les dates demandées.
c1_temp=c1_t[ind_d1:ind_f1+1]
c1_humidity=c1_h[ind_d1:ind_f1+1]
c1_lum=c1_l[ind_d1:ind_f1+1]
c1_co2=c1_c[ind_d1:ind_f1+1]

c2_noise=c2_n[ind_d2:ind_f2+1]
c2_temp=c2_t[ind_d2:ind_f2+1]
c2_humidity=c2_h[ind_d2:ind_f2+1]
c2_lum=c2_l[ind_d2:ind_f2+1]
c2_co2=c2_c[ind_d2:ind_f2+1]

c3_noise=c3_n[ind_d3:ind_f3+1]
c3_temp=c3_t[ind_d3:ind_f3+1]
c3_humidity=c3_h[ind_d3:ind_f3+1]
c3_lum=c3_l[ind_d3:ind_f3+1]
c3_co2=c3_c[ind_d3:ind_f3+1]

c4_noise=c4_n[ind_d4:ind_f4+1]
c4_temp=c4_t[ind_d4:ind_f4+1]
c4_humidity=c4_h[ind_d4:ind_f4+1]
c4_lum=c4_l[ind_d4:ind_f4+1]
c4_co2=c4_c[ind_d4:ind_f4+1]

c5_noise=c5_n[ind_d5:ind_f5+1]
c5_temp=c5_t[ind_d5:ind_f5+1]
c5_humidity=c5_h[ind_d5:ind_f5+1]
c5_lum=c5_l[ind_d5:ind_f5+1]
c5_co2=c5_c[ind_d5:ind_f5+1]

c6_noise=c6_n[ind_d6:ind_f6+1]
c6_temp=c6_t[ind_d6:ind_f6+1]
c6_humidity=c6_h[ind_d6:ind_f6+1]
c6_lum=c6_l[ind_d6:ind_f6+1]
c6_co2=c6_c[ind_d6:ind_f6+1]

base_temps=[x*60 for x in range(0,20940,45)]

#Moyenne
def moyenne(L1):
    moy=0
    for elm in L1:
        moy+=elm
    return moy/len(L1)
    

def similarites(L1,L1_t,L2,L2_t,base_temps):
    D=[]
    n=len(base_temps)
    for i in range(1,n+1):
        l1=[]
        l2=[]
        D=[]
        for x in L1_t:
            if base_temps[i-1]<=x<base_temps[i]:
                j=L1_t.index(x)
                l1.append(L1[j])
        for y in L2_t:
            if base_temps[i-1]<=y<base_temps[i]:
                z=L2_t.index(y)
                l2.append(L2[z])
        if len(l1)!=0 and len(l2)!=0:
            d=abs(moyenne(l1)-moyenne(l2))
            D.append(d)
    return D

print(similarites(c2_noise,temps_c2,c3_noise,temps_c3,base_temps))
        


    



