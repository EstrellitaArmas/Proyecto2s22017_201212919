class NodoAVL(object):
    def __init__ (self, cliente=None, total=None, tarjeta = None, izquierda=None, derecha=None , padre = None):
        self.cliente = cliente
        self.total = total
        self.tarjeta = tarjeta
        self.FE = 0
        self.izquierda = izquierda
        self.derecha = derecha
        self.padre = padre

class Logical():
    def __init__ (self, valor=None):
        self.valor = valor
        
    def setLogical(self, valor):
        self.valor = valor
        
    def getLogical(self):
        return self.valor

class ArbolAVL(object): 
    def __init__ (self):
            self.raiz = None 
            self.encontro = None
            # eliminacion
            self.nuevaRaiz = None
            self.aux = None
            self.aux2 = None
            self.aumento = None
            self.borrado = False
            self.apuntado=False
            self.apuntado2=False
                                     
######### INSERTAR ########
    def agregarAVLIni(self, nuevoNodo): #nodo avl       
            temp = self.retornarAVL(nuevoNodo) 
            if temp == None:            # si no lo encontro
                h = Logical(False)
                self.raiz = self.agregarAVL(self.raiz, nuevoNodo, h)
                print("nodo agregado correctamente"+ str(nuevoNodo.tarjeta))
            else:
                if (temp.total != nuevoNodo.total) or (temp.cliente != nuevoNodo.cliente):
                    temp.total = nuevoNodo.total 
                    temp.cliente = nuevoNodo.cliente
                    print("nodo modificado correctamente"+ str(nuevoNodo.tarjeta))
                else:
                    print "nodo ya existe"
        
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
######### BUSQUEDA ########    
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
######### ROTACION ########       
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
######### ELIMINACION #####
    def eliminarINI(self , llave):
        self.eliminar(llave,self.raiz)
        
    def eliminar(self, llave, A ):
        if(self.raiz.izquierda!=None or self.raiz.derecha!=None):
            if(A!=None):
                if(A.tarjeta < llave):
                    self.eliminar(llave,A.derecha)
                    if(self.nuevaRaiz!=None and self.nuevaRaiz != self.raiz ):
                        A.izquierda = self.nuevaRaiz
                        self.nuevaRaiz = None
                    
                    if(self.borrado==True):
                        A.FE = A.FE - 1 
                        self.rotarBorrado(A)
                        if A.FE == 0:
                            self.borrado= True
                        else: 
                            self.borrado= False
                    
                    if(self.apuntado==True):
                        A.derecha= self.aux
                        self.apuntado=False
                    
                else:
                    if(A.tarjeta>llave):
                        self.eliminar(llave,A.izquierda)
                        if(self.nuevaRaiz!=None and self.nuevaRaiz != self.raiz):
                            A.izquierda=self.nuevaRaiz
                            self.nuevaRaiz=None
                        
                        if(self.borrado==True):
                            A.FE = A.FE + 1
                            self.rotarBorrado(A)
                            if A.FE == 0:
                                self.borrado= True
                            else: 
                                self.borrado= False
                        
                        if(self.apuntado==True):
                            A.izquierda=self.aux
                            self.apuntado=False
                        
                    else:
                        if(A.tarjeta==llave):
                            self.borrado=True
                            self.apuntado=True
                            if(A.izquierda == None):
                                self.aux = A.derecha
                            else:
                                if(A.derecha == None):
                                    self.aux = A.izquierda
                                else:
                                    self.aux= self.Reemplazar(A,A,True)                   
            else:
               raiz=None 
    
    def Reemplazar(self, A, buscado, estado):
        if(estado==True):
            self.Reemplazar(A.izquierda,buscado,False)
            if(self.nuevaRaiz!=None and self.nuevaRaiz != self.raiz):
                A.izquierda=self.nuevaRaiz
                self.nuevaRaiz=None
            
            if(buscado == self.raiz):
                self.raiz = self.aux2
            
            if(self.aux2 != buscado.izquierda):
                self.aux2.izquierda=buscado.izquierda
                buscado.izquierda=None
            else:
                buscado.izquierda=None

            self.aux2.derecha = buscado.derecha   
            buscado.derecha=None
            
            if(self.borrado==True):
                self.aux2.FE = A.FE + 1
                self.rotarBorrado(self.aux2)
                if A.FE == 0:
                    self.borrado= True
                else: 
                    self.borrado= False
            
        else:
            if(A.derecha==None):
                self.aux2=A
                self.borrado=True
                self.apuntado2=True
            else: 
                self.Reemplazar(A.derecha,buscado,estado)
                if(self.nuevaRaiz!=None and self.nuevaRaiz != self.raiz):
                    A.derecha=self.nuevaRaiz
                    self.nuevaRaiz=None
                
                if(self.apuntado2==True):
                    A.derecha=self.aux2.izquierda
                    self.apuntado2=False
               
                if(self.borrado==True):
                    A.FE = A.FE - 1 
                    self.rotarBorrado(A)
                    if A.FE == 0:
                        self.borrado= True
                    else: 
                        self.borrado= False
               
        return self.aux2
        
    def rotarBorrado(self, A):
            if(A.FE<-1):
                if(A.izquierda.FE>0):
                    if(self.raiz != A):
                        self.rotacionID(A,A.izquierda)
                        self.borrado=False
                        return True
                    else:
                        self.raiz = self.rotacionID(A,A.izquierda)
                        self.borrado=False
                        return True
                
                else:
                    if(self.raiz!=A):
                        II(A,A.izquierda)
                        self.borrado=False
                        return true
                    else:
                        raiz=II(A,A.izquierda)
                        self.borrado=False
                        return true
                    
            else:
                if(A.FE>1):
                    if(A.derecha.FE<0):
                        if(self.raiz != A ):
                            self.rotacionDI(A,A.derecha)
                            self.borrado=False
                            return True
                        else:
                            self.raiz = self.rotacionDI(A,A.derecha)
                            self.borrado=False
                            return True
                    else:
                        if(self.raiz != A):
                            self.rotacionDD(A,A.derecha)
                            self.borrado=False
                            return True
                        else:
                            self.raiz= self.rotacionDD(A,A.derecha)
                            self.aumento=False
                            self.borrado=False
                            return True
            return False
       
        
######### GRAFICA #########                   
    def graficarArbolAVL(self):
        self.digraf = "digraph G{\n"
        archivo = open("arbolAVLSistemaPago.txt", 'w')
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


