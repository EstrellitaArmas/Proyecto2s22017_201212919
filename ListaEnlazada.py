class Nodo(object):
    def __init__(self, nivel = None, numero= None, prox = None):
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

    def buscar(self, idHabitacion = None):
        aux = self.primero
        while aux != None:
            if aux.id == idHabitacion:
                print "ENCONTRADO :"+ str(aux.nivel) + str(aux.numero)
                return True
            aux = aux.prox  
            if aux == self.primero:
                break
        print "fin de la lista"  
        return False

    def eliminar(self, idHabitacion= None):
        if (self.buscar(idHabitacion)) :
            #// Consulta si el nodo a eliminar es el pirmero
            if (self.primero.id == idHabitacion) :
                if self.primero == self.ultimo:
                    self.primero = None
                    self.ultimo = None
                    return "Eliminado, lista vacia"
                else:
                    self.primero = self.primero.prox
                    self.ultimo.prox = self.primero
                    return "Eliminado"
            else:
                #// Crea ua copia de la lista.
                aux = self.primero;
                #// Recorre la lista hasta llegar al nodo anterior 
                #// al de referencia.
                while(aux.prox.id != idHabitacion):
                    aux = aux.prox;
                
                if (aux.prox == self.ultimo) :
                    aux.prox = self.primero
                    self.ultimo = aux
                    return "Eliminado"
                else :
                    #// Guarda el nodo siguiente del nodo a eliminar.
                    siguiente = aux.prox;
                    #// Enlaza el nodo anterior al de eliminar con el 
                    #// sguiente despues de el.
                    aux.prox = siguiente.prox  
                    #// Actualizamos el puntero del ultimo nodo
                    return "Eliminado"
        else :
            return "Habitacion no existe"
                
    def imprimir(self):
        aux = self.primero
        while aux != None:
            print "usuarios :"+ str(aux.nivel) + str(aux.numero)
            aux = aux.prox  
            if aux == self.primero:
                break
        print "fin de la lista" 

    def graficarLista(self):
        archivo = open("listaHabitaciones.txt", 'w')
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
                    colaGraphiz += "}"
                    break

        archivo.write(colaGraphiz)
        archivo.close()