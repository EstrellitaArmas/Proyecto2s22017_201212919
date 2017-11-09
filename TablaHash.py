class NodoH:
	def __init__(self, codigo=None, nombre=None):
		self.codigo = codigo
		self.nombre = nombre	

class TablaHash:
	def __init__(self):
		self.tabla = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.tablaInicio = 47
		self.exeso = float(0.75)		
		self.maxSize = None
		self.size = None
		self.tempSize = None
		self.elementos = None		
		self.aux = None
		self.aux2 = None
		self.factorE = None
		self.CrearTabla()
		
	
	#CREAR TABLA
	def CrearTabla(self):
		#self.tabla= HNodo[self.tablaInicio]
		
		for i in range(0, self.tablaInicio-1):
			self.tabla[i]=None;
			self.elementos=0;
			self.factorE = float(0.0)
			self.maxSize = 28
			self.tempSize = 47
			self.size = 0
			self.aux = 1
			self.aux2 = self.aux
			
		
				
	#CREAR NODO HASH
	def CrearNodoInsertar(self, codigo, nombre):
		nodoHash = NodoH(codigo, nombre)
		self.Insertar(nodoHash)
	
	#INSERTAR 
	def Insertar(self, nodoHash):
		indice = self.direccion(nodoHash.codigo)
		if self.elementos < self.maxSize:
			self.insertarTabla(nodoHash, indice)
			self.elementos+=1
			return 1
		else:
			x = self.maxSize
			self.redimensionar()
			self.maxSize = x*2
		return 0
	
	
	def devolverClave(self, codigo):
		cod = str(codigo)
		constante = 0.6180334
		cod_int = int(cod)
		multiplicacion = constante * cod_int
	
		multiplicacion_S = str(multiplicacion)
	
		a = abs(multiplicacion) - abs(int(multiplicacion))
		r = a * self.tempSize
		
		return int(r)
	
	
	#EXISTE
	def existe(self, indice):
		aux = NodoH()
		if indice < len(self.tabla):
			aux = self.tabla[indice]
			if aux == None:
				return True
			else:
				return False
		
		return False
			
	
	#DIRECCION
	def direccion(self, codigo):
		clave = self.devolverClave(codigo)
		enviar = 0
		i = 0
		indice = clave #% len(self.tabla)
		
		if indice < len(self.tabla):
			while self.tabla[indice] != None: #and int(self.tabla[indice].codigo) != codigo:
				#if self.tabla[indice].codigo == codigo:
				if self.tabla[indice] == None:
					print("Retornar Indice sin Cambios")
				else:
					i+=1
					indice = clave + (i*i)
					#indice = indice % len(self.tabla)
		
		print("Clave generado: " + str(clave))
		print("Direccion enviada: " + str(indice))		
		return indice
	
	
	#INSERTAR TABLA
	def insertarTabla(self, nuevo, indice):
		self.tabla[indice] = nuevo
		print("inserto: " + str(nuevo.codigo) + " en: "+ str(indice))
	
	
	#REDIMENSIONAR
	def redimensionar(self):
		self.aux = self.aux2*2
		nuevoTamano = 2* len(self.tabla)
		print("Tamano tabla vieja: " + len(self.tabla) + " y nueva: " + nuevoTamano)
		self.elementos = 0
		tablaTemp = self.tabla
		self.tabla = HNodo[nuevoTamano]
		for i in tablaTemp.length:
			if tablaTemp[i] != None:
				aux= tablaTemp[i];
				print("Encontro " + i);
				self.insertarTabla(aux, i)
				self.elementos +=1
			
			self.maxSize = (self.maxSize*2)
			
	
	#Mostrar
	def mostrar(self):
		enviar=""
		codigo=""
		nombre=""
		
		aux =  NodoH()
		x=1
		print("Tamano tabla: " + str(len(self.tabla)))
		
		for i in range(0, len(self.tabla)):
			aux = self.tabla[i]
			if aux != None and aux != 0:
				codigo= aux.codigo
				nombre = aux.nombre
				enviar = enviar + str(codigo) + " - " + nombre + " "+ str(i) +  ";"
				print("Direccion: " + str(i) + " Codigo: " + str(codigo) + " - " + nombre + ";")
				x += 1
			    
		print("Elementos "+ str(self.elementos))
			
	#Graficar	
	def graficar(self , fecha):
		aux = NodoH()
		cadenanueva=""
		cadenanueva2=""
		
		archivo=open('TablaHash'+fecha+'.txt','w')				
		archivo.write('digraph  G {  nodesep=.05;\n')		
		archivo.write("rankdir = LR;\n")
		archivo.write("node[shape=record,width=.1,height=.1]; \n")
		archivo.write("node0 [label = \"")
		
		tablaTemp = self.tabla
		
		for i in range(0, len(tablaTemp)):
			aux = tablaTemp[i]
			if aux !=  None and aux != 0:
				codigo = str(aux.codigo)
				nombre = aux.nombre
				cadenanueva = cadenanueva + "<f" + str(i) +"> Codigo: "+ str(codigo)+" \\nNombre: "+nombre + " " + str(i)+"  | "
		
		
		cadenanueva2 = cadenanueva[0:(int(len(cadenanueva))-2)]
		
		archivo.write(str(cadenanueva2))
		archivo.write('\",height=2.5];')
		archivo.write('\n }')
		archivo.close()
		print("Archivo Creado")
		
	
					
				
			
			
			
		
		