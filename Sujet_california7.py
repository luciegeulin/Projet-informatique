

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:11:41 2020

@author: Utilisateur
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
c6_d=[x[6].strip().split('\n' and '+0200') for x in c6]
for x in c6_d :
    del x[1]










    
    



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
tps_c1=date_convertie(c1_date)#Liste avec les dates de mesures converties en secondes.
tps_c2=date_convertie(c6_date)
tps_c3=date_convertie(c3_date)
tps_c4=date_convertie(c4_date)
tps_c5=date_convertie(c5_date)
tps_c6=date_convertie(c6_date)

#Bonus: Spécifier un intervalle de temps
debut=str(input('start_date:aaaa-mm-jj '))#Demande de la date de départ
fin=str(input('end_date:aaaa-mm-jj '))#Demande de la date de fin
jd=debut[8:]#Récupération du jour de départ (Seule donnée utile par rapport à la référence car toutes les mesures sont faites au mois de septembre 2019)
jf=fin[8:]

c1_date=[elm for elm in c1_d if jourd<=int(elm[0][8:10])<=jourf]
c2_date=[elm for elm in c1_d if jourd<=int(elm[0][8:10])<=jourf]
c3_date=[elm for elm in c1_d if jourd<=int(elm[0][8:10])<=jourf]
c4_date=[elm for elm in c1_d if jourd<=int(elm[0][8:10])<=jourf]
c5_date=[elm for elm in c1_d if jourd<=int(elm[0][8:10])<=jourf]
c6_date=[elm for elm in c1_d if jourd<=int(elm[0][8:10])<=jourf]



anneed=int(debut[:4])
moisd=int(debut[5:7])
jourd=int(debut[8:])

anneef=int(fin[:4])
moisf=int(fin[5:7])
jourf=int(fin[8:])



assert anneed==2020 and anneef==2020, "Vous devez saisir l'année 2020"
assert moisd==9 and moisf==9, "Vous devez saisir le mois de septembre"
assert  11<=jourd<=25 and 11<=jourf<=25, "La jour doit être compris entre le 11 et le 25"

debut_s=(int(jd)-11)*24*(60**2)#La date est convertie en seconde, avec le 11 septembre toujours pris comme référence.
fin_s=(int(jf)-11)*24*(60**2)+23*(60**2)+59*60+59
#Nouvelles plages de temps
temps_c1=[elm for elm in tps_c1 if debut_s<=elm<=fin_s]#Recherche des mesures faites dans l'intervalles de dates demandées. Ce qui explique l'utilisation de la comparaison.
temps_c2=[elm for elm in tps_c2 if debut_s<=elm<=fin_s]
temps_c3=[elm for elm in tps_c3 if debut_s<=elm<=fin_s]
temps_c4=[elm for elm in tps_c4 if debut_s<=elm<=fin_s]
temps_c5=[elm for elm in tps_c5 if debut_s<=elm<=fin_s]
temps_c6=[elm for elm in tps_c6 if debut_s<=elm<=fin_s]

#Données en fonction de cette nouvelle plage de temps

ind_d1,ind_f1=int(tps_c1.index(temps_c1[0])),int(tps_c1.index(temps_c1[-1]))#Récupération des indices des dates compris dans les dates demandées, afin que la liste de temps et celle de données soient de même taille.
ind_d2,ind_f2=int(tps_c2.index(temps_c2[0])),int(tps_c2.index(temps_c2[-1]))
ind_d3,ind_f3=int(tps_c3.index(temps_c3[0])),int(tps_c3.index(temps_c3[-1]))
ind_d4,ind_f4=int(tps_c4.index(temps_c4[0])),int(tps_c4.index(temps_c4[-1]))
ind_d5,ind_f5=int(tps_c5.index(temps_c5[0])),int(tps_c5.index(temps_c5[-1]))
ind_d6,ind_f6=int(tps_c6.index(temps_c6[0])),int(tps_c6.index(temps_c6[-1]))
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


def courbe_moy(y1):
    plt.axhline(y=moyenne(y1),color='red',label="Moyenne")
    plt.legend()



def courbe_variance(y1):
    plt.axhline(y=variance(y1),color='green', label='Variance')
    plt.legend()


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





###CAPTEUR 1: GRAPHIQUE
plt.plot(temps_c1,c1_noise,color='green',label='noise')
plt.plot(temps_c1,c1_temp,color='orange',label='temperature')
plt.plot(temps_c1,c1_humidity,color='purple',label='humidity')
plt.plot(temps_c1,c1_lum,color='blue',label='luminosity')
plt.plot(temps_c1,c1_co2,color='red',label='CO2')
plt.legend()
plt.xlim(xmin=temps_c1[0],xmax=temps_c1[-1])



##CAPTEUR 2: GRAPHIQUE
plt.plot(temps_c2,c2_noise,color='green',label='noise')
plt.plot(temps_c2,c2_temp,color='orange',label='temperature')
plt.plot(temps_c2,c2_humidity,color='purple',label='humidity')
plt.plot(temps_c2,c2_lum,color='blue',label='luminosity')
plt.plot(temps_c2,c2_co2,color='red',label='CO2')
plt.legend()
plt.xlim(xmin=temps_c2[0],xmax=temps_c2[-1])

###CAPTEUR 3: GRAPHIQUE
plt.plot(temps_c3,c3_noise,color='green',label='noise')
plt.plot(temps_c3,c3_temp,color='orange',label='temperature')
plt.plot(temps_c3,c3_humidity,color='purple',label='humidity')
plt.plot(temps_c3,c3_lum,color='blue',label='luminosity')
plt.plot(temps_c3,c3_co2,color='red',label='CO2')
plt.legend()
plt.xlim(xmin=temps_c3[0],xmax=temps_c3[-1])

###CAPTEUR 4: GRAPHIQUE
plt.plot(temps_c4,c4_noise,color='green',label='noise')
plt.plot(temps_c4,c4_temp,color='orange',label='temperature')
plt.plot(temps_c4,c4_humidity,color='purple',label='humidity')
plt.plot(temps_c4,c4_lum,color='blue',label='luminosity')
plt.plot(temps_c4,c4_co2,color='red',label='CO2')
plt.legend()
plt.xlim(xmin=temps_c4[0],xmax=temps_c4[-1])
plt.show()

###CAPTEUR 5: GRAPHIQUE
plt.plot(temps_c5,c5_noise,color='green',label='noise')
plt.plot(temps_c5,c5_temp,color='orange',label='temperature')
plt.plot(temps_c5,c5_humidity,color='purple',label='humidity')
plt.plot(temps_c5,c5_lum,color='blue',label='luminosity')
plt.plot(temps_c5,c5_co2,color='red',label='CO2')
plt.legend()
plt.xlim(xmin=temps_c5[0],xmax=temps_c5[-1])


###CAPTEUR 6: GRAPHIQUE
plt.plot(temps_c6,c6_noise,color='green',label='noise')
plt.plot(temps_c6,c6_temp,color='orange',label='temperature')
plt.plot(temps_c6,c6_humidity,color='purple',label='humidity')
plt.plot(temps_c6,c6_lum,color='blue',label='luminosity')
plt.plot(temps_c6,c6_co2,color='red',label='CO2')
plt.legend()
plt.xlim(xmin=temps_c6[0],xmax=temps_c6[-1])


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



# def similarites(L1,L2):#Compare deux capteurs, et vérifie les similarités de ces derniers
#     n=len(L1)
#     for i in range(n):
#         #Moyenne
#         moy1=moyenne(L1[i][1:])
#         moy2=moyenne(L2[i][1:])
#         if 0.95*moy1<=moy2<=1.05*moy1:
#             print('{} et {} ont des similarités par rapport à la moyenne.'.format(L1[i][0],L2[i][0]))#Utilisation de l'outil format pour afficher les similarités.
    
#         #Variance 
#         var1=variance(L1[i][1:])
#         var2=variance(L2[i][1:])
#         if 0.95*var1<=var2<=1.05*var1:
#             print('{} et {} ont des similarités par rapport à la variance.'.format(L1[i][0],L2[i][0]))
        
#         #Ecart type
#         ecart_type1=ecart_type(L1[i][1:])
#         ecart_type2=ecart_type(L2[i][1:])
#         if 0.95*ecart_type1<=moy2<=1.05*ecart_type2:
#             print("{} et {} ont des similarités par rapport à l'écart type.".format(L1[i][0],L2[i][0]))
        
#         #Médiane
#         mediane1=mediane(L1[i][1:])
#         mediane2=mediane(L2[i][1:])
#         if 0.95*mediane1<=mediane2<=1.05*mediane1:
#             print('{} et {} ont des similarités par rapport à la mediane.'.format(L1[i][0],L2[i][0]))
       
#         #Corrélation
#         if (-0.5)<cor(L1[i][1:],L2[i][1:])<0.5:
#             return None
#         else:
#             print('{} et {} sont corrélés.'.format(L1[i][0],L2[i][0]))
# print(similarites(cap3,cap2))

# def similarites_humidex(L1,L2):
#     nom1=str(L1[0][0][:2])
#     nom2=str(L2[0][0][:2])
#     temp1=moyenne(L1[1][1:])
#     hum1=moyenne(L1[2][1:])/100
#     temp2=moyenne(L1[1][1:])
#     hum2=moyenne(L1[2][1:])/100
#     ind_humidex1=humidex(temp1,hum1)
#     ind_humidex2=humidex(temp2,hum2)
#     if 0.95*ind_humidex1<=ind_humidex2<=1.15*ind_humidex1:
#         print("{} et {} ont des similarités par rapport à l'indice humidex.".format(nom1,nom2))
        
## Détermination automatique des horaires d'occupation des bureaux

# Etude sur un seul capteur
def horaires (liste_luminosité, liste_dates):#Préciser la liste de date à mettre dans la fonction
    l=len(liste_luminosité)
    occupe=[]
    for i in range(0,l):
        if liste_luminosité[i]>150: #correspond à un seuil choisi que nous avons choisi
            occupe.append(liste_dates[i][0][11:19])
    return occupe
print(c6_date)