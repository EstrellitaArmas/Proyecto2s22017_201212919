import json , requests
import xml.etree.ElementTree as ET
from flask import Flask, request
from ListaDobleEnlazada import ListaDobleEnlazada 
from ListaDobleEnlazada import NodoDoble 
from ArbolAVL import ArbolAVL 
from ArbolAVL import NodoAVL 
from ListaEnlazada import ListaEnlazada 
from ListaEnlazada import Nodo
from ArbolB import NodoB
from ArbolB import ArbolB
from ArbolB import Pagina
from Matriz import Matriz
from Matriz import NodoMatriz

app = Flask("server")

##########################################DASHBOARD###################

listaUsuarios = ListaDobleEnlazada()
historial = ArbolB()
habitaciones = ListaEnlazada()
sistemaPago = ArbolAVL()
matriz = Matriz()

def jsonDefault(object):
    return object.__dict__
############################## USUARIOS #########################
@app.route('/insertarUsuario',methods=['POST']) 
def insertarUsuario():
    parametro = listaUsuarios.validarUser(request.form["user"],request.form["pass"])
    if parametro =="true":
        return "false"
    else:
        listaUsuarios.insertar(NodoDoble(request.form["user"],request.form["pass"],request.form["address"],request.form["phone"],request.form["age"]))
        #historial.insertar(Nodo("Usuario registrado:"+request.form["user"]))
        listaUsuarios.imprimir()
        listaUsuarios.graficarLista()
        return "true"
    
 
@app.route('/validarUsuario',methods=['POST']) 
def validarUsuario():
    parametro = listaUsuarios.validarUser(request.form["user"],request.form["pass"])
    if parametro =="true":
        return "true"
    else:
        return "false"


@app.route('/modificarUsuario',methods=['POST']) 
def modificarUsuario():
    nuevoNodo = NodoDoble(request.form["user"],request.form["pass"],request.form["address"],request.form["phone"],request.form["age"])
    response = listaUsuarios.modificarUsuario(nuevoNodo)
    listaUsuarios.imprimir()
    listaUsuarios.graficarLista()
    return response

@app.route('/eliminarUsuario',methods=['POST']) 
def eliminarUsuario():
    response = listaUsuarios.eliminarUsuario(request.data)
    listaUsuarios.imprimir()
    listaUsuarios.graficarLista()
    return response

@app.route('/usuarios', methods=['POST'])
def cargaUsuarios():
    nombre = ""
    password = ""
    direccion = ""
    telefono = ""
    edad = ""
    usuarios = ET.fromstring(request.data)
    #root = usuarios.getroot()
    for usuario in usuarios.iterfind('usuario'):
        nombre = usuario[0].text
        password = usuario[1].text
        direccion = usuario[2].text
        telefono = usuario[3].text
        edad = usuario[4].text
        
        listaUsuarios.insertar(NodoDoble(nombre,password,direccion,telefono,edad))

    #historial.insertar(Nodo("Usuario registrado:"+nombre))
    listaUsuarios.imprimir()
    listaUsuarios.graficarLista()

    return "successful"


############################## HABITACIONES #########################
@app.route('/habitaciones', methods=['POST'])
def cargaHabitaciones():
    nivel = ""
    numero = ""
    mensajes = ET.fromstring(request.form["xmlTexto"])
    #root = mensajes.getroot()
    for mensaje in mensajes.iterfind('habitacion'):
        nivel = mensaje[0].text #nivel
        numero = mensaje[1].text #numero
        habitaciones.insertar(Nodo(nivel,numero))

    habitaciones.imprimir()
    habitaciones.graficarLista()
    return "successful"

@app.route('/eliminarHabitacion',methods=['POST']) 
def eliminarHabitacion():
    response = habitaciones.eliminar(request.data)
    habitaciones.imprimir()
    habitaciones.graficarLista()
    return response

@app.route('/habitacionesB', methods=['POST'])
def cargaHabitacionesB():
    nivel = ""
    numero = ""
    mensajes = ET.fromstring(request.data)
    #root = mensajes.getroot()
    for mensaje in mensajes.iterfind('habitacion'):
        nivel = mensaje[0].text #nivel
        numero = mensaje[1].text #numero
        habitaciones.insertar(Nodo(nivel,numero))

    habitaciones.imprimir()
    habitaciones.graficarLista()
    return "successful"    

@app.route('/insertarHabitacion', methods= ['POST'])
def insertarHabitacion():
    reservaJson = request.data
    objReserva = json.loads(reservaJson)
    nivel = objReserva["nivel"]
    numero = objReserva["numero"]
    habitaciones.insertar(Nodo(nivel,numero))
    habitaciones.imprimir()
    habitaciones.graficarLista()

############################## RESERVAS #########################
@app.route('/reservas', methods=['POST'])
def cargaReservas():
    cliente = ""
    tarjeta = ""
    fechaSalida = ""
    fechaIngreso = ""
    mensajes = ET.fromstring(request.data)
    for mensaje in mensajes.iterfind('reservacion'):
        total = 0
        contador = 0
        nombreCliente = mensaje[0].text
        tarjeta = mensaje[1].text
        numHabitacion = mensaje[2].text # numero habitacion
        if mensaje[3].tag == "extras": 
            for extra in mensaje[3].iterfind('extra'):
                contador += 1  # No de extras
            if contador > 3 :
                total = (50 * contador)
            else :
                total = (75 * contador)    
                    
            fechaIngreso = mensaje[4].text # fecha ingreso
        else:
            fechaIngreso = mensaje[3].text # fecha ingreso
        for salida in mensaje.iterfind('fechaSalida'):
            fechaSalida = salida.text 
            print str(fechaSalida)

        anio = fechaIngreso[0:4]
        numeroMes = fechaIngreso[4:6]
        dia = fechaIngreso[6:8] 
        mes = matriz.verMes(numeroMes)
        codigo = str(matriz.aumetarContador())

        nuevoNodo = NodoMatriz(mes, numeroMes, anio, dia, codigo)        
        if matriz.existeReservacion(nuevoNodo) == False:      # si no existe reservacion es esa fecha
            matriz.agregarCabecerasMatriz(nuevoNodo)          # verifica y agrega cabeceras si es necesario (mes y anio)
            if matriz.necesitaProfundidad(nuevoNodo) == True: # si ya existe un dia para el mes y anio
                matriz.agregarProfundidad(nuevoNodo)          # agrega dia al mes y anio 
            else:
                matriz.agregarMatriz(nuevoNodo)               # agrega nuevo nodo despues de crear las cabeceras

        
        total += ((int(numHabitacion[0:1])*200) + int(numHabitacion[1:3]))

        print str(anio) + " mes " + str(numeroMes) + "dia" + str(dia) + "Total:" + str(total)
        pagoReserva = NodoAVL(nombreCliente,total,tarjeta)
        sistemaPago.agregarAVL1(pagoReserva)   

        # insertar en historial 
        idFechaIngreso = str(dia) + str(numeroMes) + str(anio)
        historial.crearNodoInsertar(idFechaIngreso,nombreCliente, total, numHabitacion, fechaIngreso , fechaSalida )
            
    
    sistemaPago.graficarArbolAVL()
    matriz.ArchivoMatriz()
    historial.dibujarArbol() 
    return "successful"
                
@app.route('/eliminarReserva',methods=['POST']) 
def eliminarReserva():
    #reservaJson = request.form["reservaJsonStr"]
    reservaJson = request.data
    objReserva = json.loads(reservaJson)
    
    fechaIngreso =  objReserva["fechaIngreso"] # fecha ingreso
    anio = fechaIngreso[0:4]
    numeroMes = fechaIngreso[4:6]
    dia = fechaIngreso[6:8] 
    mes = matriz.verMes(numeroMes)
    
    nuevoNodo = NodoMatriz(mes, numeroMes, anio, dia)
    matriz.eliminarMatriz(nuevoNodo)
    matriz.ArchivoMatriz()
    
    return "successful"
   
@app.route('/insertarReserva', methods=['POST'])
def insertarReserva():
    reservaJson = request.data
    objReserva = json.loads(reservaJson)
    
    total = 0
    contador = 0
    nombreCliente = objReserva["nombreCliente"]
    tarjeta = objReserva["tarjeta"]
    numHabitacion = objReserva["numHabitacion"] # numero habitacion
    fechaIngreso =  objReserva["fechaIngreso"] # fecha ingreso
    fechaSalida =  objReserva["fechaSalida"] # fecha ingreso

    anio = fechaIngreso[0:4]
    numeroMes = fechaIngreso[4:6]
    dia = fechaIngreso[6:8] 
    mes = matriz.verMes(numeroMes)
    
    anioSalida = fechaSalida[0:4]
    numeroMesSalida = fechaSalida[4:6]
    diaSalida = fechaSalida[6:8] 
    mesSalida = matriz.verMes(numeroMesSalida)
    

    while dia < diaSalida or dia == diaSalida:
        print "nuevo dia"
        codigo = str(matriz.aumetarContador())

        nuevoNodo = NodoMatriz(mes, numeroMes, anio, dia)        
        if matriz.existeReservacion(nuevoNodo) == False:      # si no existe reservacion es esa fecha
            #nuevaTabla = TablaHash()
            #nuevaTabla.CrearNodoInsertar(numHabitacion, numHabitacion)  
            codigo = str(matriz.aumetarContador())
            nuevoNodo = NodoMatriz(mes, numeroMes, anio, dia, codigo)        
            matriz.agregarCabecerasMatriz(nuevoNodo)          # verifica y agrega cabeceras si es necesario (mes y anio)
            if matriz.necesitaProfundidad(nuevoNodo) == True: # si ya existe un dia para el mes y anio
                matriz.agregarProfundidad(nuevoNodo)          # agrega dia al mes y anio 
            else:
                matriz.agregarMatriz(nuevoNodo)               # agrega nuevo nodo despues de crear las cabeceras
        else:
            print "verificacion en TablaHash"
        '''        tabla = matriz.tabla
                indice = tabla.direccion(numHabitacion)
                result = tabla.existe(indice)
                if result == True:
                    print "ya existe reservacion para esta habitacion" + str(numHabitacion)
                else:
                    tabla.CrearNodoInsertar(numHabitacion, numHabitacion)  
                    tabla.graficar()  '''        
        dia = str(int(dia) + 1)

    #total += ((int(numHabitacion[0:1])*200) + int(numHabitacion[1:3]))

    #print str(anio) + " mes " + str(numeroMes) + "dia" + str(dia) + "Total:" + str(total)
    #pagoReserva = NodoAVL(nombreCliente,total,tarjeta)
    #sistemaPago.agregarAVL1(pagoReserva)   

    # insertar en historial 
    #idFechaIngreso = str(dia) + str(numeroMes) + str(anio)
    #historial.crearNodoInsertar(idFechaIngreso,nombreCliente, total, numHabitacion, fechaIngreso , fechaSalida )
    
    return "successful"


#################################################################################################
   
@app.route('/hola',methods=['POST'])
def he():
    return "hola Mundo"+ str(request.form["dato"])

@app.route('/hola2',methods=['POST'])
def hola():
    return "hola Mundo"+ str(request.data)

if __name__ == "__main__":
    #app.run(debug=True, host='192.10.1.1')
    #app.run(debug=True, host='192.168.1.3')
    app.run(debug=True, host='127.0.0.1')