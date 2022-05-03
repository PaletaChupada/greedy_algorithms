'''
Titulo: Codigo de Huffman
Descripcion: Este programa realiza el codigo de Huffman, este codigo lo que realiza es añadirle el codigo binario mas pequeño a la letra con mayor concurrencia y el mayor a la letra con menor concurrencia
Fecha: 2 de Mayo del 2022
Autor: Espinoza Bautista Daniel asdfafas
'''

# Importamos la libreria de tiempo
from time import time

# Creamos la clase nodo
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # Frecuencia del simbolo
        self.freq = freq
 
        # Nombre del simbolo (caracter)
        self.symbol = symbol
 
        # Nodo izquierdo del nodo actual
        self.left = left
 
        # Nodo derecho del nodo actual
        self.right = right
 
        # Direccion del arbol
        self.huff = '' 
 
def printNodes(node, val=''):
    # Codigo de huffman del nodo actual
    newVal = val + str(node.huff)
 
    # Si el nodo no esta en el nodo del borde
    # lo atravesamos
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
 
        # Si el nodo esta en el nodo del borde
        # Imprimimos el codigo de Huffman del nodo
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
 
 
# Solicitamos la cadena de la cual contaremos los carecteres
print("Dame la cadena:")
cadena = input()
print("\n")

# Inicializamos el arreglo de frecuencias y caracteres
freq = []
chars = []

# Contamos los caracteres mayusculas y anexamos a los arreglos
aux_ascii= 65
while aux_ascii < 91:
    if chr(aux_ascii) in cadena:
        freq.append(cadena.count(chr(aux_ascii)))
        chars.append(chr(aux_ascii))
    aux_ascii+=1

# Contamos los caracteres minusculas y anexamos a los arreglos
aux_ascii= 97
while aux_ascii < 123:
    if chr(aux_ascii) in cadena:
        freq.append(cadena.count(chr(aux_ascii)))
        chars.append(chr(aux_ascii))
    aux_ascii+=1

# Imprimimos los arreglos ordenados de menor a mayor
print("Caracteres obtenidos de la cadena: ")
print(chars)
print("Concurrencia de los carateres obtenidos: ")
print(freq)
print("\n")

# Inicializamos los nodos
nodes = []

# Inicializamos la variable para contar el tiempo de ejecucion
tiempo_in = time()
 
# Convertimos los caracteres y las frecuencias
# En nodos del arbol de Huffman
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

# Realizamos el codigo de Huffman 
while len(nodes) > 1:
    # Ordenamos los nodos de manera ascendente
    # basandonos en su frecuencia
    nodes = sorted(nodes, key=lambda x: x.freq)
 
    # Tomamos los nodos mas pequeños
    left = nodes[0]
    right = nodes[1]
 
    # Asignamos su direccion a estos nodos
    left.huff = 0
    right.huff = 1
 
    # Combinamos los dos nodos mas pequeños para crear
    # un nuevo nodo 
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
    # Removemos los dos nodos y agregamos
    # el nuevo nodo crearo dentro de los ya existentes
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
 
# Imprimimos el arbol
print("Codigo de Huffman: ")
printNodes(nodes[0])
print("\n")

# Calculamos el tiempo que tarda en ejecutarse y lo imprimimos en pantalla
tiempo_fin = time() - tiempo_in
print("Tiempo de ejecucion: %.10f segundos." %tiempo_fin)