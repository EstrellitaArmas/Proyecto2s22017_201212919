from TablaHash import TablaHash 

class NodoMatriz():
    def __init__ (self, mes=None, numeroMes=None, anio=None, dia=None, codigo=None, tabla=None, arriba=None, abajo=None, derecha=None, izquierda=None, profundidad=None):
        self.mes = mes
        self.numeroMes = numeroMes
        self.anio = anio
        self.dia = dia
        self.codigo = codigo
        self.tabla = TablaHash()
        self.arriba = arriba
        self.abajo = abajo
        self.derecha = derecha
        self.izquierda = izquierda
        self.profundidad = profundidad

class Matriz():
    def __init__ (self):
        self.inicioMes = None
        self.inicioAnio = None
        self.matrizVacia = "si"
        self.digraf = "digraph G{\n"
        self.contador = 0
        self.tabla = None

    def aumetarContador(self):
        self.contador = self.contador + 1
        return self.contador

##################################### VALIDACIONES ###############################
    def existeMes(self, nuevoNodo):         # verifica columnas
        temp = self.inicioMes
        if temp != None:
            while temp != None:
                if temp.mes == nuevoNodo.mes:
                    return True
                temp = temp.derecha
        return False
    
    def existeAnio(self, nuevoNodo):         # verifica filas  
        temp = self.inicioAnio
        if temp != None:
            while temp != None:
                if temp.anio == nuevoNodo.anio:
                    return True
                temp = temp.abajo
        return False     
    
    def obtenerMes(self, nuevoNodo):
        temp = self.inicioMes
        while temp != None:
            if temp.mes == nuevoNodo.mes:
                return temp
            temp = temp.derecha
            
    def obtenerAnio(self, nuevoNodo):
        temp = self.inicioAnio
        while temp != None:
            if temp.anio == nuevoNodo.anio:
                return temp
            temp = temp.abajo
            
    def verMes(self, fecha):
        if fecha == "01":
            return "Enero"
        elif fecha == "02":
            return "Febrero"
        elif fecha == "03":
            return "Marzo"
        elif fecha == "04":
            return "Abril"
        elif fecha == "05":
            return "Mayo"
        elif fecha == "06":
            return "Junio"
        elif fecha == "07":
            return "Julio"
        elif fecha == "08":
            return "Agosto"
        elif fecha == "09":
            return "Septriembre"  
        elif fecha == "10":
            return "Octubre"
        elif fecha == "11":
            return "Noviembre"
        elif fecha == "12":
            return "Diciembre"
        return "No existe ese mes"
    
    def existeReservacion(self, nuevoNodo):
        busqueda = False
        if self.existeMes(nuevoNodo) == True:               # esta en el nodo de un mes en especifico?
            nodoMesTemp = self.obtenerMes(nuevoNodo)        
            if nodoMesTemp.abajo != None:                   # si lo encontro procede a buscar el anio
                temp1 = nodoMesTemp.abajo
                while temp1 != None:                        # mientras hay nodos en los cuales buscar
                    if temp1.anio == nuevoNodo.anio:        # si el anio encontrado corresponde al que se busca?
                        if temp1.profundidad != None:       # si ya tiene mas de una reserva para ese mes y anio
                            temp2 = temp1                   # temp2 para buscar el dia 
                            while temp2 != None:            # mientras hay nodos en los cuales buscar
                                if temp2.dia == nuevoNodo.dia: # si el dia encontrado corresponde al que se busca
                                    print "TABLA HASH EN EL DIA " + str(temp2.dia)
                                    self.tabla = temp2.tabla
                                    busqueda = True         # retorna true
                                temp2 = temp2.profundidad
                        else:                               # si no tiene mas de una reserva para ese mes y anio
                            if temp1.dia == nuevoNodo.dia:  # si el dia encotrado corresponde al que se busca                               
                                print "TABLA HASH EN EL DIA " + str(temp1.dia)
                                self.tabla = temp1.tabla
                                busqueda = True             # retrona true
                    temp1 = temp1.abajo
        return busqueda
    
    def existeTabla(self, nuevoNodo):
        busqueda = False
        if self.existeMes(nuevoNodo) == True:               # esta en el nodo de un mes en especifico?
            nodoMesTemp = self.obtenerMes(nuevoNodo)        
            if nodoMesTemp.abajo != None:                   # si lo encontro procede a buscar el anio
                temp1 = nodoMesTemp.abajo
                while temp1 != None:                        # mientras hay nodos en los cuales buscar
                    if temp1.anio == nuevoNodo.anio:        # si el anio encontrado corresponde al que se busca?
                        if temp1.profundidad != None:       # si ya tiene mas de una reserva para ese mes y anio
                            temp2 = temp1                   # temp2 para buscar el dia 
                            while temp2 != None:            # mientras hay nodos en los cuales buscar
                                if temp2.dia == nuevoNodo.dia: # si el dia encontrado corresponde al que se busca
                                    print "TABLA HASH EN EL DIA " + str(temp2.dia)
                                    return temp2.tabla
                                    busqueda = True         # retorna true
                                temp2 = temp2.profundidad
                        else:                               # si no tiene mas de una reserva para ese mes y anio
                            if temp1.dia == nuevoNodo.dia:  # si el dia encotrado corresponde al que se busca                               
                                print "TABLA HASH EN EL DIA " + str(temp1.dia)
                                return temp1.tabla
                                busqueda = True             # retrona true
                    temp1 = temp1.abajo
        return "no encuentra"
    
###################################### AGREGA COLUMNAS ############################    
    def agregarInicioMes(self, nuevoNodo): #agregarInicioDepartamento
        nuevoNodo1 = NodoMatriz(str(nuevoNodo.mes), str(nuevoNodo.numeroMes), "")
        nuevoNodo1.derecha = self.inicioMes
        self.inicioMes.izquierda = nuevoNodo1
        self.inicioMes = nuevoNodo1
        
    def agregarMedioMes(self, nodo1, nuevoNodo, nodo2): #agregarMedioDepartamento
        nuevoNodo1 = NodoMatriz(str(nuevoNodo.mes), str(nuevoNodo.numeroMes), "")
        nodo1.derecha = nuevoNodo1
        nuevoNodo1.izquierda = nodo1
        nuevoNodo1.derecha = nodo2
        nodo2.izquierda = nuevoNodo1
        
    def agregarFinMes(self, nuevoNodo): #agregarFinDepartamento
        nuevoNodo1 = NodoMatriz(str(nuevoNodo.mes), str(nuevoNodo.numeroMes), "")
        temp = self.inicioMes
        while temp != None:
            aux = temp
            temp = temp.derecha
        aux.derecha = nuevoNodo1
        nuevoNodo1.izquierda = aux
        
####################################### AGREGA FILAS ###############################   
    def agregarInicioAnio(self, nuevoNodo): #agregarInicioEmpresa
        nuevoNodo1 = NodoMatriz("", "", str(nuevoNodo.anio))
        nuevoNodo1.abajo = self.inicioAnio
        self.inicioAnio.arriba = nuevoNodo1
        self.inicioAnio = nuevoNodo1
        
    def agregarMedioAnio(self, nodo1, nuevoNodo, nodo2): #agregarMedioEmpresa
        nuevoNodo1 = NodoMatriz("", "", str(nuevoNodo.anio))
        nodo1.abajo = nuevoNodo1
        nuevoNodo1.arriba = nodo1
        nuevoNodo1.abajo = nodo2
        nodo2.arriba = nuevoNodo1
        
    def agregarFinAnio(self, nuevoNodo): #agregarFinEmpresa
        nuevoNodo1 = NodoMatriz("", "", str(nuevoNodo.anio))
        temp = self.inicioAnio
        while temp != None:
            aux = temp
            temp = temp.abajo
        aux.abajo = nuevoNodo1
        nuevoNodo1.arriba = aux
            
            
    def agregarCabecerasMatriz(self, nuevoNodo):
        if self.existeMes(nuevoNodo) == False:   # si no existe la columna correspondiente al mes a insertar 
            if self.inicioMes == None:           # si no existe ningun mes, se crea
                nuevoNodo1 = NodoMatriz(str(nuevoNodo.mes), str(nuevoNodo.numeroMes), "")
                self.inicioMes = nuevoNodo1
            elif self.inicioMes != None:         # si existen columnas (meses) pero no el que se va insertar 
                temp1 = self.inicioMes           # variable temporal del nodo inicio para la busqueda
                numeroMes = nuevoNodo.numeroMes  # variable temporal del nodo a insertar para comparar       
                while temp1 != None:             
                    numeroMes1 = temp1.numeroMes # var temporal para comparar el nodo actual
                    if temp1.derecha != None:    # si el nodo actual no es la ultimo 
                        temp2 = temp1.derecha    # var temporal para el nodo siguiente del nodo actual    
                        numeroMes2 = temp2.numeroMes 
                        if numeroMes < numeroMes1:    # si el nodo a insertar es menor al nodo actual
                            self.agregarInicioMes(nuevoNodo) # inserta al inicio 
                            break
                        elif numeroMes > numeroMes1:  # si el nodo a insertar es mayor al nodo actual
                            if numeroMes < numeroMes2: # si el nodo a insertar es menor al nodo siguiente
                                self.agregarMedioMes(temp1, nuevoNodo, temp2) # insertar en medio del actual y siguiente
                                break
                            # si el nodo a insertar es mayor al nodo siguiente continua la busqueda 
                        elif numeroMes == numeroMes1: # si el nodo a insertar es igual al nodo actual
                            # si es igual ya existe la columna  
                            print("ya existe")
                            break                                   
                    else:                           # si el nodo actual es el ultimo
                        if numeroMes < numeroMes1:  # si el nodo a insertar es menor al nodo actual
                            self.agregarInicioMes(nuevoNodo) # inserta al inicio
                            break
                        else:
                            self.agregarFinMes(nuevoNodo)    # inserta al final  
                            break
                    temp1 = temp1.derecha
    
        if self.existeAnio(nuevoNodo) == False:     # si no existe la fila correspondiente el anio a insertar
            if self.inicioAnio == None:             # si no existe ninguna fila, se crea
                nuevoNodo1 = NodoMatriz("", "", str(nuevoNodo.anio))
                self.inicioAnio = nuevoNodo1 
            elif self.inicioAnio != None:           # si existen filas (anios) pero no el que se va insertar
                temp1 = self.inicioAnio             # variable temporal del nodo inicio para la busqueda
                numeroAnio = nuevoNodo.anio         # variable temporal del nodo a insertar para comparar     
                while temp1 != None:
                    numeroAnio1 = temp1.anio        # variable temporal para compara el nodo actual
                    if temp1.abajo != None:         # si el nodo actual no es el ultimo
                        temp2 = temp1.abajo         # variable temporal para el nodo abajo
                        numeroAnio2 = temp2.anio    
                        if numeroAnio < numeroAnio1: # si el nodo a insertar es el menor al nodo actual
                            self.agregarInicioAnio(nuevoNodo) # se crea la fila antes del nodo actual
                            break
                        elif numeroAnio > numeroAnio1: # si el nodo a insertar es mayor al nodo actual
                            if numeroAnio < numeroAnio2: # si el nodo a insertar es menor al nodo abajo
                                self.agregarMedioAnio(temp1, nuevoNodo, temp2) # se crea la fila en medio de ambas
                                break
                            # si el nodo a insertar es mayor al nodo abajo continua la busqueda
                        elif numeroAnio == numeroAnio1:
                            #self.agregarMedioAnio(temp1, nuevoNodo, temp2)      *************************************
                            print ("ya existe")
                            break                                         
                    else:                           # si el nodo actual es el ultimo
                        if numeroAnio < numeroAnio1: # si el nodo a insertar es menor al nodo actual
                            self.agregarInicioAnio(nuevoNodo) # inserta antes del nodo actual
                            break
                        else:                       # si el nodo a insertar es mayor al nodo actual 
                            self.agregarFinAnio(nuevoNodo)  # inserta al final de las filas
                            break        
                    temp1 = temp1.abajo
                    
###################################### AGREGA NODOS #################################                    
    def agregarInicioMatrizMes(self, nodoExistente, nuevoNodo):  #agregarInicioMatrizDepartamento
        cabecera = nodoExistente.izquierda
        cabecera.derecha = nuevoNodo
        nuevoNodo.izquierda = cabecera
        nuevoNodo.derecha = nodoExistente
        nodoExistente.izquierda = nuevoNodo
        #return nuevoNodo#*****************************PRUEBA********************************
        
    def agregarMedioMatrizMes(self, nodo1, nuevoNodo, nodo2):  #agregarMedioMatrizDepartamento
        nodo1.derecha = nuevoNodo
        nuevoNodo.izquierda = nodo1
        nuevoNodo.derecha = nodo2
        nodo2.izquierda = nuevoNodo
        #return nuevoNodo#*****************************PRUEBA********************************
        
    def agregarFinMatrizMes(self, nodoExistente, nuevoNodo):  #agregarFinMatrizDepartamento
        nodoExistente.derecha = nuevoNodo
        nuevoNodo.izquierda = nodoExistente
     
        
    def agregarInicioMatrizAnio(self, nodoExistente, nuevoNodo):  #agregarInicioMatrizEmpresa
        cabecera = nodoExistente.arriba
        cabecera.abajo = nuevoNodo
        nuevoNodo.arriba = cabecera
        nuevoNodo.abajo = nodoExistente
        nodoExistente.arriba = nuevoNodo
        #return nuevoNodo#*****************************PRUEBA********************************
        
    def agregarMedioMatrizAnio(self, nodo1, nuevoNodo, nodo2):  #agregarMedioMatrizEmpresa
        nodo1.abajo = nuevoNodo
        nuevoNodo.arriba = nodo1
        nuevoNodo.abajo = nodo2
        nodo2.arriba = nuevoNodo
        #return nuevoNodo#*****************************PRUEBA********************************
        
    def agregarFinMatrizAnio(self, nodoExistente, nuevoNodo):  #agregarFinMatrizEmpresa
        nodoExistente.abajo = nuevoNodo
        nuevoNodo.arriba = nodoExistente
        #return nuevoNodo#*****************************PRUEBA********************************
                    
                    
    def agregarMatriz(self, nuevoNodo):
        if self.matrizVacia == "no":  # si la matriz no esta vacia
            nodoMesTemp = self.obtenerMes(nuevoNodo)  #obtenerDepartamento    nodoDepartamentoTemp
            nodoAnioTemp = self.obtenerAnio(nuevoNodo)   #obtenerEmpresa   nodoEmpresaTemp
            nodoMesTemp.abajo = nuevoNodo
            nuevoNodo.arriba = nodoMesTemp
            nodoAnioTemp.derecha = nuevoNodo
            nuevoNodo.izquierda = nodoAnioTemp
            self.matrizVacia = "no"
        else:
            nodoMesTemp = self.obtenerMes(nuevoNodo)   # obtiene mes y anio correspondiente al nodo a insertar
            nodoAnioTemp = self.obtenerAnio(nuevoNodo)            
            if nodoMesTemp.abajo == None:               # si el mes no tiene ninguna fila abajo asociada
                nodoMesTemp.abajo = nuevoNodo           
                nuevoNodo.arriba = nodoMesTemp 
                # a continuacion busca el anio al cual enlazar
                if nodoAnioTemp.derecha == None:        # si el anio no tiene columna a la derecha asociada
                    nodoAnioTemp.derecha = nuevoNodo 
                    nuevoNodo.izquierda = nodoAnioTemp
                elif nodoAnioTemp.derecha != None:      # si el anio si tiene columnas a la derecha asociadas 
                    numeroMesNuevo = nuevoNodo.numeroMes 
                    temp1 = nodoAnioTemp.derecha        # *************************************************
                    while temp1 != None:
                        numeroMes1 = temp1.numeroMes    
                        if temp1.derecha != None:       # si el nodo encontrado no es el ultimo
                            temp2 = temp1.derecha       # var temporal del nodo siguiente
                            numeroMes2 = temp2.numeroMes 
                            if numeroMesNuevo < numeroMes1:  # si el nodo a insertar es menor al nodo en curso
                                self.agregarInicioMatrizMes(temp1, nuevoNodo) # inserta antes del nodo en curso
                                break
                            elif numeroMesNuevo > numeroMes1: # si el nodo a insertar es mayor al nodo en curso
                                if numeroMesNuevo < numeroMes2: # si el nodo a insertar en menor al nodo siguiente
                                    self.agregarMedioMatrizMes(temp1, nuevoNodo, temp2) # inserta en medio de ambos
                                    break
                                else:
                                    print(":(")
                            elif numeroMesNuevo == numeroMes1:
                                #self.agregarMedioMatrizMes(temp1, nuevoNodo, temp2)    *********** AQUI IRIA LA PROFUNDIDAD
                                break                                   
                        else:                           # si el nodo encontrado es el ultimo
                            if numeroMesNuevo < numeroMes1: # si el nodo a insertar es menor al nodo actual
                                self.agregarInicioMatrizMes(temp1, nuevoNodo) # se inserta antes del nodo actual
                                break
                            else:
                                self.agregarFinMatrizMes(temp1, nuevoNodo) # si el nodo es mayor al nodo actual se insertal al final
                                break
                        temp1 = temp1.derecha                       
            elif nodoAnioTemp.derecha == None:          # si el anio no tiene ninguna columna derecha asociada
                nodoAnioTemp.derecha = nuevoNodo        #     
                nuevoNodo.izquierda = nodoAnioTemp
                # a continuacion busca el mes al cual enlazar
                if nodoMesTemp.abajo == None:           # si el mes no tiene ninguna fila abajo asociada
                    nodoMesTemp.abajo = nuevoNodo
                    nuevoNodo.arriba = nodoMesTemp 
                elif nodoMesTemp.abajo != None:         # si el mes si tiene filas abajo asociada
                    numeroAnioNuevo = nuevoNodo.anio #caracterNuevoASCII = ord(caracterNuevo)
                    temp1 = nodoMesTemp.abajo                    
                    while temp1 != None:
                        numeroAnio1 =temp1.anio #caracter1ASCII = ord(caracter1)
                        if temp1.abajo != None:
                            temp2 = temp1.abajo
                            numeroAnio2 = temp2.anio #caracter2ASCII = ord(caracter2)
                            if numeroAnioNuevo < numeroAnio1:
                                self.agregarInicioMatrizAnio(temp1, nuevoNodo)
                                break
                            elif numeroAnioNuevo > numeroAnio1:
                                if numeroAnioNuevo < numeroAnio2:
                                    self.agregarMedioMatrizAnio(temp1, nuevoNodo, temp2)
                                    break
                            elif numeroAnioNuevo == numeroAnio1:
                                #self.agregarMedioMatrizAnio(temp1, nuevoNodo, temp2)        *************** O TALVEZ AQUI xD
                                break                                   
                        else:
                            if numeroAnioNuevo < numeroAnio1:
                                self.agregarInicioMatrizAnio(temp1, nuevoNodo)
                                break
                            else:
                                self.agregarFinMatrizAnio(temp1, nuevoNodo)
                                break        
                        temp1 = temp1.abajo                
            else:                                       # si el anio y mes si tienen filas y columnas asociadas
                if nodoAnioTemp.derecha != None: 
                    numeroMesNuevo = nuevoNodo.numeroMes #
                    temp1 = nodoAnioTemp.derecha        #*************************************************
                    while temp1 != None:
                        numeroMes1 = temp1.numeroMes    
                        if temp1.derecha != None:
                            temp2 = temp1.derecha
                            numeroMes2 = temp2.numeroMes 
                            if numeroMesNuevo < numeroMes1:
                                self.agregarInicioMatrizMes(temp1, nuevoNodo)
                                break
                            elif numeroMesNuevo > numeroMes1:
                                if numeroMesNuevo < numeroMes2:
                                    self.agregarMedioMatrizMes(temp1, nuevoNodo, temp2)
                                    break
                                else:
                                    print(":(")
                            elif numeroMesNuevo == numeroMes1:
                                #self.agregarMedioMatrizMes(temp1, nuevoNodo, temp2)    ************** o NO SE QUE DICEN UDS.. SERA QUE ES AQUI??
                                break                                   
                        else:
                            if numeroMesNuevo < numeroMes1:
                                self.agregarInicioMatrizMes(temp1, nuevoNodo)
                                break
                            else:
                                self.agregarFinMatrizMes(temp1, nuevoNodo)
                                break
                        temp1 = temp1.derecha   
                if nodoMesTemp.abajo != None:
                    numeroAnioNuevo = nuevoNodo.anio #caracterNuevoASCII = ord(caracterNuevo)
                    temp1 = nodoMesTemp.abajo                    
                    while temp1 != None:
                        numeroAnio1 = temp1.anio #caracter1ASCII = ord(caracter1)
                        if temp1.abajo != None:
                            temp2 = temp1.abajo
                            numeroAnio2 =temp2.anio #caracter2ASCII = ord(caracter2)
                            if numeroAnioNuevo < numeroAnio1:
                                self.agregarInicioMatrizAnio(nuevoNodo)
                                break
                            elif numeroAnioNuevo > numeroAnio1:
                                if numeroAnioNuevo < numeroAnio2:
                                    self.agregarMedioMatrizAnio(temp1, nuevoNodo, temp2)
                                    break
                            elif numeroAnioNuevo == numeroAnio1:
                                #self.agregarMedioMatrizAnio(temp1, nuevoNodo, temp2)   ******* YA TENGO SUENIO YA NO SE QUE ESTOY HACIENDO xD
                                break                                   
                        else:
                            if numeroAnioNuevo < numeroAnio1:
                                self.agregarInicioMatrizAnio(temp1, nuevoNodo)
                                break
                            else:
                                self.agregarFinMatrizAnio(temp1, nuevoNodo)
                                break        
                        temp1 = temp1.abajo
                        #********************************************
                        
###################################### PROFUNDIDAD ####################################                        
    def necesitaProfundidad(self, nuevoNodo):
        if self.existeMes(nuevoNodo) == True:           # si existe el mes donde se va insertar 
            nodoMesTemp = self.obtenerMes(nuevoNodo)    # obtiene del nodo donde se va insertar
            if nodoMesTemp.abajo != None:               # si el mes corresponde a mas filas
                temp1 = nodoMesTemp.abajo               
                while temp1 != None:                    # mientras no llege al final
                    if temp1.anio == nuevoNodo.anio:    # si el anio del nodo actual es igual al nodo a insertar
                        return True                     # retorna true, significa que existe el anio y mes donde se va insertar
                    temp1 = temp1.abajo
        return False
    
    def agregarProfundidad(self, nuevoNodo):
        if self.existeMes(nuevoNodo) == True:           # si existe el mes donde se va insertar 
            nodoMesTemp = self.obtenerMes(nuevoNodo)    # obtiene el nodo del mes donde se va insertar
            if nodoMesTemp.abajo != None:               # 
                temp1 = nodoMesTemp.abajo
                while temp1 != None: 
                    if temp1.anio == nuevoNodo.anio:    # si el anio es igual al anio a insertar
                        temp2 = temp1
                        while temp2 != None:            # mientras no haya llegado a la ultima posicion de la profundidad
                            aux = temp2
                            temp2 = temp2.profundidad
                        aux.profundidad = nuevoNodo     # agrega produndidad 
                    temp1 = temp1.abajo
                    
    def mostrarProfundidad(self, nuevoNodo):
        if self.existeMes(nuevoNodo) == True:
            nodoMesTemp = self.obtenerMes(nuevoNodo) 
            if nodoMesTemp.abajo != None:
                temp1 = nodoMesTemp.abajo
                while temp1 != None:
                    if temp1.anio == nuevoNodo.anio:
                        temp2 = temp1
                        while temp2 != None:
                            print("anio: " + str(temp2.anio) + " mes: " + str(temp2.mes) + " dia: " + str(temp2.dia))
                            temp2 = temp2.profundidad
                    temp1 = temp1.abajo
   
###################################### GRAFICA ########################################                 
    def ArchivoMatriz(self):
        texto="digraph G{"+"\n"+"rankdir=UD; \n"+"node [shape=box];"+"\n"
        texto+="{ \n rank=min; \n"
        texto+="m[label=""Matriz""]; \n"
        outfile = open("Matriz.txt", 'w')
        temp=self.inicioMes
        while temp!=None:
            ident=""
            for letra in temp.mes:
                ident+=str(ord(letra))
            texto+="x"+str(ident)+'[label="'+str(temp.mes)+'"]; \n'
            temp=temp.derecha
        texto+="} \n"
    
        temp2=self.inicioAnio
        while temp2.abajo!=None:
            texto+="{ \n rank=same; \n"
            local=""
            for letra in temp2.anio:
                local+=str(ord(letra))
            texto+="f"+local+'[label="'+str(temp2.anio)+'"]; \n'
            if temp2.derecha!=None:
                temp21=temp2.derecha
                while temp21!=None:
                    contra=""
                    for letra in temp21.codigo:  #for letra in temp21.contrasenia:
                        contra+=str(ord(letra))
                    texto+="n"+str(contra)+'[label="'+str(temp21.dia)+'"]; \n'
                    temp21=temp21.derecha
            temp2=temp2.abajo
            texto+="} \n"
    
        texto+="{ \n rank=max; \n"
        maximo=""
        for letra in temp2.anio:
            maximo+=str(ord(letra))
        texto+="f"+maximo+'[label="'+str(temp2.anio)+'"]; \n'
        if temp2.derecha!=None:
            temp21=temp2.derecha
            while temp21!=None:
                contra=""
                for letra in temp21.codigo:  #for letra in temp21.contrasenia:
                    contra+=str(ord(letra))
                texto+="n"+str(contra)+'[label="'+str(temp21.dia)+'"]; \n'
                temp21=temp21.derecha
        texto+="} \n"
    
        temp3=self.inicioMes
        while temp3.derecha!=None:
            concat=""
            concat2=""
            for letra in temp3.mes:
                concat+=str(ord(letra))
            for letra2 in temp3.derecha.mes:
                concat2+=str(ord(letra2))
            texto+="x"+str(concat)+" -> "+"x"+str(concat2)+"; \n"
            temp3=temp3.derecha
    
        temp4=self.inicioAnio
        while temp4.abajo!=None:
            emp1=""
            emp2=""
            for letra in temp4.anio:
                emp1+=str(ord(letra))
            for letra2 in temp4.abajo.anio:
                emp2+=str(ord(letra2))
    
            texto+="f"+emp1+" -> "+"f"+emp2+"[rankdir=UD]; \n"
            temp4=temp4.abajo
    
        temp5=self.inicioMes
        while temp5!=None:
            if temp5.abajo!=None:
                cadena1=""
                cadena2=""
                for letra in temp5.mes:
                    cadena1+=str(ord(letra))
                for letra1 in temp5.abajo.codigo:   #for letra1 in temp5.abajo.contrasenia:
                    cadena2+=str(ord(letra1))
                texto+="x"+str(cadena1)+" -> "+"n"+str(cadena2)+"; \n"
                aux=temp5.abajo
                while aux.abajo!=None:
                    text1=""
                    text2=""
                    for letra in aux.codigo:   #for letra in aux.contrasenia:
                        text1+=str(ord(letra))
                    for letra2 in aux.abajo.codigo:  #for letra2 in aux.abajo.contrasenia:
                        text2+=str(ord(letra2))
                    texto+="n"+str(text1)+" -> "+"n"+str(text2)+"; \n"
    
                    aux=aux.abajo
    
                    text3=""
                    text4=""
                    for letra in aux.codigo:   #for letra in aux.contrasenia:
                        text3+=str(ord(letra))
                    for letra2 in aux.arriba.codigo:   #for letra2 in aux.arriba.contrasenia:
                        text4+=str(ord(letra2))
                    texto+="n"+str(text3)+" -> "+"n"+str(text4)+"; \n"
            temp5=temp5.derecha
    
        temp6=self.inicioAnio
        while temp6!=None:
            if temp6.derecha!=None:
                cadena1=""
                cadena2=""
                for letra in temp6.anio:   #for letra in temp6.empresa:
                    cadena1+=str(ord(letra))
                for letra2 in temp6.derecha.codigo:   #for letra2 in temp6.derecha.contrasenia:
                    cadena2+=str(ord(letra2))
                texto+="f"+cadena1+" -> "+"n"+str(cadena2)+"[constraint=false]; \n"
    
                temp61=temp6.derecha
                while temp61.derecha!=None:
                    text1=""
                    text2=""
                    for letra in temp61.codigo:   #for letra in temp61.contrasenia:
                        text1+=str(ord(letra))
                    for letra2 in temp61.derecha.codigo:   #for letra2 in temp61.derecha.contrasenia:
                        text2+=str(ord(letra2))
                    texto+="n"+str(text1)+" -> "+"n"+str(text2)+"[constraint=false]; \n"
    
                    temp61=temp61.derecha
    
                    text3=""
                    text4=""
                    for letra in temp61.codigo:  #for letra in temp61.contrasenia:
                        text3+=str(ord(letra))
                    for letra2 in temp61.izquierda.codigo:   #for letra2 in temp61.izquierda.contrasenia:
                        text4+=str(ord(letra2))
                    texto+="n"+str(text3)+" -> "+"n"+str(text4)+"[constraint=false]; \n"
    
            temp6=temp6.abajo
    
        cadena1=""
        cadena2=""
        for letra in self.inicioMes.mes:   #for letra in self.inicioDepartamento.departamento:
            cadena1+=str(ord(letra))
        for letra2 in self.inicioAnio.anio:   #for letra2 in self.inicioEmpresa.empresa:
            cadena2+=str(ord(letra2))
        texto+="m ->"+"x"+str(cadena1)+"; \n"
        texto+="m ->"+"f"+str(cadena2)+"; \n"
        texto+="}"
        outfile.write(texto)
        outfile.close()
        
    def graficarProfundidad(self, nuevoNodo):
        if self.existeMes(nuevoNodo) == True:
            nodoMesTemp = self.obtenerMes(nuevoNodo) #esta en el nodo de un departamento en especifico
            if nodoMesTemp.abajo != None:
                temp1 = nodoMesTemp.abajo
                archivo=open('Profundidad.txt','w')             
                archivo.write('digraph G{\n')       
                archivo.write("node [shape = record];\n");
                archivo.write("rankdir = LR;\n");   
                
                while temp1 != None:
                    if temp1.anio == nuevoNodo.anio:
                        temp2 = temp1
                        while temp2 != None:
                            archivo.write("nodo_"+str(temp2.dia) + " [label="+str(temp2.dia)+ "]\n")
                            #print("anio: " + str(temp2.anio) + " mes: " + str(temp2.mes) + " dia: " + str(temp2.dia))
                            temp2 = temp2.profundidad
                        temp2 = temp1
                        while temp2 != None:
                            if temp2.profundidad != None:
                                archivo.write("nodo_"+str(temp2.dia)+" ->"+"nodo_"+str(temp2.profundidad.dia)+"\n")   
                            temp2 = temp2.profundidad
                    temp1 = temp1.abajo  
                archivo.write('}')
                archivo.close()                

   
###################################### ELIMINA NODOS ##################################        
    def eliminarMatriz(self, nuevoNodo):
        if self.existeMes(nuevoNodo) == True:
            nodoMesTemp = self.obtenerMes(nuevoNodo) #esta en el nodo de un mes en especifico
            if nodoMesTemp.abajo != None:
                temp1 = nodoMesTemp.abajo
                while temp1 != None:
                    if temp1.anio == nuevoNodo.anio:
                        temp2 = temp1
                        if temp2.dia == nuevoNodo.dia:
                            if temp2.profundidad != None:
                                tempNuevo = temp2.profundidad
                                tempArriba = temp2.arriba
                                tempAbajo = temp2.abajo
                                tempDerecha = temp2.derecha
                                tempIzquierda = temp2.izquierda
    
                                tempNuevo.arriba = temp2.arriba
                                tempArriba.abajo = tempNuevo
                                tempNuevo.izquierda = temp2.izquierda
                                tempIzquierda.derecha = tempNuevo
                                if tempDerecha != None:
                                    tempNuevo.derecha = temp2.derecha
                                    tempDerecha.izquierda = tempNuevo
                                if tempAbajo != None:
                                    tempNuevo.abajo = temp2.abajo
                                    tempAbajo.arriba = tempNuevo
                                return temp2
                            else:
                                tempArriba = temp2.arriba
                                tempAbajo = temp2.abajo
                                tempDerecha = temp2.derecha
                                tempIzquierda = temp2.izquierda
    
                                tempArriba.abajo = temp2.abajo
                                tempIzquierda.derecha = temp2.derecha
    
                                if tempAbajo != None:
                                    tempAbajo.arriba = temp2.arriba
                                if tempDerecha != None:
                                    tempDerecha.izquierda = temp2.izquierda
                        else:
                            while temp2.profundidad != None:
                                temp3 = temp2.profundidad
                                if temp3.dia == nuevoNodo.dia:
                                    temp2.profundidad = temp3.profundidad
                                    return temp3
                                temp2 = temp2.profundidad
                    temp1 = temp1.abajo