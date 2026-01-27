# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:09:21 2022

@author: Vazsa
"""
'''
#año 0
#T_p: Tamaño de pobblación
#t_n: tasa del año anterior 
#t_m: tasa de mortalidad 
#x=edad 
#t=tiempo en años
#2020=a0


T_p_x_t+1_=(t_n_x_t)*(t_m_x_t)

N_0_2021=Nacimientos
N_1_2021=N_0_2020*t_m_0_2020
N_2_2021=N_1_2020*t_m_1_2020

N_0_2022=Nacimientos
N_1_2022=N_0_2021*t_m_0_2021
N_2_2022=N_1_2021*t_m1_2021


Parametros de las dos funciones recursivas.

N(T) Población total respecto a cada X 
M(T) Población con AD siendo >65 (x>65)
tQx(T) Tasa de muerte de la población total 
Qx(T) Tasa de muerte de la poblaicón con AD
tPx(T) Tasa de supervicencia a partir de X edad de la población total
Px(T) Tasa de supervivencia de sujetos con AD de la población de AD
rx  Tasa de prevanlencia
K(T) Proproción de nuevos casos de AD en la población
a(X) coeficiente de muerte al año.  
b(x) es una parametro que los autores calcularon pero no dicen como, o de que forma y que significa 
su función es a(n-+1)+ 1 - a(n-i). Menos un año 
'''


import numpy as np
from math import e 

#Hacer código de regresión lineal para estimar la tasa de natalidad
#Código para estimar la tasa de supervivencia

def poblacion(x):
    #Va del año 0 (2020) al 59(2080)
    Tasa_natalidad_año=[]
    #Va del año 0 al 59 y como es por edad (se necesitan 101 listas dentro la lista )
    Tasa_supervivencia=[]
    # de la edad 0 a 100
    Población_por_edad_año_0=[]
    listas=[]
    listas.append(Tasa_natalidad_año)
    for i in range(x):
        tamaño_pob=np.multiply(listas[x-1], Tasa_supervivencia[x-1])
        tamaño_pob.insert(0,Población_por_edad_año_0[x])
        tamaño_pob.pop(61)
        listas.append(tamaño_pob)
        tamaño_pob.clear()
    #La idea es que listas sea una lista de listas donde
    #cada lista tenga el tamaño de la población de esa edad del año 0 al 60
    #en total habrá 101 listas, una por edad
    return listas
    
def poblacion_EA(poblacion_total):
    #Va del año 0(2020) al 59(2080)
    Población_65_años_con_EA=[]
    #Va del año 0 al 59_por edad (se necesitan 36 listas dentro la lista 65-100 años)
    Tasa_supervivencia_pob_EA=[]
    # de la edad 65 a 100
    Población_por_edad_año_0=[]
    for i in range(len(poblacion_total)):
        if i<65:
            poblacion_total.pop()
            
    return poblacion_total
    
   
    def r(edad):
        "el valor de la tasade prevalencia deben ser == al numero de edades de 0 a 101 "
        #o de 0 a 65 etc etc
        r=[]
        #obtenemos r, la lista tendrá un valor de r por edad.
        for i in range(edad):
            r_x=(0.0142*e)**(0.1161*(i))
            r_x.append(r)
        r=np.array([r])
        return r
            
        
    #obtenemos M
    lista_M=[] #pacientes con AD 
    
    #l i que esta en la longitud de aqui no irá de 0 a # cantidad de listas?
    #en lugar de ir de 65 a 101? años. Es correcta mi du
    
    tasa_prevalencia_=[i for i in range(0, 101)]
    
    rT=[] #tasass de prevalencia de toda la población.
    for i in tasa_prevalencia_:
        rm=r(i)
        rT.append(rm)
    
    rM=rT[65:]    #indicdencia de AD
    rN=rT[:65]   #indicencia de AD san

    for i in range(len(poblacion_total)):
            tasa_prevalencia_Total=np.multiply(poblacion_total[i],rM[i])
#            expec_vida_total=(-0.25*i)+24.6 #expectativa de vida en función de la edad
            lista_M.append(tasa_prevalencia_Total) 
           
                
     k=[]
     
       
    
    
    lista_expec_vida=[]
    
    for i in range(65,101):
        expec_vida=(-0.25*i)+24.6
        lista_expec_vida.append(expec_vida)  
    lista_expec_vida=np.array([lista_expec_vida])
        
    coef_muerte_nacimientos=0.08
    coef_muerte_poblacion=0.5
    
    parametro_b=a(n-x+1) + 1 - a(n-i)
    
    Tasa_sup_AD= (lista_expec_vida-coef_muerte_poblacion)/np.sum(np.prod)
    
    # lista_expec_vida=()
    # for i in x:
    #     expec_vida=(-0.25*i)+24.6
    #     lista_expec_vida(expec_vida)
'''    
    listas_r.append(Población_65_años_con_EA)
    y=x-65
    for i in range(y):
        #Obtenemos r 
        r_x=np.divide(listas_r[y-1], poblacion_total[y-1])
        r_x.insert(0,Población_por_edad_año_0[y])
        r_x.pop(61)
        listas_r.append(r_x)
        r_x.clear()
    #La idea es que listas sea una lista de listas donde
    #cada lista tenga el tamaño de la población de esa edad con EA del año 0 al 60
    #en total habrá 36 listas, una por edad
    return listas_r
'''    
pob_total=poblacion(100)            
poblacion_EA(100, pob_total)            
        

    
b=[1,2,3,4]
c=[4,3,2,1]
a=np.array([b, c], order='C')

tasa_prevalencia_=[i for i in range(0, 101)]

pruena=tasa_prevalencia_[:65]

