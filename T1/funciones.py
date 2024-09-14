#Primero hacemos las funciones por si solas para comprobar que funcionan antes de pasarlas a una clase
def caminos_iterativo(n, m):
    #Matriz que almacena caminos
    matriz = [[0] * m for _ in range(n)]

    #Nuestro caso base será que para cualquier celda de la primera fila y columna, su cantidad de caminos será 1
    for i in range(n):
        matriz[i][0] = 1
    for j in range(m):
        matriz[0][j] = 1

    #Para calcular las demás celdas lo hacemos con la suma de los caminos de la celda de arriba y de la izquierda
    for i in range(1, n):
        for j in range(1, m):
            matriz[i][j] = matriz[i-1][j] + matriz[i][j-1]

    #Retornamos los caminos de la celda inferior derecha
    return matriz[n-1][m-1]

#Comprobamos que resulta
N = 3
M = 3
#caminos = caminos_iterativo(N, M)
#print(f"Número de caminos entre A y B: {caminos}")
#se ve que funciona


#---------------------------------------------------------------------------------------------------------------------------


#vemos ahora la recurrencia
def caminos_recursivo(n, m):
    #Mismo caso base
    if n == 1 or m == 1:
        return 1
    #Misma forma de calcular el resto de celdas (suma de la de arriba y la de la izquierda)
    else:
        return caminos_recursivo(n - 1, m) + caminos_recursivo(n, m - 1)

#probamos si funciona
caminos = caminos_recursivo(N, M)
print(f"Número de caminos entre A y B: {caminos}")
#se ve que funciona

#---------------------------------------------------------------------------------------------------------------------------


#veamos combinatoria
from math import comb
def caminos_comb(n, m):
    return comb(n + m - 2, n - 1)

#probamos si funciona
caminos = caminos_comb(N, M)
print(f"Número de caminos entre A y B: {caminos}")
#se ve que funciona


#Ahora podemos pasar a la clase
