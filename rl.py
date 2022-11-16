# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:42:21 2022

@author: 22541
"""

import numpy as np
import pandas as pd 
donnees = pd.read_csv('TP1.csv')
donnees.head()
X1=donnees['X1']
X2=donnees['X2']
X3=donnees['X3']
Y=donnees['Y']
A=pd.DataFrame(np.c_[donnees['X1'],donnees['X2'],donnees['X3'],donnees['b']])
TA=np.transpose(A)
ATA=np.dot(TA,A)
I=np.linalg.inv(ATA)
ATY=np.dot(TA,Y)
Resultat=np.dot(I,ATY)
a1=Resultat[0]
a2=Resultat[1]
a3=Resultat[2]
b=Resultat[3]
for i,j in enumerate(Resultat):
    if (i==3):
        print("la valeur de b est:",j)
    else:
     print("la valeur de a"+str(i+1)+ " est:",j)
Y_prev=[]
for i in range (0,24):
    Y_prev.append (a1*X1[i]+a2*X2[i]+a3*X3[i]+b)
e=[]
for i in range (0,24):
    e.append (Y[i]-Y_prev[i])
scr=0
for i in e :
    scr=scr+e[int(i)]*e[int(i)]
var_Y= np.var(Y)
sct= 24*var_Y
sce=sct-scr
cmr= scr/20
cme=sce/3
fisher= (cme/cmr)

#TABLEAUANOVA
print ('                          ')
print ('                          ')
print ('                          ')
print ('                                 TABLEAU ANOVA            ')
print('---------------------------------------------------------------------------|')
print('         |      valeur             |     ddl   |     CM    |   Fisher      |')
print('---------|-------------------------|-----------|-----------|---------------|')
print("scr      |",scr,"      | n-p-1     |",cmr,"|",fisher,"|")
print('---------|-------------------------|-----------|-----------|---------------|')
print("sce      |",sce,"      |   P       |",cme," |               |")
print('---------|-------------------------|-----------|-----------|---------------|')
print("sct      |",sct,"     |   n-1     |           |               |")
print('---------|-------------------------|-----------|-----------|---------------|')

teststud=scr*I
print ("la valeur du test de student est",teststud)




















                                                   
