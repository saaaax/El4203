{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOn1/jicBOMPP/CjFl3zBW8"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fLF2mmMpTkgp",
        "outputId": "ff01f094-8115-49a1-fe19-1f7de385e94b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Número de caminos entre A y B: 6\n"
          ]
        }
      ],
      "source": [
        "#Primero hacemos las funciones por si solas para comprobar que funcionan antes de pasarlas a una clase\n",
        "\n",
        "def caminos_iterativo(n, m):\n",
        "    #Matriz que almacena caminos\n",
        "    matriz = [[0] * m for _ in range(n)]\n",
        "\n",
        "    #Nuestro caso base será que para cualquier celda de la primera fila y columna, su cantidad de caminos será 1\n",
        "    for i in range(n):\n",
        "        matriz[i][0] = 1\n",
        "    for j in range(m):\n",
        "        matriz[0][j] = 1\n",
        "\n",
        "    #Para calcular las demás celdas lo hacemos con la suma de los caminos de la celda de arriba y de la izquierda\n",
        "    for i in range(1, n):\n",
        "        for j in range(1, m):\n",
        "            matriz[i][j] = matriz[i-1][j] + matriz[i][j-1]\n",
        "\n",
        "    #Retornamos los caminos de la celda inferior derecha\n",
        "    return matriz[n-1][m-1]\n",
        "\n",
        "#Comprobamos que resulta\n",
        "N = 3\n",
        "M = 3\n",
        "#caminos = caminos_iterativo(N, M)\n",
        "#print(f\"Número de caminos entre A y B: {caminos}\")\n",
        "#se ve que funciona\n",
        "\n",
        "\n",
        "#---------------------------------------------------------------------------------------------------------------------------\n",
        "\n",
        "\n",
        "#vemos ahora la recurrencia\n",
        "def caminos_recursivo(n, m):\n",
        "    #Mismo caso base\n",
        "    if n == 1 or m == 1:\n",
        "        return 1\n",
        "    #Misma forma de calcular el resto de celdas (suma de la de arriba y la de la izquierda)\n",
        "    else:\n",
        "        return caminos_recursivo(n - 1, m) + caminos_recursivo(n, m - 1)\n",
        "\n",
        "#probamos si funciona\n",
        "caminos = caminos_recursivo(N, M)\n",
        "print(f\"Número de caminos entre A y B: {caminos}\")\n",
        "#se ve que funciona\n",
        "\n",
        "#Ahora podemos pasar a la clase"
      ]
    }
  ]
}