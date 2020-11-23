

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:11:41 2020

@author: Utilisateur
"""

from math import exp,sqrt,log
import matplotlib.pyplot as plt


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
c1_n=[float(x[2]) for x in c1]                 #Récupération de la première colonne des données du capteur 1, ici, le bruit.
c1_t=[float(x[3]) for x in c1]                 #Récupération de la température du capteur 1.
c1_h=[float(x[4]) for x in c1]                 #Récupération de l'humidité du capteur 1.
c1_l=[float(x[5]) for x in c1]                 #Récupération de la lumière du capteur 1.
c1_c=[float(x[6]) for x in c1]                 #Récupération du CO2 du capteur 1.
c1_d=[x[7].strip().split('\n')for x in c1]     #Suppression de '\n'
c1_d=[x[0][:19]for x in c1_d]                  #Suppression de '+00:20'


#Données capteur2
c2_n=[float(x[2]) for x in c2]
c2_t=[float(x[3]) for x in c2]
c2_h=[float(x[4]) for x in c2]
c2_l=[float(x[5]) for x in c2]
c2_c=[float(x[6]) for x in c2]
c2_d=[x[7].strip().split('\n')for x in c2]
c2_d=[x[0][:19]for x in c2_d]

#Données capteur3
c3_n=[float(x[2]) for x in c3]
c3_t=[float(x[3]) for x in c3]
c3_h=[float(x[4]) for x in c3]
c3_l=[float(x[5]) for x in c3]
c3_c=[float(x[6]) for x in c3]
c3_d=[x[7].strip().split('\n')for x in c3]
c3_d=[x[0][:19]for x in c3_d]

#Données capteur 4
c4_n=[float(x[2]) for x in c4]
c4_t=[float(x[3]) for x in c4]
c4_h=[float(x[4]) for x in c4]
c4_l=[float(x[5]) for x in c4]
c4_c=[float(x[6]) for x in c4]
c4_d=[x[7].strip().split('\n')for x in c4]
c4_d=[x[0][:19]for x in c4_d]


#Données capteur 5
c5_n=[float(x[2]) for x in c5]
c5_t=[float(x[3]) for x in c5]
c5_h=[float(x[4]) for x in c5]
c5_l=[float(x[5]) for x in c5]
c5_c=[float(x[6]) for x in c5]
c5_d=[x[7].strip().split('\n')for x in c5]
c5_d=[x[0][:19]for x in c5_d]


#Données capteur 6
c6_n=[float(x[2]) for x in c6]
c6_t=[float(x[3]) for x in c6]
c6_h=[float(x[4]) for x in c6]
c6_l=[float(x[5]) for x in c6]
c6_c=[float(x[6]) for x in c6]
c6_d=[x[7].strip().split('\n')for x in c6]
c6_d=[x[0][:19]for x in c6_d]





##Bonus: Spécifier un intervalle de temps

print('Appuyez sur "ENTER" pour un intervalle par défaut ou entrez les valeurs souhaitées.')

def my_input_start_date(prompt,default='2019-08-11 '):#Demande de la date de départ
    return input (prompt) or default
debut=my_input_start_date('start_date=aaaa-mm-jj ')



def my_input_end_date(prompt,default='2019-08-25 '):#Demande de la date de fin
    return input (prompt) or default
fin=my_input_end_date('end_date=aaaa-mm-jj ')






anneed=int(debut[:4])
moisd=int(debut[5:7])
jourd=int(debut[8:])        #Récupération du jour de départ (Seule donnée utile par rapport à la référence car toutes les mesures sont faites au mois d'août 2019)

anneef=int(fin[:4])
moisf=int(fin[5:7])
jourf=int(fin[8:])



assert anneed==2019 and anneef==2019, "Vous devez saisir l'année 2019"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées en 2019, le assert permet de vérifier que l'utilisateur entre bien l'année 2019
assert moisd==8 and moisf==8, "Vous devez saisir le mois d'août"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées en août, le assert permet de vérifier que l'utilisateur entre bien le mois d'août.
assert  11<=jourd<=25 and 11<=jourf<=25, "La jour doit être compris entre le 11 et le 25"#D'après les dates de mesures des capteurs,toutes les mesures sont réalisées entre le 11 et le 25, le assert permet de vérifier que l'utilisateur entre bien des dates entre le 11 et le 25.

c1_date=[elm for elm in c1_d if jourd<=int(elm[8:10])<=jourf]
c2_date=[elm for elm in c2_d if jourd<=int(elm[8:10])<=jourf]
c3_date=[elm for elm in c3_d if jourd<=int(elm[8:10])<=jourf]
c4_date=[elm for elm in c4_d if jourd<=int(elm[8:10])<=jourf]
c5_date=[elm for elm in c5_d if jourd<=int(elm[8:10])<=jourf]
c6_date=[elm for elm in c6_d if jourd<=int(elm[8:10])<=jourf]




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



def date_convertie(L):
    n=len(L)
    Lc=[]
    for i in range(n):
        j=int(L[i][8:10])-11                  #Récupération du jour. La référence prise est le 11 août, ce qui exlique le -11.
        h=int(L[i][11:13])                      #Récupération de l'heure
        m=int(L[i][14:16])                      #Récupération du nombre de minutes
        s=int(L[i][17:19])                      #Récupération du nombre de secondes
        conv=j*24*(60**2)+h*(60**2)+m*60+s      #Date convertie en seconde avec comme référence (0s), pour le 11 août 2019 à 0h00
        Lc.append(conv)
    return Lc

temps_c1=date_convertie(c1_date)                #Liste avec les dates de mesures converties en secondes.
temps_c2=date_convertie(c2_date)
temps_c3=date_convertie(c3_date)
temps_c4=date_convertie(c4_date)
temps_c5=date_convertie(c5_date)
temps_c6=date_convertie(c6_date)


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

##
#Courbe maximum
def courbe_max1(L_t,L):
    ind,m=L_t[L.index(maximum(L))],maximum(L)
    plt.plot(ind,m,'go')
    plt.legend()
def courbe_max2(L_t,L):
    ind,m=L_t[L.index(maximum(L))],maximum(L)
    plt.plot(ind,m,'o', color='orange')
    plt.legend()
def courbe_max3(L_t,L):
    ind,m=L_t[L.index(maximum(L))],maximum(L)
    plt.plot(ind,m,'o', color='purple')
    plt.legend()
def courbe_max4(L_t,L):
    ind,m=L_t[L.index(maximum(L))],maximum(L)
    plt.plot(ind,m,'bo', label='maximum')
    plt.legend()
def courbe_max5(L_t,L):
    ind,m=L_t[L.index(maximum(L))],maximum(L)
    plt.plot(ind,m,'ro')
    plt.legend()
def courbe_max6(L_t,L):
    ind,m=L_t[L.index(maximum(L))],maximum(L)
    plt.plot(ind,m,'yo')
    plt.legend()

#Courbe minimum
def courbe_min1(x1,y1):
    ind,m=x1[y1.index(minimum(y1))],minimum(y1)
    plt.plot(ind,m,'go',label='minimum')
    plt.legend()
def courbe_min2(x1,y1):
    ind,m=x1[y1.index(minimum(y1))],minimum(y1)
    plt.plot(ind,m,'o', color='orange')
    plt.legend()
def courbe_min3(x1,y1):
    ind,m=x1[y1.index(minimum(y1))],minimum(y1)
    plt.plot(ind,m,'o', color='purple')
    plt.legend()
def courbe_min4(x1,y1):
    ind,m=x1[y1.index(minimum(y1))],minimum(y1)
    plt.plot(ind,m,'bo')
    plt.legend()
def courbe_min5(x1,y1):
    ind,m=x1[y1.index(minimum(y1))],minimum(y1)
    plt.plot(ind,m,'ro')
    plt.legend()
def courbe_min6(x1,y1):
    ind,m=x1[y1.index(minimum(y1))],minimum(y1)
    plt.plot(ind,m,'yo')
    plt.legend()

#Courbe de la moyenne
def courbe_moy(y1):
    plt.axhline(y=moyenne(y1),color='red',label="Moyenne")
    plt.legend()
    plt.show()




n=jourf-jourd+1

## GRAPHIQUES


### GRAPHIQUE NOISE
axes = plt.gca()
plt.plot(temps_c1,c1_noise,color='green',label='c1')
plt.plot(temps_c2,c2_noise,color='orange',label='c2')
plt.plot(temps_c3,c3_noise,color='purple',label='c3')
plt.plot(temps_c4,c4_noise,color='blue',label='c4')
plt.plot(temps_c5,c5_noise,color='red',label='c5')
plt.plot(temps_c6,c6_noise,color='yellow',label='c6')
plt.plot(temps_c1,[moyenne(c1_noise)]*len(temps_c1),color='green', label='moyenne')
plt.plot(temps_c2,[moyenne(c2_noise)]*len(temps_c2),color='orange')
plt.plot(temps_c3,[moyenne(c3_noise)]*len(temps_c3),color='purple')
plt.plot(temps_c4,[moyenne(c4_noise)]*len(temps_c4),color='blue')
plt.plot(temps_c5,[moyenne(c5_noise)]*len(temps_c5),color='red')
plt.plot(temps_c6,[moyenne(c6_noise)]*len(temps_c6),color='yellow')
courbe_min1(temps_c1,c1_noise)
courbe_min2(temps_c2,c2_noise)
courbe_min3(temps_c3,c3_noise)
courbe_min4(temps_c4,c4_noise)
courbe_min5(temps_c5,c5_noise)
courbe_min6(temps_c6,c6_noise)
courbe_max1(temps_c1,c1_noise)
courbe_max2(temps_c2,c2_noise)
courbe_max3(temps_c3,c3_noise)
courbe_max4(temps_c4,c4_noise)
courbe_max5(temps_c5,c5_noise)
courbe_max6(temps_c6,c6_noise)
plt.legend()
plt.xticks([86400*i for i in range (n)])                        # On a ainsi une graduation toutes les 86400 secondes, donc tous les jours
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])          #On renomme des graduations avec le numéro de jour correspondant
axes.set_xlabel("Jours du mois d'août")
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
plt.plot(temps_c1,[moyenne(c1_temp)]*len(temps_c1),color='green', label='moyenne')
plt.plot(temps_c2,[moyenne(c2_temp)]*len(temps_c2),color='orange')
plt.plot(temps_c3,[moyenne(c3_temp)]*len(temps_c3),color='purple')
plt.plot(temps_c4,[moyenne(c4_temp)]*len(temps_c4),color='blue')
plt.plot(temps_c5,[moyenne(c5_temp)]*len(temps_c5),color='red')
plt.plot(temps_c6,[moyenne(c6_temp)]*len(temps_c6),color='yellow')
courbe_min1(temps_c1,c1_temp)
courbe_min2(temps_c2,c2_temp)
courbe_min3(temps_c3,c3_temp)
courbe_min4(temps_c4,c4_temp)
courbe_min5(temps_c5,c5_temp)
courbe_min6(temps_c6,c6_temp)
courbe_max1(temps_c1,c1_temp)
courbe_max2(temps_c2,c2_temp)
courbe_max3(temps_c3,c3_temp)
courbe_max4(temps_c4,c4_temp)
courbe_max5(temps_c5,c5_temp)
courbe_max6(temps_c6,c6_temp)
plt.legend()
plt.xticks([86400*i for i in range (n)])
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])
axes.set_xlabel("Jours du mois d'août")
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
plt.plot(temps_c1,[moyenne(c1_co2)]*len(temps_c1),color='green', label='moyenne')
plt.plot(temps_c2,[moyenne(c2_co2)]*len(temps_c2),color='orange')
plt.plot(temps_c3,[moyenne(c3_co2)]*len(temps_c3),color='purple')
plt.plot(temps_c4,[moyenne(c4_co2)]*len(temps_c4),color='blue')
plt.plot(temps_c5,[moyenne(c5_co2)]*len(temps_c5),color='red')
plt.plot(temps_c6,[moyenne(c6_co2)]*len(temps_c6),color='yellow')
courbe_min1(temps_c1,c1_co2)
courbe_min2(temps_c2,c2_co2)
courbe_min3(temps_c3,c3_co2)
courbe_min4(temps_c4,c4_co2)
courbe_min5(temps_c5,c5_co2)
courbe_min6(temps_c6,c6_co2)
courbe_max1(temps_c1,c1_co2)
courbe_max2(temps_c2,c2_co2)
courbe_max3(temps_c3,c3_co2)
courbe_max4(temps_c4,c4_co2)
courbe_max5(temps_c5,c5_co2)
courbe_max6(temps_c6,c6_co2)
plt.legend()
plt.xticks([86400*i for i in range (n)])
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])
axes.set_xlabel("Jours du mois d'août")
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
plt.plot(temps_c1,[moyenne(c1_humidity)]*len(temps_c1),color='green', label='moyenne')
plt.plot(temps_c2,[moyenne(c2_humidity)]*len(temps_c2),color='orange')
plt.plot(temps_c3,[moyenne(c3_humidity)]*len(temps_c3),color='purple')
plt.plot(temps_c4,[moyenne(c4_humidity)]*len(temps_c4),color='blue')
plt.plot(temps_c5,[moyenne(c5_humidity)]*len(temps_c5),color='red')
plt.plot(temps_c6,[moyenne(c6_humidity)]*len(temps_c6),color='yellow')
courbe_min1(temps_c1,c1_humidity)
courbe_min2(temps_c2,c2_humidity)
courbe_min3(temps_c3,c3_humidity)
courbe_min4(temps_c4,c4_humidity)
courbe_min5(temps_c5,c5_humidity)
courbe_min6(temps_c6,c6_humidity)
courbe_max1(temps_c1,c1_humidity)
courbe_max2(temps_c2,c2_humidity)
courbe_max3(temps_c3,c3_humidity)
courbe_max4(temps_c4,c4_humidity)
courbe_max5(temps_c5,c5_humidity)
courbe_max6(temps_c6,c6_humidity)
plt.legend()
plt.xticks([86400*i for i in range (n)])
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])
axes.set_xlabel("Jours du mois d'août")
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
plt.plot(temps_c1,[moyenne(c1_lum)]*len(temps_c1),color='green', label='moyenne')
plt.plot(temps_c2,[moyenne(c2_lum)]*len(temps_c2),color='orange')
plt.plot(temps_c3,[moyenne(c3_lum)]*len(temps_c3),color='purple')
plt.plot(temps_c4,[moyenne(c4_lum)]*len(temps_c4),color='blue')
plt.plot(temps_c5,[moyenne(c5_lum)]*len(temps_c5),color='red')
plt.plot(temps_c6,[moyenne(c6_lum)]*len(temps_c6),color='yellow')
courbe_min1(temps_c1,c1_lum)
courbe_min2(temps_c2,c2_lum)
courbe_min3(temps_c3,c3_lum)
courbe_min4(temps_c4,c4_lum)
courbe_min5(temps_c5,c5_lum)
courbe_min6(temps_c6,c6_lum)
courbe_max1(temps_c1,c1_lum)
courbe_max2(temps_c2,c2_lum)
courbe_max3(temps_c3,c3_lum)
courbe_max4(temps_c4,c4_lum)
courbe_max5(temps_c5,c5_lum)
courbe_max6(temps_c6,c6_lum)
plt.legend()
plt.xticks([86400*i for i in range (n)])
axes.xaxis.set_ticklabels([jourd+i for i in range(n)])
axes.set_xlabel("Jours du mois d'août")
axes.set_ylabel('Luminosité en lux')
plt.show()



#Liste des données de chaque capteur avec le titre
cap1=[['c1_noise']+c1_noise,['c1_temp']+c1_temp,['c1_humidity']+c1_humidity,['c1_lum']+c1_lum,['c1_co2']+c1_co2]
cap2=[['c2_noise']+c2_noise,['c2_temp']+c2_temp,['c2_humidity']+c2_humidity,['c2_lum']+c2_lum,['c2_co2']+c2_co2]
cap3=[['c3_noise']+c3_noise,['c3_temp']+c3_temp,['c3_humidity']+c3_humidity,['c3_lum']+c3_lum,['c3_co2']+c3_co2]
cap4=[['c4_noise']+c4_noise,['c4_temp']+c4_temp,['c4_humidity']+c4_humidity,['c4_lum']+c4_lum,['c4_co2']+c4_co2]
cap5=[['c5_noise']+c5_noise,['c5_temp']+c5_temp,['c5_humidity']+c5_humidity,['c5_lum']+c5_lum,['c5_co2']+c5_co2]
cap6=[['c6_noise']+c6_noise,['c6_temp']+c6_temp,['c6_humidity']+c6_humidity,['c6_lum']+c6_lum,['c6_co2']+c6_co2]

base_temps=[x*60 for x in range(0,20940,60)]

noise=[c1_noise,c2_noise,c3_noise,c4_noise,c5_noise,c6_noise]
temperature=[c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp]
humidity=[c1_humidity,c2_humidity,c3_humidity,c4_humidity,c5_humidity,c6_humidity]
luminosity=[c1_lum,c2_lum,c3_lum,c4_lum,c5_lum,c6_lum]
co2=[c1_co2,c2_co2,c3_co2,c4_co2,c5_co2,c6_co2]


date=[c1_date,c2_date,c3_date,c4_date,c5_date,c6_date]

def distance(L1,l1_t,L2,l2_t,base_temps):
    L1_t=date_convertie(l1_t)
    L2_t=date_convertie(l2_t)
    D=[]
    #D_n=[]#Distance normalisée entre 0 et 1
    n=len(base_temps)
    for i in range(1,n):                                        #Indice parcourant la liste des temps
        l1=[]
        l2=[]
        for x in L1_t:                                          #On parcourt les temps de L1_t
            if base_temps[i-1]<=x<base_temps[i]:                #Détermination des valeurs comprises dans un intervalle de 45 minutes.
                j=L1_t.index(x)                                 #Détermination des indices des éléments compris dans cet intervalle.
                l1.append(L1[j])                                #Liste contenant les valeurs de la caractérique en question dans l'intervalle de temps de 45 minutes.
        for y in L2_t:                                          #Idem mais dans la seconde liste
            if base_temps[i-1]<=y<base_temps[i]:
                z=L2_t.index(y)
                l2.append(L2[z])
        if len(l1)==0 or len(l2)==0:
            D.append(None)
        else:
            d=abs(moyenne(l1)-moyenne(l2))                      #Calcul de la distance
            D.append(d)
    return D



caractéristiques=[noise,temperature,humidity,luminosity,co2]
s_capt_car=[]                               #Liste de liste comportant les distances normalisées des capteurs deux à deux pour chaque caractéristique
for c in caractéristiques:
    ##distances capteurs
    D_capteurs=[]
    taille_n=len(c)
    for i in range(taille_n):
        for j in range(i+1,taille_n):
            D_capteurs.append(distance(c[i],date[i],c[j],date[j],base_temps))

    taille_D=len(D_capteurs)                        #Comparaison entre tous les capteurs : 15 listes
    t=len(D_capteurs[0])                            #Nombre de mesures réalisées
    Lmini=[]
    Lmaxi=[]
    for i in range(t):                              #Parcourt les indices des distances entre deux capteurs
        mini=D_capteurs[0][i]
        maxi=D_capteurs[0][i]
        if mini==None:
            for k in range(taille_D-1):
                mini=D_capteurs[k+1][i]
        if maxi==None:
            for k in range(taille_D-1):
                maxi=D_capteurs[k+1][i]
        for j in range(taille_D):                   #Parcourt les indices de toutes les comparaisons entre les capteurs.
            if type(D_capteurs[j][i])==float:
                if D_capteurs[j][i]>maxi:
                    maxi=D_capteurs[j][i]
                if D_capteurs[j][i]<mini:
                    mini=D_capteurs[j][i]
        Lmini.append(mini)
        Lmaxi.append(maxi)


    ##Normalisation
    for x in D_capteurs:
        for i in range(t):
            if type(x[i])==float and (Lmaxi[i]-Lmini[i])!=0 :
                x[i]=(Lmaxi[i]-x[i])/(Lmaxi[i]-Lmini[i])
            else:
                x[i]=None


    ## Similairarités
    similaire_p=[]
    for z in D_capteurs:
        M=[]
        for u in range(t):
            if type(z[u])==float:
                M.append(z[u])
        similaire_p.append((moyenne(M))*100)
    s_capt_car.append(similaire_p)

print('\nSimilarités')
#Définition des seuils de similarités.
seuils=[80,65,70,70,85]
comparaison_capt=[['1', '2'],[ '1', '3'],['1', '4'],['1','5'],['1', '6'],['2', '3'],['2', '4'],['2', '5'],['2', '6'],['3', '4'],['3', '5'],['3', '5'],['3', '6'],['4', '5'],['5', '6']]
carac=['du bruit.','de la température.', "de l'humidité.", 'de la lumière.', "du co2."]
ns=len(seuils)
nc=len(comparaison_capt)

for i in range(ns):
    for j in range(nc):
        if s_capt_car[i][j]>=seuils[i]:
            print('Les capteurs {} et {} sont similaires vis à vis {}'.format(comparaison_capt[j][0],comparaison_capt[j][1],carac[i]))



## Détermination automatique des horaires d'occupation des bureaux

def bruit_jour(L1, L1_t):                           #Sépare la liste des bruits par jours
    L_indj=[0]                                      #Future liste comportant les indices, lorsque la liste des temps change de jour.
    noise_jour=[]                                   #Future liste de liste séparée par jour
    a=jourd                                         #Jour de départ
    for x in L1_t:                                  #Boucle sur la liste des dates.
        if int(x[8:11])==a:                         #Condition déterminant si le jour est le même que le précédent
            a=int(x[8:11])                          #a prend la nouvelle valeur du jour
        else:
            a=int(x[8:11])
            L_indj.append(L1_t.index(x))            #Si la date du jour est différente de la date précédente, on ajoute son indice dans la liste.
    L_indj.append(len(L1))                          #On ajoute le dernier indice de la liste des temps
    for i in range(len(L_indj)-1):
        i_d=L_indj[i]
        i_f=L_indj[i+1]
        noise_jour.append(L1[i_d:i_f])              #A l'aide de la liste des indices, on sépare la liste L1 suivant les différents jours.
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
    j=int(L_date[0][8:10])              #on récupère le premier jour
    n=len(M)                            #on récupère le nombre de jours
    for i in range (n):
        if M[i]>29.5:
            semaine.append(j)
        else :
            week_end.append(j)
        j=j+1
    return week_end, semaine

nw=len(weekend(c1_noise,c1_date)[0])
ns=len(weekend(c1_noise,c1_date)[1])

print ('\nJours de la semaine')

for i in range(0,nw,2):
    print('Le {} et {} août tombent un weekend.'.format(weekend(c1_noise, c1_date)[0][i],weekend(c1_noise, c1_date)[0][i+1]))

for i in range(0,ns,5):
    print('Le {} août tombent en semaine.'.format(weekend(c1_noise, c1_date)[1][i:i+5]))

print('\nOuverture des bureaux')

def occupation_bu(L1_lum,L1_d):
    L=[]                                        #Tous les indices lorsque les bureaux sont allumés
    n=len(L1_lum)
    occ_bureaux=[]
    for i in range(n):
        if L1_lum[i]>=150:
            L.append(i)                         #Liste comportant les indices tq la valeur de luminosité soit supérieur au seuil.
    for x in L:
        occ_bureaux.append(L1_d[x])             #Liste de toutes les dates où les bureaux sont allumés.
    #Ne récupère que les dates de début et de fin.
    Lj=[]                                       #Liste prenant les jours d'ouverture des bureaux
    for x in occ_bureaux:
        if int(x[8:10]) not in Lj:
            Lj.append(int(x[8:10]))

    occ_deb_fin=[]                              #Liste de comportant que deux dates par jour : celle de début et de fin d'ouverture des bureaux.
    for x in Lj:
        L_date=[]
        for i in range(len(occ_bureaux)):
            if int(occ_bureaux[i][8:10])==x:
                L_date.append(occ_bureaux[i])#Récupération dans une liste de toutes les dates d'un même jour (car la luminosité peut baisser au cours de la journée)
        occ_deb_fin.append(L_date[0][8:])           #Récupération de l'heure la plus tôt
        occ_deb_fin.append(L_date[-1][8:])          #Récupération de l'heure la plus tardive
    return(occ_deb_fin)



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


occ_bur=horaire_semaine(c1_lum,c1_date,c1_noise)
for i in range(0,len(occ_bur)-1,2):
    print('Les bureaux étaient ouverts de {} à {} le {} août 2019.'.format(occ_bur[i][3:8],occ_bur[i+1][3:8], occ_bur[i][0:2]))

