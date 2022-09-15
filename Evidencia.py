
listaClient = []
listaSala = []
reservaciones = []

def menu():
        print("1.-Reservar una Sala")
        print("2.-Editar el nombre del evento")
        print("3.-Consultar las reservaciones existentes para una fecha especifica")
        print("4.-Regsitrar cliente nuevo")
        print("5.-Registrar una sala")
        print("6.-salir")
        menuOpcion = int(input("Seleccione una opcion: "))
        if(menuOpcion == 1):
            #reservacion
            reservacion = newReservacion(listaClient, listaSala, reservaciones)
            if(reservacion != False):
                reservaciones.append(reservacion)
                print(reservaciones)
            menu()
        elif(menuOpcion == 2):
            #editar evento
            editEvento(reservaciones)
            menu()
        elif(menuOpcion == 3):
            # Consultar las reservaciones existentes para una fecha específica.
            consultaReservaciones(reservaciones)
            menu()
        elif(menuOpcion == 4):
            # Registro de clientes
            cliente = newClient(randomKey())
            listaClient.append(cliente)
            print(listaClient)
            menu()
        elif(menuOpcion == 5):
            # Regristro de salas
            sala = newSala(randomKey())
            listaSala.append(sala)
            print(listaSala)
            menu()
        else:
            return 0


def randomKey():
    numero=100
    folio=format(id(numero),"x")
    return folio

from datetime import datetime
fecha = datetime.now()

dt_string = fecha.strftime("%d/%m/%Y %H:%M:%S")


# print("date and time =", dt_string)


def fechaDosDias():
    fechaRes = fecha.day + 2
    return fechaRes

def fechaUnDia():
    diaActual = fecha.day
    return diaActual + 1

def fechaActual():
    diaActual = fecha.day
    return diaActual

def conversionFecha(fechaConvertida):
    # una_fecha = '20/04/2019'
    fecha_dt = datetime.strptime(fechaConvertida, '%d/%m/%Y')
    return fecha_dt

def strFecha(fechastr):
    stringFecha = fechastr.strftime("%d/%m/%Y")
    return stringFecha

# Registrar a un nuevo cliente
def newClient(idClient):
    idClient = idClient
    nameClient = input("Nombre del Cliente: ")
    return idClient, nameClient #regresa lista (idClient, nombre)

# Registrar una sala
def newSala(idSala):
    idSala = idSala
    nameSala = input("Nombre de la Sala: ")
    capacidad = input("Capacidad de la Sala: ")
    return idSala, nameSala, capacidad #regresa lista (idSala, nombre de la sala, capacidad)

# Registrar reservacion de una sala
def newReservacion(listaClient, listaSala, reservaciones):
    nombreCliente = input("\nNombre del Cliente: ")
    if(validacionCliente(listaClient, nombreCliente)):
        nombreSala = input("Nombre de la Sala: ")
        if(validacionSala(listaSala, nombreSala)):
            nombreEvento = input("Nombre del evento: ")
            fechaEvento = input("Fecha del evento en formato d/m/y. Ejemplo: 20/04/2019: ")
            fechaEvento = conversionFecha(fechaEvento)
            if(validacionDias(fechaEvento.day)):
                turno = input("Que turno desea reservar, Formato para turno, 'mañana, 'tarde', noche: ")
                if(turno == 'mañana' or turno == 'tarde' or turno == 'noche'):
                # ('sala2', 'tarde', '18/09/2022', lista)
                    if(disponibilidadSala(nombreSala, turno, strFecha(fechaEvento), reservaciones) != True):
                        folio = randomKey()
                        return nombreCliente, nombreSala, nombreEvento, strFecha(fechaEvento), turno, folio
                    else:
                        print("sala no disponoble en ese turno en esa fecha\n")
                else:
                    print("formato del turno incorrecto\n")
    return False



# a)	La reserva de la sala se debe hacer, por lo menos, dos días antes
def validacionDias(fechaApartada):
    if(fechaUnDia() != fechaApartada and fechaDosDias() != fechaApartada and fechaActual() != fechaApartada and fechaApartada > fechaActual()):
        print("Fecha disponible")
        return True
    else:
        print("Fecha no disponible.\n")
        print("Favor de reservar con dos dias de anticipacion\n")
        return False

# b)	Solamente pueden reservar una sala aquellos que son clientes registrados
def validacionCliente(listaClient, nameClient):
    if(len(listaClient) != 0):
        strClients = str(listaClient).strip("[]")
        strName = str(nameClient).strip("[]")
        if ",".join(strName) in ",".join(strClients):
            print("Cliente encontrado\n")
            return True
        else:
            print("cliente no registrado\n")
            return False
    else:
        print("ningun Cliente registrado\n")
        return False

# validacion de sala existente
def validacionSala(listaSala, nameSala):
    if(len(listaSala) != 0):
        strClients = str(listaSala).strip("[]")
        strName = str(nameSala).strip("[]")
        if ",".join(strName) in ",".join(strClients):
            print("Sala encontrada")
            return True
        else:
            print("Sala no registrada\n")
    else:
        print("ningun Sala registrada\n")
        return False

# validacion de sala con disponibilidad
def disponibilidadSala(sala, turno, fecha, listaReservacion):
    if(len(listaReservacion) != 0):
        for itemReservacion in listaReservacion:
            stritemReservacion = str(itemReservacion).strip("[]")
            strNameSala = str(sala).strip("[]")
            strFecha = str(fecha).strip("[]")
            strTurno = str(turno).strip("[]")
            if ",".join(strFecha) in ",".join(stritemReservacion):
                if ",".join(strNameSala) in ",".join(stritemReservacion):
                    if ",".join(strTurno) in ",".join(stritemReservacion):
                        print('turno encontrado')
                        print(itemReservacion)
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        # print("Ninguna reservacion\n")
        return False


# Consultar las reservaciones existentes para una fecha específica.
def consultaReservaciones(reservaciones):
    fecha = input("que fecha deseas consultar: ")
    fecha = conversionFecha(fecha)
    fecha = strFecha(fecha)
    print("**** Reporte de Reservaciones para el dia ", fecha, " ****\n")
    print("Cliente\t", "Sala\t", "Evento\t", "Turno\t",)
    if(len(reservaciones) != 0):
        for itemReservacion in reservaciones:
            stFecha = str(fecha).strip("[]")
            if stFecha in ",".join(itemReservacion):
                print(itemReservacion[0], "\t", itemReservacion[1], "\t", itemReservacion[2], "\t", itemReservacion[4])
            else:
                print("error")
        print("****** FIN DEL REPORTE ******\n")
    else:
        print("No hay reservaciones aun")
        return False


# Editar evento existente
def editEvento(reservaciones):
    elemento = input("Nombre del evento a modificar: ")
    nuevoElemento = input("Nuevo Nombre: ")
    if(len(reservaciones) != 0):
        for itemReservacion in reservaciones:
            strElement = str(elemento).strip("[]")
            if strElement in ",".join(itemReservacion):
                copia = list(itemReservacion)
                copia[2] = nuevoElemento
                itemReservacion = tuple(copia)
                print(itemReservacion)
                print("Nombre cambiado")
                return reservaciones
            else:
                print("error")

    else:
        print("No hay reservaciones aun")
        return False

menu()