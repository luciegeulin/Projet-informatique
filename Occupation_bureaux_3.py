# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:12:42 2020

@author: mario
"""

def occupation_bu(L1,L1_t):
    L=[]                                        #Liste contenant les indices des moments pour lesquels les bureaux sont occupés
    n=len(L1)
    Occ_bureaux=[]
    for i in range(n):
        if L1[i]>= 150:
            L.append(i)                         #Liste comportant les indices tels que la luminosité soit supérieure au seuil
    n1=len(L)
    L_ind=[]                                    #Liste comportant les indices de début et de fin d'occupation (par rapport au seuil de 150)
    if L1[0]>=150:                              #Si les bureaux sont occupés au début d'enregistrement du capteur
        L_ind.append(0)
    for j in range(n1-1) :
        if (L[j+1]-L[j])>1:                     #Vérifié lorsque L[j+1] et L[j] ne sont pas consécutifs, donc lorsqu'on est passé au dessus ou en dessous du seuil
            L_ind.append(L[j])                  #L'un correspond à l'indice de début ou de fin de journée et l'autre à l'indice de fin ou de début de journée
            L_ind.append(L[j+1])
    if L1[-1]>=150:                             #Si les bureaux sont occupés à la fin de l'enregistrement du capteur
        L_ind.append(n-1)
    for x in L_ind:
        Occ_bureaux.append(L1_t[x][8:])        #A l'aide des indices récupérés précédemment, on détermine les horaires d'occupation des bureaux par journée
    return Occ_bureaux


