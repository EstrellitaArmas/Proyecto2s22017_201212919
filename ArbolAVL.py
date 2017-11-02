class NodoAVL(object):
    def __init__ (self, cliente=None, total=None, tarjeta = None, izquierda=None, derecha=None , padre = None):
        self.cliente = cliente
        self.total = total
        self.tarjeta = tarjeta
        self.FE = 0
        self.izquierda = izquierda
        self.derecha = derecha
        self.padre = padre

class ArbolAVL(object): 
    def __init__ (self):
            self.raiz = None 
            self.encontro = None
                         

    def agregarAVL1(self, nuevoNodo): #nodo avl       
            temp = self.retornarAVL(nuevoNodo) 
            if temp == None:
                h = Logical(False)
                self.raiz = self.agregarAVL(self.raiz, nuevoNodo, h)
                print("nodo agregado correctamente"+ str(nuevoNodo.tarjeta))
            else:
                print("ya existe")
        
    def agregarAVL(self, raiz, nuevoNodo, h):
        if raiz == None:
            raiz = nuevoNodo            
            h.setLogical(True)
        elif nuevoNodo.tarjeta < raiz.tarjeta:
            nodoIz = self.agregarAVL(raiz.izquierda, nuevoNodo, h)
            raiz.izquierda = nodoIz
            if h.getLogical() == True:
                op = raiz.FE
                if op == 1:
                    raiz.FE = 0
                    h.setLogical(False)
                elif op == 0:
                    raiz.FE = -1
                elif op == -1:
                    nodo1 = raiz.izquierda
                    if nodo1.FE == -1:
                        raiz = self.rotacionII(raiz, nodo1)
                    else:
                        raiz = self.rotacionID(raiz, nodo1)
                    h.setLogical(False)
        elif nuevoNodo.tarjeta > raiz.tarjeta:
            nodoDr = self.agregarAVL(raiz.derecha, nuevoNodo, h)
            raiz.derecha = nodoDr
            if h.getLogical() == True:
                op = raiz.FE
                if op == 1:
                    nodo1 = raiz.derecha
                    if nodo1.FE == 1:
                        raiz = self.rotacionDD(raiz, nodo1)
                    else:
                        raiz = self.rotacionDI(raiz, nodo1)
                    h.setLogical(False)
                elif op == 0:
                            raiz.FE = 1
                elif op == -1:
                    raiz.FE = 0
                    h.setLogical(False)
        return raiz    
    
    def retornarAVL(self, nuevoNodo): 
        self.encontro = None
        self.buscarAVL(self.raiz, nuevoNodo.tarjeta)
        return self.encontro
    
    def buscarAVL(self, raiz, tarjeta):  # raiz, nodo avl y nodo Circular
       if raiz != None:
            if tarjeta == raiz.tarjeta:
                #self.raiz.encontro = raiz
                self.encontro = raiz
            else:
                self.buscarAVL(raiz.izquierda, tarjeta)
                self.buscarAVL(raiz.derecha, tarjeta) 
                    
       
    def rotacionID(self, nodo, nodo1):
        nodo2 = nodo1.derecha
        nodo1.derecha = nodo2.izquierda
        nodo2.izquierda = nodo1
        nodo.izquierda = nodo2.derecha
        nodo2.derecha = nodo
        #nodo = nodo2
        if nodo2.FE == 1:
            nodo1.FE = -1
        else:
            nodo1.FE = 0
        if nodo2.FE == -1:
            nodo.FE = 1
        else:
            nodo.FE = 0
        nodo2.FE = 0
        return nodo2
    
    def rotacionII(self, nodo, nodo1):
        nodo.izquierda = nodo1.derecha
        nodo1.derecha = nodo
        if nodo1.FE == -1:
            nodo.FE = 0
            nodo1.FE = 0
        else:
            nodo.FE = -1
            nodo1.FE = 1
        return nodo1
    
    def rotacionDD(self, nodo, nodo1):
        nodo.derecha = nodo1.izquierda
        nodo1.izquierda = nodo
        if nodo1.FE == 1:
            nodo.FE = 0
            nodo1.FE = 0
        else:
            nodo.FE = 1
            nodo1.FE = -1
        return nodo1
    
    def rotacionDI(self, nodo, nodo1):
        nodo2 = nodo1.izquierda
        nodo1.izquierda = nodo2.derecha
        nodo2.derecha = nodo1
        nodo.derecha = nodo2.izquierda
        nodo2.izquierda = nodo
    
        if nodo2.FE == 1:
            nodo.FE = -1
        else:
            nodo.FE = 0
        if nodo2.FE == -1:
            nodo1.FE = 1
        else:
            nodo1.FE = 0
        nodo2.FE = 0
        return nodo2    
                    
    def graficarArbolAVL(self):
        self.digraf = "digraph G{\n"
        archivo = open("SistemaPagoAVL.dot", 'w')
        self.graficarPreOrden(self.raiz)
        self.digraf += "\n}"
        archivo.write(self.digraf)
        archivo.close()

    def graficarPreOrden(self, nuevoNodo):
        if nuevoNodo != None:
            mensajeFin = nuevoNodo.tarjeta
            mensajeTotal = nuevoNodo.total
            self.digraf += "nodo_" + str(mensajeFin) + ' [label="' +str(mensajeFin) +'/ Q'+ str(mensajeTotal) +'"]\n'
            if nuevoNodo.izquierda != None:
                mensajeIzq = nuevoNodo.izquierda.tarjeta
                self.digraf += "nodo_" + str(mensajeFin) + " -> " "nodo_" + str(mensajeIzq) + "\n"
                self.graficarPreOrden(nuevoNodo.izquierda)
            else:
                pass
            if nuevoNodo.derecha != None:
                mensajeDer = nuevoNodo.derecha.tarjeta
                self.digraf += "nodo_" + str(mensajeFin) + " -> " "nodo_" + str(mensajeDer) + "\n"
                self.graficarPreOrden(nuevoNodo.derecha)                   
            else:
                pass
        else:
            pass


class Logical():
    def __init__ (self, valor=None):
        self.valor = valor
        
    def setLogical(self, valor):
        self.valor = valor
        
    def getLogical(self):
        return self.valor
