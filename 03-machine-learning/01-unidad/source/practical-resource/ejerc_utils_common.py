""" 
lab_utils_common.py
    funciones comunes a todos los ejercicios, Machine Learning, Semana 2 
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('./deeplearning.mplstyle')
dlblue = '#0096ff'; dlorange = '#FF9300'; dldarkred='#C00000'; dlmagenta='#FF40FF'; dlpurple='#7030A0';
dlcolors = [dlblue, dlorange, dldarkred, dlmagenta, dlpurple]
dlc = dict(dlblue = '#0096ff', dlorange = '#FF9300', dldarkred='#C00000', dlmagenta='#FF40FF', dlpurple='#7030A0')


##########################################################
# Rutinas de regresión
##########################################################

#Función para calcular el costo
def compute_cost_matrix(X, y, w, b, verbose=False):
    """
    Calcula el gradiente para regresión lineal
     Argumentos:
      X (ndarray (m,n)): Datos, m ejemplos con n características
      y (ndarray (m,)) : valores objetivo
      w (ndarray (n,)) : parámetros del modelo  
      b (scalar)      : parámetro del modelo
      verbose : (Booleano) Si es True, imprime el valor intermedio f_wb
    Retorna
      cost: (scalar)
    """
    m = X.shape[0]

    # calcular f_wb para todos los ejemplos.
    f_wb = X @ w + b
    # calcular el costo
    total_cost = (1/(2*m)) * np.sum((f_wb-y)**2)

    if verbose: print("f_wb:")
    if verbose: print(f_wb)

    return total_cost


def compute_gradient_matrix(X, y, w, b):
    """
    Calcula el gradiente para regresión lineal

    Argumentos:
      X (ndarray (m,n)): Datos, m ejemplos con n características
      y (ndarray (m,)) : valores objetivo
      w (ndarray (n,)) : parámetros del modelo  
      b (scalar)      : parámetro del modelo
    Retorna
      dj_dw (ndarray (n,1)): El gradiente del costo respecto a los parámetros w.
      dj_db (scalar):        El gradiente del costo respecto al parámetro b.

    """
    m,n = X.shape
    f_wb = X @ w + b
    e   = f_wb - y
    dj_dw  = (1/m) * (X.T @ e)
    dj_db  = (1/m) * np.sum(e)

    return dj_db,dj_dw


# Versión con bucle de compute_cost para múltiples variables
def compute_cost(X, y, w, b):
    """
    Calcula el costo
    Argumentos:
      X (ndarray (m,n)): Datos, m ejemplos con n características
      y (ndarray (m,)) : valores objetivo
      w (ndarray (n,)) : parámetros del modelo  
      b (scalar)      : parámetro del modelo
    Retorna
      cost (scalar)   : costo
    """
    m = X.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb_i = np.dot(X[i],w) + b           #(n,)(n,)=escalar
        cost = cost + (f_wb_i - y[i])**2
    cost = cost/(2*m)
    return cost 

def compute_gradient(X, y, w, b):
    """
    Calcula el gradiente para regresión lineal
    Argumentos:
      X (ndarray (m,n)): Datos, m ejemplos con n características
      y (ndarray (m,)) : valores objetivo
      w (ndarray (n,)) : parámetros del modelo  
      b (scalar)      : parámetro del modelo
    Retorna
      dj_dw (ndarray Forma (n,)): El gradiente del costo respecto a los parámetros w.
      dj_db (scalar):             El gradiente del costo respecto al parámetro b.
    """
    m,n = X.shape           #(número de ejemplos, número de características)
    dj_dw = np.zeros((n,))
    dj_db = 0.

    for i in range(m):
        err = (np.dot(X[i], w) + b) - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * X[i,j]
        dj_db = dj_db + err
    dj_dw = dj_dw/m
    dj_db = dj_db/m

    return dj_db,dj_dw

