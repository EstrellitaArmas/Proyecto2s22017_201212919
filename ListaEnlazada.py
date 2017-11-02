class Nodo(object):
    def __init__(self, numero = None, nivel= None, prox = None):
        self.numero = numero
        self.nivel = nivel
        self.id = str(nivel) + str(numero)
        self.prox = prox
    def __str__(self):
        return str(self.ip, self.mascara)

class ListaEnlazada(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, nodo = None):
        if self.primero == None :
            self.primero = nodo
            self.ultimo = nodo
        else :
            nodo.prox = self.primero
            self.primero = nodo

        self.ultimo.prox = self.primero

    def imprimir(self):
        aux = self.primero
        while aux != None:
            print "usuarios :"+ str(aux.numero) + str(aux.nivel)
            aux = aux.prox  
            if aux == self.primero:
                break
        print "fin de la lista"  

    def graficarLista(self):
        archivo = open("listaHabitaciones.dot", 'w')
        colaGraphiz = "digraph habitaciones {"
        contador = 0
        contadorMas = 1 
        aux = self.primero
        if aux == None:
            colaGraphiz += "}"
        while aux != None:
            contador += 1
            contadorMas += 1
            colaGraphiz += "n0"+str(contador)+" [label=\""+str(aux.nivel)+" / "+str(aux.numero)+" / "+str(aux.id)+"\"] ; "
            aux = aux.prox 
            if aux != None:
                if aux != self.primero:
                    colaGraphiz +=  "n0"+str(contador)+" -> n0"+str(contadorMas)+" ;"
                else:
                    colaGraphiz +=  "n0"+str(contador)+" -> n01"
                    break

        colaGraphiz += "}"
        archivo.write(colaGraphiz)
        archivo.close()