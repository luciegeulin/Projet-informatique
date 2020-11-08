

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:11:41 2020

@author: Utilisateur
"""
from math import log
from math import exp,sqrt
import matplotlib.pyplot as plt
import numpy as np



f=open('Données_california2.txt','r')

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
    if int(donnees[i][1])==1:#Récupération des données seulement du capteur 1.
        c1.append(donnees[i])
    elif int(donnees[i][1])==2:
        c2.append(donnees[i])
    elif int(donnees[i][1])==3:
        c3.append(donnees[i])
    elif int(donnees[i][1])==4:
        c4.append(donnees[i])
    elif int(donnees[i][1])==5:
        c5.append(donnees[i])
    elif int(donnees[i][1])==6:
        c6.append(donnees[i])

#Données capteur1       
c1_n=[float(x[2]) for x in c1]#Récupération de la première colonne des données du capteur 1, ici, le bruit. 
c1_t=[float(x[3]) for x in c1]#Récupération de la température du capteur 1.
c1_h=[float(x[4]) for x in c1]#Récupération de l'humidité du capteur 1.
c1_l=[float(x[5]) for x in c1]#Récupération de la lumière du capteur 1.
c1_c=[float(x[6]) for x in c1]#Récupération du CO2 du capteur 1.
c1_d=[x[7].strip().split('\n')for x in c1]#Suppression de '\n' 
c1_d=[x[0][:19]for x in c1_d]#Suppression de '+00:20'


#Données capteur2
c2_n=[float(x[2]) for x in c2]
c2_t=[float(x[3]) for x in c2]
c2_h=[float(x[4]) for x in c2]
c2_l=[float(x[5]) for x in c2]
c2_c=[float(x[6]) for x in c2]
c2_d=[x[7].strip().split('\n')for x in c2]
c2_d=[x[0][:19]for x in c2_d]

#Données capteur3
c3_n=[float(x[1]) for x in c3]
c3_t=[float(x[2]) for x in c3]
c3_h=[float(x[3]) for x in c3]
c3_l=[float(x[4]) for x in c3]
c3_c=[float(x[5]) for x in c3]
c3_d=[x[7].strip().split('\n')for x in c3]
c3_d=[x[0][:19]for x in c3_d]

#Données capteur 4
c4_n=[float(x[1]) for x in c4]
c4_t=[float(x[2]) for x in c4]
c4_h=[float(x[3]) for x in c4]
c4_l=[float(x[4]) for x in c4]
c4_c=[float(x[5]) for x in c4]
c4_d=[x[7].strip().split('\n')for x in c4]
c4_d=[x[0][:19]for x in c4_d]


#Données capteur 5
c5_n=[float(x[1]) for x in c5]
c5_t=[float(x[2]) for x in c5]
c5_h=[float(x[3]) for x in c5]
c5_l=[float(x[4]) for x in c5]
c5_c=[float(x[5]) for x in c5]
c5_d=[x[7].strip().split('\n')for x in c5]
c5_d=[x[0][:19]for x in c5_d]


#Données capteur 6
c6_n=[float(x[1]) for x in c6]
c6_t=[float(x[2]) for x in c6]
c6_h=[float(x[3]) for x in c6]
c6_l=[float(x[4]) for x in c6]
c6_c=[float(x[5]) for x in c6]
c6_d=[x[7].strip().split('\n')for x in c6]
c6_d=[x[0][:19]for x in c6_d]


debut='2019-08-11'
fin='2019-08-14'



# ##Bonus: Spécifier un intervalle de temps
# debut=str(input('start_date:aaaa-mm-jj '))#Demande de la date de départ
# fin=str(input('end_date:aaaa-mm-jj '))#Demande de la date de fin



anneed=int(debut[:4])
moisd=int(debut[5:7])
jourd=int(debut[8:])#Récupération du jour de départ (Seule donnée utile par rapport à la référence car toutes les mesures sont faites au mois de septembre 2020)

anneef=int(fin[:4])
moisf=int(fin[5:7])
jourf=int(fin[8:])



assert anneed==2019 and anneef==2019, "Vous devez saisir l'année 2019"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées en 2020, le assert permet de vérifier que l'utilisateur entre bien l'année 2020
assert moisd==8 and moisf==8, "Vous devez saisir le mois d'août"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées en septembre, le assert permet de vérifier que l'utilisateur entre bien le mois de septembre.
assert  11<=jourd<=25 and 11<=jourf<=25, "La jour doit être compris entre le 11 et le 25"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées entre le 11 et le 25, le assert permet de vérifier que l'utilisateur entre bien des dates entre le 11 et le 25.

c1_date=[elm for elm in c1_d if jourd<=int(elm[8:10])<=jourf]
c2_date=[elm for elm in c2_d if jourd<=int(elm[8:10])<=jourf]
c3_date=[elm for elm in c3_d if jourd<=int(elm[8:10])<=jourf]
c4_date=[elm for elm in c4_d if jourd<=int(elm[8:10])<=jourf]
c5_date=[elm for elm in c5_d if jourd<=int(elm[8:10])<=jourf]
c6_date=[elm for elm in c6_d if jourd<=int(elm[8:10])<=jourf]



def date_convertie(L):
    n=len(L)
    Lc=[]
    for i in range(n):
        j=j=int(L[i][8:10])-11#Récupération du jour. La référence prise est le 11 septembre, ce qui exlique le -11.
        h=int(L[i][11:13])#Récupération de l'heure
        m=int(L[i][14:16])#Récupération du nombre de minutes
        s=int(L[i][17:19])#Récupération du nombre de secondes
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


### Fonctions demandées:
#Maximum
def maximum(L1):
    maxi=L1[0]
    for elm in L1:
        if elm>maxi:
            maxi=elm
    return maxi
#Minimum
def minimum(L1):
    mini=L1[0]
    for elm in L1:
        if elm<mini:
            mini=elm
    return mini

#Moyenne
def moyenne(L1):
    moy=0
    for elm in L1:
        moy+=elm
    return moy/len(L1)

#Variance
def variance(L1):
    moy=moyenne(L1)
    var=[(x-moy)**2 for x in L1]
    return moyenne(var)

#Ecart type
def ecart_type(L1):
    return (sqrt(variance(L1)))


#Courbe maximum
def courbe_max(x1,y1):
    ind,m=x1[y1.index(maximum(y1))],maximum(y1)
    plt.plot(ind,m,'ro',label='Maximum')
    plt.legend()

#Courbe minimum
def courbe_min(x1,y1):
    ind,m=x1[y1.index(minimum(y1))],minimum(y1)
    plt.plot(ind,m,'bo',label='Minimum')
    plt.legend()

#Courbe de la moyenne
def courbe_moy(y1):
    plt.axhline(y=moyenne(y1),color='red',label="Moyenne")
    plt.legend()

#Courbe de la variance
def courbe_variance(y1):
    plt.axhline(y=variance(y1),color='green', label='Variance')
    plt.legend()

#Courbe de l'écart-type
def courbe_ectype(y1):
    plt.axhline(y=ecart_type(y1),color='orange',linestyle='--',label='Ecart type')
    plt.legend()



#Médiane
#Organiser la série:
def insertionSort(L):
    for i in range(1,len(L)):
        elm=L[i]
        j=i-1
        while j>=0 and elm<L[j]:
            L[j+1]=L[j]
            j-=1
            L[j+1]=elm
    return L

def mediane(L):
    Lt=insertionSort(L)
    taille=len(insertionSort(Lt))+1
    mediane=moyenne([Lt[int(taille/2)-1],Lt[int(taille/2)]])
    return mediane

#Courbe médiane
def courbe_mediane(L):
    plt.axhline(y=mediane(L),color='purple',label="Mediane")
    plt.legend()
## GRAPHIQUES 

n=jourf-jourd+1         #n correspond au nombre de jours demandés

### GRAPHIQUE NOISE
axes = plt.gca()
plt.plot(temps_c1,c1_noise,color='green',label='c1')
plt.plot(temps_c2,c2_noise,color='orange',label='c2')
plt.plot(temps_c3,c3_noise,color='purple',label='c3')
plt.plot(temps_c4,c4_noise,color='blue',label='c4')
plt.plot(temps_c5,c5_noise,color='red',label='c5')
plt.plot(temps_c6,c6_noise,color='yellow',label='c6')
plt.legend()
plt.xticks([86400*i for i in range (n)]) # On a ainsi une graduation toutes les 86400 secondes, donc tous les jours
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])  #On renomme des gradutations avec le numéro de jour correspondant
axes.set_xlabel('Jours du mois de septembre')
axes.set_ylabel('Niveau sonore en dBA')
plt.show()

### GRAPHIQUE TEMPERATURE
axes = plt.gca()
plt.plot(temps_c1,c1_temp,color='green',label='c1')
plt.plot(temps_c2,c2_temp,color='orange',label='c2')
plt.plot(temps_c3,c3_temp,color='purple',label='c3')
plt.plot(temps_c4,c4_temp,color='blue',label='c4')
plt.plot(temps_c5,c5_temp,color='red',label='c5')
plt.plot(temps_c6,c6_temp,color='yellow',label='c6')
plt.legend()
plt.xticks([86400*i for i in range (n)])
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])
axes.set_xlabel('Jours du mois de septembre')
axes.set_ylabel('Température en °C')
plt.show()

### GRAPHIQUE CO2
axes = plt.gca()
plt.plot(temps_c1,c1_co2,color='green',label='c1')
plt.plot(temps_c2,c2_co2,color='orange',label='c2')
plt.plot(temps_c3,c3_co2,color='purple',label='c3')
plt.plot(temps_c4,c4_co2,color='blue',label='c4')
plt.plot(temps_c5,c5_co2,color='red',label='c5')
plt.plot(temps_c6,c6_co2,color='yellow',label='c6')
plt.legend()
plt.xticks([86400*i for i in range (n)])
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])
axes.set_xlabel('Jours du mois de septembre')
axes.set_ylabel('Quantité de CO2 en ppm')
plt.show()

### GRAPHIQUE HUMIDITY
axes = plt.gca()
plt.plot(temps_c1,c1_humidity,color='green',label='c1')
plt.plot(temps_c2,c2_humidity,color='orange',label='c2')
plt.plot(temps_c3,c3_humidity,color='purple',label='c3')
plt.plot(temps_c4,c4_humidity,color='blue',label='c4')
plt.plot(temps_c5,c5_humidity,color='red',label='c5')
plt.plot(temps_c6,c6_humidity,color='yellow',label='c6')
plt.legend()
plt.xticks([86400*i for i in range (n)])
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])
axes.set_xlabel('Jours du mois de septembre')
axes.set_ylabel('Humidité relative en %')
plt.show()

###GRAPHIQUE LUM
axes = plt.gca()
plt.plot(temps_c1,c1_lum,color='green',label='c1')
plt.plot(temps_c2,c2_lum,color='orange',label='c2')
plt.plot(temps_c3,c3_lum,color='purple',label='c3')
plt.plot(temps_c4,c4_lum,color='blue',label='c4')
plt.plot(temps_c5,c5_lum,color='red',label='c5')
plt.plot(temps_c6,c6_lum,color='yellow',label='c6')
plt.legend()
plt.xticks([86400*i for i in range (n)])
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])
axes.set_xlabel('Jours du mois de septembre')
axes.set_ylabel('Luminosité en lux')
plt.show()


## HUMIDEX
a=17.27
b=237.7

#On a besoin de l'humidité relative pour le calcul de la température de rosée (je suis pas sûre que ça soit utile)
hum_pourc1=[x/100 for x in c1_humidity]
hum_pourc2=[x/100 for x in c2_humidity]
hum_pourc3=[x/100 for x in c3_humidity]
hum_pourc4=[x/100 for x in c4_humidity]
hum_pourc5=[x/100 for x in c5_humidity]
hum_pourc6=[x/100 for x in c6_humidity]

def alpha(T,h):
    alp=a*T/(b+T)+log(h)
    return alp


def Tros(T,h):
    return b*alpha(T,h)/(a-alpha(T,h))

def humidex(T,h):
    c=1/273.16-1/(273.16+Tros(T,h))
    hd=T+0.5555*(6.11*exp(5417.7530*c)-10)
    return hd


#Pour ces trois fonctions, l'humidité doit être comprise entre 0 et 1

# ##Coefficient de corrélation
# #Calcul de la covariance
# def cov(X,Y):
#     n=len(X)
#     s=0
#     mx=moyenne(X)
#     my=moyenne(Y)
#     for i in range (n):
#         s=s+(X[i]-mx)*(Y[i]-my)
#         cv=(1/n)*s
#     return cv

# #Calcul du coefficient de corrélation
# def cor(X,Y):
#     return cov(X,Y)/(ecart_type(X)*ecart_type(Y))


#Liste des données de chaque capteur avec le titre
cap1=[['c1_noise']+c1_noise,['c1_temp']+c1_temp,['c1_humidity']+c1_humidity,['c1_lum']+c1_lum,['c1_co2']+c1_co2]
cap2=[['c2_noise']+c2_noise,['c2_temp']+c2_temp,['c2_humidity']+c2_humidity,['c2_lum']+c2_lum,['c2_co2']+c2_co2]
cap3=[['c3_noise']+c3_noise,['c3_temp']+c3_temp,['c3_humidity']+c3_humidity,['c3_lum']+c3_lum,['c3_co2']+c3_co2]
cap4=[['c4_noise']+c4_noise,['c4_temp']+c4_temp,['c4_humidity']+c4_humidity,['c4_lum']+c4_lum,['c4_co2']+c4_co2]
cap5=[['c5_noise']+c5_noise,['c5_temp']+c5_temp,['c5_humidity']+c5_humidity,['c5_lum']+c5_lum,['c5_co2']+c5_co2]
cap6=[['c6_noise']+c6_noise,['c6_temp']+c6_temp,['c6_humidity']+c6_humidity,['c6_lum']+c6_lum,['c6_co2']+c6_co2]

base_temps=[x*60 for x in range(0,20940,45)]

def similarites(L1,L1_t,L2,L2_t,base_temps):
    D=[]
    n=len(base_temps)
    for i in range(1,n):#Indice parcourant la liste des temps
        l1=[]
        l2=[]
        for x in L1_t:#On parcourt les temps de L1_t
            if base_temps[i-1]<=x<base_temps[i]:#Détermination des valeurs comprises dans un intervalle de 45 minutes.
                j=L1_t.index(x)#Détermination des indices des éléments compris dans cet intervalle.
                l1.append(L1[j])#Liste contenant les valeurs de la caractérique en question dans l'intervalle de temps de 45 minutes.
        for y in L2_t:#Idem mais dans la seconde liste
            if base_temps[i-1]<=y<base_temps[i]:
                z=L2_t.index(y)
                l2.append(L2[z])
        if len(l1)!=0 and len(l2)!=0:
            d=abs(moyenne(l1)-moyenne(l2))#Calcul de la distance
            D.append(d)
    return D

print(similarites(c1_noise,temps_c1,c3_noise,temps_c3,base_temps))
        
## Détermination automatique des horaires d'occupation des bureaux

# Etude sur un seul capteur
def horaires (liste_luminosité, liste_dates):#Préciser la liste de date à mettre dans la fonction
    l=len(liste_luminosité)
    occupe=[]
    for i in range(0,l):
        if liste_luminosité[i]>150: #correspond à un seuil choisi que nous avons choisi
            occupe.append(liste_dates[i][0][11:19])
    return occupe

