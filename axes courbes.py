#
n=jourf-jourd+1 #n correspond au nombre de jours demandés

axes = plt.gca()
plt.plot(temps_c1,c1_lum,color='green',label='c1')
plt.plot(temps_c2,c2_lum,color='orange',label='c2')
plt.plot(temps_c3,c3_lum,color='purple',label='c3')
plt.plot(temps_c4,c4_lum,color='blue',label='c4')
plt.plot(temps_c5,c5_lum,color='red',label='c5')
plt.plot(temps_c6,c6_lum,color='yellow',label='c6')
plt.legend()
plt.xticks([86400*i for i in range (n)]) # 86400=le nombre de secondes dans une journée, pour qu'il y ait une graduation par jour
plt.xticks(rotation = 'vertical',fontsize = 8)
plt.show()


#Programme qui donne une liste des jours
def jours(L):
    M=[]
    l=len(L)
    for i in range (l):
        M.append(L[i][0][8:10])
    c1_j=[]
    for x in M:
        if x not in c1_j:
            c1_j.append(x)
    print(c1_j)



##BROUILLON


axes.xaxis.set_ticks(range(15))
axes.xaxis.set_ticklabels([], rotation = 90,, fontsize = 8, style = 'italic',)