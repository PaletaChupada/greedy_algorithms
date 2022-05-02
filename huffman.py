'''
Titulo: Codigo de Huffman
Descripcion: Este programa realiza el codigo de Huffman, este codigo lo que realiza es añadirle el codigo binario mas pequeño a la letra con mayor concurrencia y el mayor a la letra con menor concurrencia
Fecha: 5 de Mayo del 2022
Autor: Espinoza Bautista Daniel asdfafas
'''
 
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
 
 
# Solicitamos el tamaño del arreglo de caracteres
tam = int(input("Dame el tamaño del arreglo de caracteres: "))

# Inicializamos el arreglo
chars = []

# Realizamos el llenado del arreglo
i=0
while i<tam:
    aux = input("Dame el caracter: ")
    chars.append(aux)
    i += 1

# Inicializamos el arreglo de frecuencias
freq = []

# Realizamos el llenado del arreglo de frecuencias
i=0
while i<tam:
    aux=int(input("Dame la frecuencia del caracter: "))
    freq.append(aux)
    i += 1

# Inicializamos los nodos
nodes = []
 
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
printNodes(nodes[0])
