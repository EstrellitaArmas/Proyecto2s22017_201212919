from ArbolAVL import ArbolAVL 
from ArbolB import ArbolB 
from ArbolB import NodoB 

class NodoDoble(object):
    def __init__(self, nombre = None , password= None, direccion = None, phone = None, age = None, prox = None , ant = None):
        self.nombre = nombre 
        self.password = password  
        self.direccion = direccion
        self.phone = phone
        self.age = age
        self.prox = prox
        self.ant = ant
    def __str__(self):
        return str(self.password, self.nombre, self.phone,self.age)

class ListaDobleEnlazada(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, nodo = None):
        if self.primero == None :
            self.primero = nodo
            self.ultimo = nodo
        else :
            nodo.prox = self.primero
            self.primero.ant = nodo 
            self.primero = nodo
       
    def imprimir(self):
        aux = self.primero
        while aux != None:
            print "Usuario insertado :"+ str(aux.nombre)
            aux = aux.prox  
        print "fin de la lista"

    def obtenerUsuario(self, nombre= None):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                print "usuario encontrado :"+ str(aux.nombre)    
                return aux            
            aux = aux.prox
           
    def validarUser(self, nombre= None, password = None):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre and aux.password == password:
                print "usuario encontrado :"+ str(aux.nombre)    
                return "true"            
            aux = aux.prox
            

    def graficarLista(self):
        archivo = open("listaUsuarios.dot", 'w')
        colaGraphiz = "digraph cola {"
        contador = 0
        contadorMas = 1 
        aux = self.primero
        if aux == None:
            colaGraphiz += "}"
        while aux != None:
            contador += 1
            contadorMas += 1
            colaGraphiz += "n0"+str(contador)+" [label=\""+str(aux.nombre)+"\"] ; "
            aux = aux.prox 
            if aux != None:
                colaGraphiz +=  "n0"+str(contador)+" -> n0"+str(contadorMas)+" ;"
                colaGraphiz +=  "n0"+str(contadorMas)+" -> n0"+str(contador)+" ;"
                
        colaGraphiz += "}"
        archivo.write(colaGraphiz)
        archivo.close()