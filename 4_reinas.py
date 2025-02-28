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
import random

def seleccion(poblacion, fitness):
    new_poblacion = []

    # Ordenar población por fitness (ascendente)
    for i in range(0, len(poblacion) - 1):
        if fitness[i] > fitness[i + 1]:
            aux = fitness[i]
            auxp = poblacion[i]
            fitness[i] = fitness[i + 1]
            poblacion[i] = poblacion[i + 1]
            fitness[i + 1] = aux
            poblacion[i + 1] = auxp

    # Calcular la suma total de las probabilidades (sumando los rangos)
    total = sum(range(1, len(poblacion) + 1))  # Suma de rangos
    
    # Calcular probabilidades acumuladas
    acumulado = []
    acumulado.append(1 / total)  # La primera probabilidad acumulada
    for i in range(1, len(poblacion)):
        acumulado.append(acumulado[i-1] + (i + 1) / total)  # Acumulamos las probabilidades

    # Seleccionar según las probabilidades acumuladas
    while len(new_poblacion) < 5:  
        rand = random.random()  
        for i in range(len(acumulado)):
            if rand <= acumulado[i]:
                new_poblacion.append(poblacion[i])
                break

    return new_poblacion
    
def cruza(poblacion):
  nuevaPob=[]
  for i in range(5):
    padre1=random.randint(0, 9)
    padre2=random.randint(0, 9)
    while(padre1==padre2): 
        padre2=random.randint(0, 9)
        
    aux = poblacion[padre1][1]
    hijo1 = poblacion[padre1]
    hijo1[1] = poblacion[padre2][1]
    hijo2 = poblacion[padre2]
    hijo2[1] = aux
    nuevaPob.append(hijo1) 
    nuevaPob.append(hijo2)
    return nuevaPob

#Función de mutación de un solo gen
def muta(poblacion):  # Corregido el nombre de la variable
    nuevaPob = []
    for i in range(len(poblacion)):
        individuo = list(poblacion[i])

        # Se evalúa si muta o no
        if random.random() <= 0.1:  # Es la probabilidad
            alelo1 = random.randint(0, 3)
            alelo2 = random.randint(0, 3)
            
            while alelo1 == alelo2:
                alelo2 = random.randint(0, 3)
               
            aux = individuo[alelo1]
            individuo[alelo1] = individuo[alelo2]
            individuo[alelo2] = aux
        nuevaPob.append(individuo)
    return nuevaPob

fitness = []
poblacion = generarPoblacion(10)
print(poblacion)
generarMapa(poblacion[0])

fitness = evaluarPoblacion(poblacion)
print("Fitness:")
print(fitness)

new_poblacion = seleccion(poblacion,fitness)
print("Nueva poblacion:")
print(new_poblacion)