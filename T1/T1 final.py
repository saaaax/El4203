import time
import matplotlib.pyplot as plt
from math import comb


def tiempo_decorador(func):
    def medir_tiempo(*args):
        #como sólo queremos comparar los tiempos, simplificaremos el problema a un cuadrado
        #tomamos el tiempo de partida
        inicio = time.time()
        #vector para los tiempos
        v_tiempo =[0]
        #extraemos los argumentos
        n = args[1]
        #recorremos los n
        for i in range(1, n):
            #usamos el método para ver cuanto tarda
            func(args[0], i, i)
            fin = time.time()
            #lo guardamos en el vector
            v_tiempo.append(fin - inicio)
        return v_tiempo
    return medir_tiempo

#Ahora que sabemos que las funciones funcionan lo pasamos a una clase
class PCB:
    # def __init__(self, n, m):
    #     self.n = n
    #     self.m = m
    @tiempo_decorador
    def caminos_iterativo(self,n, m):
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
    @tiempo_decorador
    def caminos_recursivo(self, n, m):
        #Mismo caso base
        if n == 1 or m == 1:
            return 1
        #Misma forma de calcular el resto de celdas (suma de la de arriba y la de la izquierda)
        else:
            return self.caminos_recursivo(n - 1, m) + self.caminos_recursivo(n, m - 1)
    @tiempo_decorador
    def caminos_comb(self, n, m):
        return comb(n + m - 2, n - 1)


caminos = PCB()

largo=15

#probamos el metodo para medir tiempo
iterativo = caminos.caminos_iterativo
recursivo = caminos.caminos_recursivo
combinatoria = caminos.caminos_comb

t_iterativo = iterativo(largo)
t_recursivo = recursivo(largo)
t_combinatoria = combinatoria(largo)



plt.plot(t_iterativo, label="método iterativo")
#restringimos el 0
plt.xlim(1, largo)
plt.title("método iterativo")
plt.xlabel("Ancho de la PCB")
plt.ylabel("Tiempo de ejecución en segundos")
plt.savefig("Tiempo con iteración.png")
plt.show()

plt.plot(t_recursivo, label="método recursivo")
#restringimos el 0
plt.xlim(1, largo)
plt.title("método recursivo")
plt.xlabel("Ancho de la PCB")
plt.ylabel("Tiempo de ejecución en segundos")
plt.savefig("Tiempo con recursión.png")
plt.show()


plt.plot(t_combinatoria, label="método recursivo")
#restringimos el 0
plt.xlim(1, largo)
plt.title("método combinatoria")
plt.xlabel("Ancho de la PCB")
plt.ylabel("Tiempo de ejecución en segundos")
plt.savefig("Tiempo con combinatoria.png")
plt.show()
