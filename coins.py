'''
Titulo: Cambio minimo de monedas
Descripcion: Este programa regresa el cambio minimo que se puede regresar de un valor que el usuario digita
Fecha: 2 de mayo del 2022
Autor: Espinoza Bautista Daniel
'''

# Importamos las librerias
from time import time

# Definimos la funcion de cambio
def cambio(V):
      
    # Denominacion de las monedas a utilizar
    deno = [1, 2, 5, 10]
    n = len(deno)
      
    # Inicializamos los resultados
    ans = []
  
    # Realizamos el ciclo de las operaciones a usar para cada una de las denominaciones
    i = n - 1
    while(i >= 0):
          
        # Obtenemos las denominaciones
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])
  
        i -= 1
  
    # Realizamos el conteo de monedas de cambio
    count_10=0
    count_5=0
    count_2=0
    count_1=0
    for i in range(len(ans)):
        if ans[i]==10:
            count_10+=1
        if ans[i]==5:
            count_5+=1
        if ans[i]==2:
            count_2+=1
        if ans[i]==1:
            count_1+=1
    
    # Imprimimos las monedas
    print("Monedas de 10: "+str(count_10))
    print("Monedas de 5: "+str(count_5))
    print("Monedas de 2: "+str(count_2))
    print("Monedas de 1: "+str(count_1))
    print("\n")
  
# Pedimos la cantidad
print("Cantidad para regresar cambio")
n = int(input())

# Inicializamos la variable para contar el tiempo de ejecucion
tiempo_in = time()

# Realizamos el calculo del cambio y lo imprimimos en pantalla
print("La cantidad minima de cambio para la cantidad", n, ": \n")
cambio(n)

# Calculamos el tiempo que tarda en ejecutarse y lo imprimimos en pantalla
tiempo_fin = time() - tiempo_in
print("Tiempo de ejecucion: %.10f segundos." %tiempo_fin)