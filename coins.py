'''
Titulo: Cambio minimo de monedas
Descripcion: Este programa regresa el cambio minimo que se puede regresar de un valor que el usuario digita
Fecha: 5 de mayo del 2022
Autor: Espinoza Bautista Daniel
'''

from time import time

def findMin(V):
      
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
  
    # Imprimimos los resultados
    for i in range(len(ans)):
        print(ans[i])
  
if __name__ == '__main__':
    print("Cantidad para regresar cambio")
    n = int(input())

    tiempo_in = time()

    print("La cantidad minima de cambio para la cantidad", n, ": ")
    findMin(n)

    tiempo_fin = time() - tiempo_in

    print("Tiempo de ejecucion: %.10f segundos." %tiempo_fin)
