# EJERCICIOS 4 REINAS

import random
from ctypes import pointer

# LEER EL MAPA
def generarMapa(game):
    board = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

    for i in range(0,4):
        board[i][game[i]-1] = "®"
        for j in range(0,4):
            if board[i][j] == 0:
                board[i][j] = 0

    for i in range(0,4):
  
        print(board[i])



# GENERAR POBLACION
def generarPoblacion(cantInd):
    poblacion=[]
    for i in range(cantInd):
        game = [random.randint(1, 4) for _ in range(4)] 
        poblacion.append(game) 
    return poblacion



# EVALUAR FITNESS
def evaluarPoblacion(poblacion):
    fitness = []
    for reinas in poblacion:
        n = 4
        fit = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Si están en la misma columna
                if reinas[i] == reinas[j]:
                    fit = fit + 1
                
                # Si están en la misma diagonal
                if abs(reinas[i] - reinas[j]) == abs(i - j):
                    fit = fit + 1

        fitness.append(fit)
    return fitness


#GENERAR UNA NUEVA POBLACION


fitness = []
poblacion = generarPoblacion(10)
print(poblacion)
generarMapa(poblacion[0])

fitness = evaluarPoblacion(poblacion)
print(fitness)