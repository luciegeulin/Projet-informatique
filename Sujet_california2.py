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
ligne=f.readlines()
n=len(ligne)
for i in range(1,n):
    L=ligne[i].split('\t')
    donnees.append(L)


#Récupération des données par capteurs
l=len(donnees)
c=len(donnees[1])
  
c1,c2,c3,c4,c5,c6=[],[],[],[],[],[]
for i in range(0,l):
    if int(donnees[i][0])==1:
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
c1_noise=[float(x[1]) for x in c1]
c1_temp=[float(x[2]) for x in c1]
c1_humidity=[float(x[3]) for x in c1]
c1_lum=[float(x[4]) for x in c1]
c1_co2=[float(x[5]) for x in c1]
c1_date=[x[6].strip().split('\n' and '+0200') for x in c1]
for x in c1_date :
    del x[1]



#Données capteur2
c2_noise=[float(x[1]) for x in c2]
c2_temp=[float(x[2]) for x in c2]
c2_humidity=[float(x[3]) for x in c2]
c2_lum=[float(x[4]) for x in c2]
c2_co2=[float(x[5]) for x in c2]
c2_date=[x[6].strip().split('\n' and '+0200') for x in c2]
for x in c2_date :
    del x[1]


#Données capteur3
c3_noise=[float(x[1]) for x in c3]
c3_temp=[float(x[2]) for x in c3]
c3_humidity=[float(x[3]) for x in c3]
c3_lum=[float(x[4]) for x in c3]
c3_co2=[float(x[5]) for x in c3]
c3_date=[x[6].strip().split('\n' and '+0200') for x in c3]
for x in c3_date :
    del x[1]

#
c4_noise=[float(x[1]) for x in c4]
c4_temp=[float(x[2]) for x in c4]
c4_humidity=[float(x[3]) for x in c4]
c4_lum=[float(x[4]) for x in c4]
c4_co2=[float(x[5]) for x in c4]
c4_date=[x[6].strip().split('\n' and '+0200') for x in c4]
for x in c4_date :
    del x[1]


#Données capteur 5
c5_noise=[float(x[1]) for x in c5]
c5_temp=[float(x[2]) for x in c5]
c5_humidity=[float(x[3]) for x in c5]
c5_lum=[float(x[4]) for x in c5]
c5_co2=[float(x[5]) for x in c5]
c5_date=[x[6].strip().split('\n' and '+0200') for x in c5]
for x in c5_date :
    del x[1]


#Données capteur 6
c6_noise=[float(x[1]) for x in c6]
c6_temp=[float(x[2]) for x in c6]
c6_humidity=[float(x[3]) for x in c6]
c6_lum=[float(x[4]) for x in c6]
c6_co2=[float(x[5]) for x in c6]
c6_date=[x[6].strip().split('\n' and '+0200') for x in c6]
for x in c6_date :
    del x[1]

##

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

##Convertir les dates

def date_convertie(L):
    n=len(L)
    Lc=[]
    for i in range(n):
        j=j=int(L[i][0][8:10])-11
        h=int(L[i][0][11:13])
        m=int(L[i][0][14:16])
        s=int(L[i][0][17:19])
        conv=j*24*(60**2)+h*(60**2)+m*60+s
        Lc.append(conv)
    return Lc

temps_c1=date_convertie(c1_date)
temps_c2=date_convertie(c6_date)
temps_c3=date_convertie(c3_date)
temps_c4=date_convertie(c4_date)
temps_c5=date_convertie(c5_date)
temps_c6=date_convertie(c6_date)

###CAPTEUR 1: GRAPHIQUE
plt.plot(temps_c1,c1_noise,color='green',label='noise')
plt.plot(temps_c1,c1_temp,color='orange',label='temperature')
plt.plot(temps_c1,c1_humidity,color='purple',label='humidity')
plt.plot(temps_c1,c1_lum,color='blue',label='luminosity')
plt.plot(temps_c1,c1_co2,color='red',label='CO2')
plt.legend()
plt.xlim(xmin=temps_c1[0],xmax=temps_c1[-1])
plt.show()


###CAPTEUR 2: GRAPHIQUE
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

##Coefficient de corrélation
#Calcul de la covariance
def cov(X,Y):
    n=len(X)
    s=0
    mx=moyenne(X)
    my=moyenne(Y)
    for i in range (n):
        s=s+(X[i]-mx)*(Y[i]-my)
        cv=(1/n)*s
    return cv

#Calcul du coefficient de corrélation
def cor(X,Y):
    return cov(X,Y)/(ecart_type(X)*ecart_type(Y))


#Liste des données de chaque capteur avec le titre
cap1=[['c1_noise']+c1_noise,['c1_temp']+c1_temp,['c1_humidity']+c1_humidity,['c1_lum']+c1_lum,['c1_co2']+c1_co2]
cap2=[['c2_noise']+c2_noise,['c2_temp']+c2_temp,['c2_humidity']+c2_humidity,['c2_lum']+c2_lum,['c2_co2']+c2_co2]
cap3=[['c3_noise']+c3_noise,['c3_temp']+c3_temp,['c3_humidity']+c3_humidity,['c3_lum']+c3_lum,['c3_co2']+c3_co2]
cap4=[['c4_noise']+c4_noise,['c4_temp']+c4_temp,['c4_humidity']+c4_humidity,['c4_lum']+c4_lum,['c4_co2']+c4_co2]
cap5=[['c5_noise']+c5_noise,['c5_temp']+c5_temp,['c5_humidity']+c5_humidity,['c5_lum']+c5_lum,['c5_co2']+c5_co2]
cap6=[['c6_noise']+c6_noise,['c6_temp']+c6_temp,['c6_humidity']+c6_humidity,['c6_lum']+c6_lum,['c6_co2']+c6_co2]



def similarites(L1,L2):
    n=len(L1)
    for i in range(n):
        #Moyenne
        moy1=moyenne(L1[i][1:])
        moy2=moyenne(L2[i][1:])
        if 0.95*moy1<=moy2<=1.05*moy1:
            print('{} et {} ont des similarités par rapport à la moyenne.'.format(L1[i][0],L2[i][0]))
    
        #Variance 
        var1=variance(L1[i][1:])
        var2=variance(L2[i][1:])
        if 0.95*var1<=var2<=1.05*var1:
            print('{} et {} ont des similarités par rapport à la variance.'.format(L1[i][0],L2[i][0]))
        
        #Ecart type
        ecart_type1=ecart_type(L1[i][1:])
        ecart_type2=ecart_type(L2[i][1:])
        if 0.95*ecart_type1<=moy2<=1.15*ecart_type2:
            print("{} et {} ont des similarités par rapport à l'écart type.".format(L1[i][0],L2[i][0]))
        
        #Médiane
        mediane1=mediane(L1[i][1:])
        mediane2=mediane(L2[i][1:])
        if 0.95*mediane1<=mediane2<=1.05*mediane1:
            print('{} et {} ont des similarités par rapport à la mediane.'.format(L1[i][0],L2[i][0]))
       
        #Corrélation
        if (-0.5)<cor(L1[i][1:],L2[i][1:])<0.5:
            return None
        else:
            print('{} et {} sont corrélés.'.format(L1[i][0],L2[i][0]))
print(similarites(cap3,cap2))

def similarites_humidex(L1,L2):
    nom1=str(L1[0][0][:2])
    nom2=str(L2[0][0][:2])
    temp1=moyenne(L1[1][1:])
    hum1=moyenne(L1[2][1:])/100
    temp2=moyenne(L1[1][1:])
    hum2=moyenne(L1[2][1:])/100
    ind_humidex1=humidex(temp1,hum1)
    ind_humidex2=humidex(temp2,hum2)
    if 0.95*ind_humidex1<=ind_humidex2<=1.05*ind_humidex1:
        print("{} et {} ont des similarités par rapport à l'indice humidex.".format(nom1,nom2))
        
print(similarites_humidex(cap3,cap2))