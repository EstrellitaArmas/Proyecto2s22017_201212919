class NodoLB:
	def __init__(self, idB=None, nodoArbolB=None, index=None, siguiente=None):
		self.idB = idB
		self.nodoArbolB = nodoArbolB
		self.index = index
		self.siguiente = siguiente

class ListaB:
	def __init__(self):
		self.raiz = None
		self.indiceLista = 0
		self.contadorRegistro = 0
		self.archivoBitacora =""
	
	def insertar(self, nodoB):
		self.contadorRegistro +=1
		if self.raiz == None:			
			nodo = NodoLB(self.contadorRegistro, nodoB, self.indiceLista)
			self.raiz = nodo
			self.indiceLista = self.indiceLista + 1
		else :
			aux = self.raiz
			while aux.siguiente != None:
				aux = aux.siguiente				
			
			nodo = NodoLB(self.contadorRegistro, nodoB, self.indiceLista)
			self.indiceLista = self.indiceLista + 1
			aux.siguiente = nodo
		print("Inserto En Lista")
				
	
	def consultarLista(self):
		aux = self.raiz
		dato = ""
		if aux == None:			
			return "Lista Vacia"			
		else :
			while aux != None:
				if aux.index != None:
					dato += str(aux.idB) + " -> "+ str(aux.nodoArbolB.nombreCarpeta) +"; \n"										
				aux = aux.siguiente
			return str(dato) 
	
	def retornarLista(self):
		aux = self.raiz
		return aux	
	
	def Limpiar(self):
		self.raiz=None
	
	
	