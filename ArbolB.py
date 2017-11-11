from ListaB import ListaB

class NodoB(object):
	def __init__(self, idFechaIngreso=None, nombreCliente=None, total = None, habitacion = None, fechaIngreso = None, fechaSalida = None):
		self.idFechaIngreso = idFechaIngreso
		self.nombreCliente = nombreCliente
		self.total = total 
		self.habitacion = habitacion
		self.fechaIngreso = fechaIngreso
		self.fechaSalida = fechaSalida

class Pagina(object): 
	def __init__(self, ramas=[0,0,0,0,0], claves=[0,0,0,0], cuentas=0):		
		self.ramas = ramas
		self.claves = claves
		self.cuentas = cuentas

claseListaB = ListaB()		
class ArbolB(object):
	def __init__(self):
		self.inicio = Pagina()
		self.inserta = NodoB()
		self.enlace = Pagina()
		self.pivote = False
		self.existe = False
		self.existe2 = False
		self.carpetaEncontrada = None

	
######################### INSERTAR ###################################################		
	#Crea el Nodo del Arbol B
	def crearNodoInsertar(self, idFechaIngreso, nombreCliente, total, habitacion,fechaIngreso,fechaSalida):
		nodob = NodoB(idFechaIngreso, nombreCliente, total, habitacion,fechaIngreso,fechaSalida)
		self.InsertarArbolB(nodob, self.inicio)
		
	
	#Inserta el nodo al Arbol B La clave es el Nodo y la raiz la Pagina
	def InsertarArbolB(self, clave, raiz):
		self.agregar(clave, raiz)
		if(self.pivote == True):
			self.inicio = Pagina(ramas=[None,None,None,None,None], claves=[None,None,None,None], cuentas=0)
			self.inicio.cuentas = 1
			self.inicio.claves[0] = self.inserta
			self.inicio.ramas[0] = raiz
			self.inicio.ramas[1] = self.enlace
			
			
	#Agregar al Arbol, Balanceando el arbol por Id
	def agregar(self, clave, raiz):
		pos = 0              
		self.pivote = False; 
		
		vacioBol = self.vacio(raiz)
		
		if(vacioBol == True):
			self.pivote = True
			self.inserta = clave
			self.enlace = None
		else:
			pos = self.existeNodo(clave, raiz)
			
			if(self.existe == True):
				self.pivote = False
			else:
				self.agregar(clave, raiz.ramas[pos])
				
				if(self.pivote == True):
					
					if(raiz.cuentas < 4):
						self.pivote = False;
						self.insertarClave(self.inserta, raiz, pos)
					else:
						self.pivote = True
						self.dividirPagina(self.inserta, raiz, pos)
						print("Inserto: "+ clave.nombreCliente + "id: "+ str(clave.idFechaIngreso))
			
			
	#Verificar si la raiz no Existe
	def vacio(self, raiz):
		if(raiz == None or raiz.cuentas == 0):
			return True
		else:
			return False
		
	
	#Insertar Claves en Pagina
	def insertarClave(self, clave, raiz, posicion):
		i = raiz.cuentas
		
		while i != posicion:
			raiz.claves[i] = raiz.claves[i - 1]
			raiz.ramas[i + 1] = raiz.ramas[i]
			i-=1
		
		raiz.claves[posicion] = clave
		raiz.ramas[posicion + 1] = self.enlace
		val = raiz.cuentas+1
		raiz.cuentas = val
		print("Inserto Valor: "+ clave.nombreCliente + "id: "+ str(clave.idFechaIngreso))
		
		
	#Dividir Pagina
	def dividirPagina(self, clave, raiz, posicion):
		pos = 0
		Posmda = 0
		if(posicion <= 2):
			Posmda = 2
		else:
			Posmda = 3
		
		Mder = Pagina(ramas=[None,None,None,None,None], claves=[None,None,None,None], cuentas=0)
		pos = Posmda + 1
		
		while pos != 5:
			i = ((pos - Posmda) - 1)
			j = (pos - 1)
			Mder.claves[i] = raiz.claves[j]
			Mder.ramas[pos - Posmda] = raiz.ramas[pos]
			pos+=1
		
		Mder.cuentas = 4 - Posmda
		raiz.cuentas = Posmda
		
		if(posicion <= 2):
			self.insertarClave(clave, raiz, posicion)
		else:
			self.insertarClave(clave, Mder, (posicion - Posmda))
			
		self.inserta = raiz.claves[raiz.cuentas - 1]
		Mder.ramas[0] = raiz.ramas[raiz.cuentas]
		val = raiz.cuentas - 1
		raiz.cuentas = val
		self.enlace = Mder
		
############################## BUSCAR #####################################	
	#Virificar si Existe el Nodo	
	def existeNodo(self, clave, raiz):
		valor =0
		if(clave.idFechaIngreso < raiz.claves[0].idFechaIngreso):
			self.existe2 = False
			valor = 0
		else:
			valor = raiz.cuentas
			while (clave.idFechaIngreso < raiz.claves[valor - 1].idFechaIngreso and valor > 1):
				valor-=1
			
			if (clave.idFechaIngreso < raiz.claves[valor - 1].idFechaIngreso):
				self.existe = True
			else:
				self.existe = False
			
			if (clave.idFechaIngreso == raiz.claves[valor - 1].idFechaIngreso):
				self.existe2 = True
			else:
				self.existe2 = False			
			
		
		return valor

	#Buscar Nodo
	def retornarNodoArbolB(self, idBuscar, nombreCliente):	
		#self.inicio = raiz 
		clave = NodoB(idBuscar, nombreCliente)
		return self.retornarNodo(clave, self.inicio)
	
	#Buscar Nodo
	def retornarNodo(self, clave, raiz):
		valorEncontrado = None
		pos = 0
		vacioBol = self.vacio(raiz)
		
		if(vacioBol == True):
			print("No Existe")
		else:
			pos = self.existeNodo(clave, raiz)
			if(self.existe2 == True):
				valorEncontrado = raiz.claves[pos - 1]	
				self.carpetaEncontrada = raiz.claves[pos - 1]	
			else:
				valorEncontrado = self.retornarNodo(clave, raiz.ramas[pos])
		return valorEncontrado

	#RetornarHabitaciones
	def retornarHabitaciones(self, nombreUsuario):	
		self.todasLasHabitaciones = ""
		self.RetornarArbolHabitaciones(self.inicio, nombreUsuario)
		return self.todasLasHabitaciones 
	
	#Retornar Habitaciones
	def RetornarArbolHabitaciones(self, raiz, nombreUsuario):
		nodo = raiz
	
		if(nodo == None):
			variable = "Hola Mundo"
		else:
			if (nodo.cuentas != 0):
				k=1
				while k <= nodo.cuentas:
					if nodo.claves[k - 1].Nombre == nombreUsuario:
						self.todasLasHabitaciones += str(nodo.claves[k - 1].Habitacion) + "@"
					k+=1
				i=0
				while i <= nodo.cuentas:
					if (nodo.ramas[i] != None):
						if (nodo.ramas[i].cuentas != 0):					
							hola = "Mundo xD"
					i+=1
	
				j=0
				while j <= nodo.cuentas:
					self.RetornarArbolHabitaciones(nodo.ramas[j], nombreUsuario)
					j+=1

############################# GRAFICAR ######################################
	#Crear Archivo
	def dibujarArbol(self ):
		archivo=open('arbolBHistorial.txt', 'w')
		archivo.write('digraph G{\n')
		archivo.write("node [shape = record];\n");3
		archivo.write("rankdir = TD;\n");
		self.grabarArchivo(self.inicio , archivo)
		archivo.write('}')
		archivo.close()	
		
	#Escribir Contenido del Archivo
	def grabarArchivo(self, raiz, archivo):
		nodo = raiz				
		if(nodo == None):
			print("---")
		else:
			if (nodo.cuentas != 0):
				archivo.writelines("activo_" + str(nodo.claves[0].nombreCliente) + " [label= \"")
				k=1
				while k <= nodo.cuentas:
					archivo.writelines("<r" + str(k - 1) + ">" + " | " + "<cl" + str(k) + ">" + "Fecha: " + str(nodo.claves[k - 1].idFechaIngreso) +" / " + str(nodo.claves[k - 1].nombreCliente)+ " &#92;" + " | ")
					k+=1
				
				
				archivo.writelines("<r" + str(k - 1) + "> \"];\n")
				i=0
				while i <= nodo.cuentas:
					if (nodo.ramas[i] != None):
						if (nodo.ramas[i].cuentas != 0):
							archivo.writelines("activo_" + str(nodo.claves[0].nombreCliente) + ":r" + str(i) + " -> activo_" + str(nodo.ramas[i].claves[0].nombreCliente) + ";\n")							
						
					i+=1
					
				j=0
				while j <= nodo.cuentas:
					self.grabarArchivo(nodo.ramas[j],archivo)
					j+=1
					
############### MODIFICAR NOMBRE ################
	def actualizarNombre(self, idFechaIngreso, nuevaFecha):
		nodoB = NodoB(idFechaIngreso, "1", "1", "1", "1")
		self.actualizarNombreArbolB(nodoB, nuevaFecha, self.inicio)
		return "Nombre Actualizado"
	
	#ACTUALIZAR NOMBRE 
	def actualizarNombreArbolB(self, nodoB, nuevaFecha, raiz):
		pos = 0
		pos = self.existeNodo(nodoB, raiz)
		if(self.existe2 == True):
			raiz.claves[pos - 1].nombreCliente = nuevaFecha.nombreCliente
			raiz.claves[pos - 1].total = nuevaFecha.total
			raiz.claves[pos - 1].habitacion = nuevaFecha.habitacion
			raiz.claves[pos - 1].fechaSalida = nuevaFecha.fechaSalida
		else:
			self.actualizarNombreArbolB(nodoB, nuevaFecha, raiz.ramas[pos])					
	
################# Eliminar ########################
	def Eliminar(self, idEliminar):
		self.InsertarNodosLista(self.inicio)
		raizLista = claseListaB.retornarLista()
		self.inicio = Pagina()
		
		while raizLista != None:
			if raizLista.index != None and raizLista.nodoArbolB.idFechaIngreso != idEliminar:
				self.InsertarArbolB(raizLista.nodoArbolB, self.inicio)
			raizLista = raizLista.siguiente		
		
		claseListaB.Limpiar()
		return self.inicio
	
	#INSERTAR NODOS EN LISTA
	def InsertarNodosLista(self, raiz):
		nodo = raiz		
		
		if(nodo != None):
			if (nodo.cuentas != 0):
				k=1
				while k <= nodo.cuentas:
					claseListaB.insertar(nodo.claves[k - 1])					
					k+=1
					
				j=0
				while j <= nodo.cuentas:
					self.InsertarNodosLista(nodo.ramas[j])
					j+=1
					
											
					
					
	