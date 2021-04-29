"""
Nombre: Convertir str
Entrada: Una lista
Salidad: Convierte algún parametro entero a str
Restricción: Si la lista no se encuentra en algún archivo, no se puede volver str
"""
def convertirstr(lista):
    if isinstance(lista, list):
        string = ""
        for indice in lista:
            string += indice
        return string
    else:
        print("Error: no se puede convertir a String, porque, el tipo de dato de entrada, no es una lista")
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Es valido
Entrada: Un valor str
Salida: Validar si la opción digitada es un str
Restricciones: No posee
"""
def esValido(opcion):
    if (isinstance(opcion, str)):
        return True
    else:
        print("La opción que digitaste es errónea")
        return menu()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Generador de número
Entrada: Una lista
Salida: La cantidad de viajes que haya sido registrados en el archivo de viajes
Restricciones: No posee
"""
def generadordeN(lista):
    lista1=convertirstr(lista)
    if (lista==[]):
        return 1
    else:
        return generadordeNA(lista,0)
    
def generadordeNA(lista,conta):
    if (lista==[]):
        return conta // 11 + 1
    else:
        return generadordeNA(lista[1:],conta+1)

def generadordeN1(lista):
    lista1=convertirstr(lista)
    if (lista==[]):
        return 1
    else:
        return generadordeNA1(lista,0)
    
def generadordeNA1(lista,conta):
    if (lista==[]):
        return conta // 11 + 1
    else:
        return generadordeNA1(lista[1:],conta+1)
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Cantidad de indices
Entrada: Un parametro con valor de str
Salida: La cantidad de digitos registrados en un archivo
Restricciones: El parametro debe ser Str
"""
def cantidadDeindices(convertirstr):
    if convertirstr == "" or convertirstr==[]:
        return 0
    else:
        return 1+ cantidadDeindices(convertirstr[1:])

"""
Nombre: Se encuentra
Entrada: Contiene dos parametros, buscar y convertirstr, el parametro buscar es la palabra que vamos a buscar en algún archivo y el parametro convertirstr es para validar si el parametro buscar es un str
Salidad: La palabra o la posición de la palabra a buscar
Restricciones: Que el paramentro sea un str
"""
def seEncuentra(buscar,convertirstr):
    indicesBuscar= cantidadDeindices(buscar)
    if isinstance(convertirstr,list):
        return seEncuentraA(buscar,indicesBuscar,convertirstr,0)
    else:
        return seEncuentraEnstring(buscar,convertirstr,indicesBuscar)

def seEncuentraA(buscar,indicesBuscar,lista,cont):
    if lista == []:
        return False
    else:
        if seEncuentraEnstring(buscar,lista[0],indicesBuscar):
            return True
        else:
            return seEncuentraA(buscar,indicesBuscar,lista[1:],cont +1)

def seEncuentraEnstring(buscar,cadena,indicesBuscar):
    if cadena =="":
        return False
    else:
        if buscar == cadena [0:indicesBuscar]:
            return True
        else:
            return seEncuentraEnstring(buscar,cadena[1:], indicesBuscar)
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Es númerico
Entrada: El parametro de entrada es una cadena de números 
salida: Validar si la cadena de números tiene una cantidad exacta
Restricciones: No posee
"""
def esNumerico(cadena):
    if (cadena ==""):
        return True
    else:
        primerCaracter=cadena[0]
        if(primerCaracter =="0" or primerCaracter =="1" or primerCaracter=="2" or primerCaracter =="3" or primerCaracter =="4"):
            return True and esNumerico(cadena=cadena[1:])
        elif(primerCaracter == "5" or primerCaracter == "6" or primerCaracter == "7" or primerCaracter == "8" or primerCaracter == "9" or primerCaracter =="10"):
            return True and esNumerico(cadena=cadena[1:])
        else:
            return False

#------------------------------------------------------------------------------------------------------------------------------------------------            
"""
Nombre: Clave
Entrada: No posee
Salida: Abrir el archivo de usuarios
Restricciones: No posee
Función: Abrir el archivo de usuarios, que es utilizado para validar las claves de acceso al menú administrativo
"""
def claves():
    clave2=open("usuario.txt")
    clave=clave2.readlines()
    clave2.close()
    return clave
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Empresa
Entrada: No posee
Salida: La información que se encuentra en el archivo empresa
Función: Abrir el archivo de empresas para poder ya sea agregar una empresa, eliminarla, modificarle y mostrar todos sus empresas registradas
"""
def Empresa():
    viaje=open("Empresas.txt")
    viaje1=viaje.readlines()
    viaje.close()
    return viaje1
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Abrir archivo transporte
Entrada: No posee
Salida: No posee
Funcionalidad: Abrir el archivo de Transporte
"""
def transportes():
    transporte=open("Transporte.txt")
    transporte1=transporte.readlines()
    transporte.close()
    return transporte1
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Viajes
Entrada: No posee
Salida: No posee
Funcionalidad: Abrir el archivo de viajes
"""
def viajes():
    viaje2=open("viajes.txt")
    viaje=viaje2.readlines()
    viaje2.close()
    return viaje
"""
Nombre: Reservaciones
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Abrir el archivo de viajes
"""
def reservaciones():
    reservacion=open("reservacion.txt")
    reservacion1=reservacion.readlines()
    reservacion.close()
    return reservacion1
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: menu
Entrada: No posee
Salida: No posee
Funcionalidad: Menú principal para acceder a las funciones que el usuario desee
"""
def menu():
    print("-------------------------------------------------")
    print("*BIENVENIDO AL MENU PRINCIPAL*")
    print("-------------------------------------------------")
    print("Digite una de las siguiente opciones\n ")
    print("1-Opciones Administrativa\n2-Opciones de usuarios normales\n3-Salir\n")
    opcion=input("Digite una de las siguientes opciones:  "   )
    if (opcion=="1"):
        return validarC()
    elif(opcion=="2"):
        return menuusuario()
    elif(opcion=="3"):
        print("*********************")
        print("* HASTA LUEGO*")
        print("**********************")
    else:
        print("Ningúna opción es correcta")
        return menu()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Validar
Entrada: No posee
Salida: No posee
Funcionalidad: Sirve para validar si el usuario se encuentra registrado en el registro de usuarios y si la clave es correspondiente al usurio
"""
def validarC():
    print("\n")
    print("---------INICIE SESIÓN----------\n")
    usuario=input("Digite el usuario: ")
    if usuario=="":
        print("La opción no puede estar vacia")
        return validarC()
    contrasena=input("Digite la contraseña: ")
    if contrasena=="":
        print("La opción no puede estar vacia")
        return validarC()
    return validador(usuario,contrasena)

def validarU_aux(usuario,clave):
    if(seEncuentra("usuario:"+usuario +"\n",clave)):
        return"Usuario valido"
    else:
        print("El usuario no existe, por favor registrarse")
        return Crearnuevousuario()

def validarContrasena(contrasena,clave):
    if(seEncuentra("contraseña:"+contrasena +"\n",clave)):
        return True 
    else:
        print("Contraseña incorrecta,intenta de nuevo")
        return validarC()

def validador(usuario,contrasena):
    clave=claves()
    valiU=validarU_aux(usuario,clave)
    valiC=validarContrasena(contrasena,clave)
    if(valiU and valiC):
        return menuAdministrativo()
    else:
        return False

#------------------------------------------------------------------------------------------------------------------------------------------------

"""
Nombre: Crear nuevo usuario
Entrada: No posee
Salida: No posee
Funcionalidad: Sirve para registrarse en el sistema por si el usuario no se encuentra registrado 
"""
def Crearnuevousuario():
    print("-----------Bienvenido al registro de usuario--------------\n")
    usuario=input("Digite su nombre de usuario:")
    if usuario=="":
        print("La opción no puede estar vacia")
        return Crearnuevousuario()
    contrasena=input("Digite una contraseña:")
    if contrasena=="":
        print("La opción no puede estar vacia")
        return Crearnuevousuario()
    return agregarUsuario(usuario,contrasena)

def agregarUsuario(usuario,contrasena):
        claves=open("usuario.txt","a")
        claves.write("--------------------------------------------------------------"+"\n")
        claves.write("usuario:"+usuario+"\n")
        claves.write("contraseña:"+contrasena+"\n")
        claves.close()
        print("\nUsuario agregado con exito")
        return menu()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Menú administrativo
Entrada: No posee
Salida: No posee
Funcionalidad: Es el menú administrativo donde el usuario podra gestionar diferentes tipos de áreas 
"""
def menuAdministrativo():
    print("\n \n")
    print("-----------Funciones administrativas-------------\n")
    print("Digite una de las siguientes opciones\n")
    print("1-Gestión de empresas\n2-Gestión de transporte por empresa\n3-Gestión de viaje\n4-Consultar historial de reservaciones\n5-Estadisticas de viaje\n6-Retonar al menú principal\n")
    opcion=input("Digite una de las siguiente opciones:   "  )
    if(opcion=="1"):
        return Gestiondeempresa()
    elif(opcion=="2"):
        return GestionDetransEmpresa()
    elif(opcion=="3"):
        return AdministracionViaje()
    elif(opcion=="4"):
        return print("Falta código")
    elif (opcion=="5"):
        return print("Falta código")
    elif(opcion=="6"):
        return menu()
    else:
        print("Ningúna opción es correcta")
        return menuAdministrativo()

#------------------------------------------------------------------------------------------------------------------------------------------------

"""
Nombre: Gestión de empresa
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Deja al usuario modificar el archivo de empresa, ya sea ejecutando las funciones disponibles
"""
def Gestiondeempresa():
    print("\n")
    print("--------------Gestión  de empresas-----------------------\n")
    print("1-Incluir empresa\n2-Eliminar Empresa\n3-Modificar Viajes\n4-Mostrar todos los viajes\n5-Cantidad de empresas registradas posees\n6-Retonar a menú principal")
    opcion=input("\nDigite una opción:   ")
    if(esValido(opcion)):
        if opcion=="1":
            return IncluirEmpresa()
        elif opcion=="2":
            return EliminarEmpresa()
        elif opcion=="3":
            cedula=input("Digite el número de cédula de la empresa: ")
            return modificarEmpresa(cedula)
        elif opcion=="4":
            return mostraempresa()
        elif opcion =="5":
            return cantidadDeempresa()
        elif  opcion=="6":
            return menuAdministrativo()
        else:
            print("Ningúna opción es correcta")
            return Gestiondeempresa()

#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Validar cédula
Entrada: Cédula, viaje1
Salida: No posee
Restricciones: No posee
Funcionalidades: Verificar que las cédulas juridicas a registrar  no se encuentren agregadas anteriormente y que la cédula
sea de 10 digitos exactos
"""
def validarCedula( cedula,viaje1):
    if (seEncuentra(cedula + "\n", viaje1)):
        return False
    else:
        if(cantidadDeindices(cedula) == 10 and isinstance(int(cedula), int)):
            return True
        else:
            print("ERROR\nLa cédula no contiene 10 dígitos exactos")
            return Gestiondeempresa()

"""
Nombre: Incluir empresa
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le pida al usuario la información agregar para la empresa
"""
def IncluirEmpresa():
    print("\n")
    print("----------AGREGANDO EMPRESA--------------")
    cedula=input("Ingrese la cedula juridica:  ")
    nombre=input("Ingrese el nombre de la empresa de viajes:  ")
    ubicacion=input("Ingrese la ubicación de la empresa:   ")
    return agregarEmpresa(cedula,nombre,ubicacion)

def agregarEmpresa(cedula,nombre,ubicacion):
    viaje1=Empresa()
    validarC=validarCedula(cedula,viaje1)
    if(validarC):
        viaje=open("Empresas.txt","a")
        #comienzo agregar los datos
        viaje.write("Cedula: "+cedula+"\n")
        viaje.write("Nombre de la empresa: "+nombre +"\n")
        viaje.write("Ubicación de la empresa: "+ubicacion+"\n")
        viaje.write("-------------------------------------"+"\n")
        viaje.close()
        print("\nEmpresa agregada con exito")
        return Gestiondeempresa()
    else:
        print("Empresa ya registrada")
        return Gestiondeempresa()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Eliminar Empresa
Entrada: Viaje2,indice,contador
Salida: No posee
Restricciones: No posee
Funcionalidad: Mostrar la información de la empresa a eliminar 
"""
def eliminarempresa(viaje2,indice,contador):
    if contador==4:
        return convertirstr(viaje2)
    else:
        print(viaje2[indice].strip())
        viaje2.pop(indice)
        return eliminarempresa(viaje2,indice,contador+1)

"""
Nombre: Eliminar Empresa
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le pide al usuario  que digite el número de cédula juridica de la empresa a eliminar
"""
def  EliminarEmpresa():
    viaje=open("Empresas.txt")
    viaje1=viaje.readlines()
    cedula=input("Digite la cédula juridica: ")
    transporte=open("Transporte.txt")
    transporte1=transporte.readlines()
    indice=viaje1.index("Cedula: "+cedula+"\n")
    verificar=viaje1[indice+1]
    print((verificar) in transporte1)
    if (verificar) in transporte1:
        print("\nLa empresa se encuentra asociada a un transporte")
        return Gestiondeempresa()
    else:
        return EliminarEmpresa_aux(cedula)
"""
Nombre: Eliminar Empresa auxiliar
Entrada: Cédula
Salida: La información de la empresa a seleccionar
Restricciones: Que la cédula se encuentre en el archivo y sea un str
Funcionalidad: Me muestra la información de la empresa que estoy borrando 
"""
def EliminarEmpresa_aux(cedula):
    viaje=open("Empresas.txt")
    viaje2=viaje.readlines()
    if(seEncuentra(cedula+ "\n", viaje2)):
        print("-------------------------------------------------------")
        print("Eliminando Empresa\n")
        indice=viaje2.index("Cedula: "+cedula+"\n")
        viaje2=eliminarempresa(viaje2,indice,0)
        viaje.close()
        viaje=open("Empresas.txt","w")
        viaje.write(viaje2)
        viaje.close()
        print("Empresa Eliminada con exito")
        print(".....................................................................................")
        return Gestiondeempresa()
    else:
        print("No existe ninguna empresa con la cédula: ",cedula)
        viaje.close()
        return Gestiondeempresa()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Función: Sirve para mostrarle al usuario a la hora que esté eliminando o cambiando algo del algún archivo
Nombre : mostrarEmpresa
Entrada: viaje1,indice,cont
Salida: Mostrar la información que el usuario solicite
Restricciones: No posee
"""
def mostrarEmpresa(viaje1, indice, cont):
    if cont > 2:
        print("-----------------------------")
    else:
        if(cont==0):
            print(viaje1[indice][0:-1])
            return mostrarEmpresa(viaje1, indice + 1, cont + 1)
        elif(cont ==1):
            print(viaje1[indice][0:-1])
            return mostrarEmpresa(viaje1,indice +1,cont+1)
        else:
            print(viaje1[indice][0:-1])
            return mostrarEmpresa(viaje1,indice +1 ,cont+1)
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Modificar Empresa
Entrada: Cédula
Salida: No posee
Restricciones: No posee
Funcionales:  Verifica si la cédula de la empresa se encuentra registrada en el archivo
"""
def modificarEmpresa(cedula):
    viaje1= Empresa()
    if (seEncuentra(cedula + "\n", viaje1)):
        print("\n")
        print("Información del contacto seleccionado\n")
        indice = viaje1.index("Cedula: "+cedula + "\n")
        mostrarEmpresa(viaje1, indice, 0)
        EmpresaM= modificarEmpresaA(viaje1, indice + 1, 0)
        viaje = open("Empresas.txt", "w")
        viaje.write(convertirstr(EmpresaM))
        viaje.close()
        print("La empresa ha sido modificada exitosamente")
        return Gestiondeempresa()
    else:
        print("No tienes ninguna empresa con esta cédula juridica", cedula)
        return Gestiondeempresa()

"""
Nombre: Modificar Empresa Auxiliar
Entrada: Viaje, indice, cont
Salida: No posee
Restricciones: No posee
Funcionalidades:  El usuario ingresará la nueva información de la empresa
"""
def modificarEmpresaA(viaje, indice, cont):
    if cont == 2:
        return viaje
    else:
        if cont == 0:
            nuevaInformación = input("Escribe el nuevo nombre de la empresa:  ")
            viaje[indice] ="Nombre de la empresa: "+ nuevaInformación + "\n"
            return modificarEmpresaA(viaje, indice+1, cont+1)
        elif cont == 1:
            nuevaInformación1= input("Escribe la nueva dirección de la empresa: ")
            viaje[indice] ="Ubicación de empresa: "+nuevaInformación1 + "\n"
            return modificarEmpresaA(viaje, indice+1, cont+1)
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Mostrar empresa
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad:  
"""
def mostraempresa():
    print("\n")
    print("-----------VIENDO TODAS LAS EMPRESAS-----------\n")
    viaje = open("Empresas.txt", "r")
    print(viaje.read())
    input("Estos son todos tus viajes.\nPresiona enter para volver al menú administrativo...")
    return Gestiondeempresa()
"""
Nombre cantidad empresa 1
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Muestra al usuario las empresas disponibles para seleccionar
"""
def mostraempresa1():
    print("\n")
    print("-----------VIENDO TODAS LAS EMPRESAS DISPONIBLES-----------\n")
    viaje = open("Empresas.txt", "r")
    print(viaje.read())
    print("Estos son todas tus empresas...")
    return ""
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
def cantidadDeviajes():
    print("-----------TOTAL DE EMPRESAS-----------\n")
    viaje = open("Empresas.txt")
    viaje1 = viaje.read()
    if(viaje1==""):
        print("0")
    else:
        return cantidadDeviaje1()
"""
"""
Nombre: Cantidad de empresas
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Mostra la cantidad de empresas que se encuentra registradas en el archivo empresa
"""
def cantidadDeempresa():
    viaje = open("Empresas.txt")
    viaje1 = viaje.readlines()
    print("MOSTRANDO LA CANTIDAD DE EMPRESAS REGISTRADAS")
    print(f"Tienes {int(cantidadDeindices(viaje1)/4)} empresas en total.")
    viaje.close()
    input("\nPresiona enter para volver al menú principal...")
    return Gestiondeempresa()

#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Gestion de transporte por empresa
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidades: Mostrar al usuarios diferentes tipos de opciones para que pueda modificar el archivo transporte
"""
def GestionDetransEmpresa():
    print("\nBIENVENIDO AL MENU DE GESTIÓN DE TRANSPORTE POR EMPRESA\n")
    print("1-Agregar Transporte\n2-Eliminar Transporte\n3-Modificar Transporte\n4-Mostrar Todos los transportes\n5-Cantidad de transportes registrados\n6-Cantidad de asientos VIP registrados\n7-Cantidad de asientos clase normal registrados\n8-Cantidad de asientos económicos registrados\n9-Retonar a Menú Administrativo")
    opcion=input("\nDigite una de las opciones: ")
    if (esValido(opcion)):
        if (opcion=="1"):
            return agregarTransporte()
        elif(opcion=="2"):
            return EliminarTransporte()
        elif(opcion=="3"):
            placa=input("Digite la placa del transporte: ")
            if(placa==""):
                print("No puede estar vacio")
                return GestionDetransEmpresa()
            else:
                return ModificarTransporte(placa)
        elif(opcion=="4"):
            return MostrarTodostranspo()
        elif (opcion =="5"):
            return cantidadDetransporte()
        elif (opcion =="6"):
            return cantidadDeVIP()
        elif(opcion =="7"):
            return cantidadDenormal()
        elif( opcion =="8"):
            return cantidadDeeconomico()
        elif(opcion=="9"):
            return menuAdministrativo()
        else:
            print("Ningúna opción es correcta")
            return GestionDetransEmpresa()
#------------------------------------------------------------------------------------------
"""
Nombre: Validadr Placa
Entrada: Placa, transporte1
Salida: No posee
Restricciones: No posee
Funcionalidad: Verificar que la placa a agregar no sé encuentre registrada anteriormente y  que posea 6 digitos exactos
"""
def validarPlaca( placa,transporte1):
    if (seEncuentra(placa + "\n", transporte1)):
        return False
    else:
        if(cantidadDeindices(placa) == 6 and isinstance(int(placa), int)):
            return True
        else:
            print("ERROR\nLa placa no contiene 6 dígitos exactos")
            return GestionDetransEmpresa()
"""
Nombre: Agregar transporte
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le pide al usuario la información a agregar del transporte
"""
def agregarTransporte():
    print("\n")
    print("----------AGREGANDO TRANSPORTE--------------")
    placa=input("Ingrese la placa del transporte:  ")
    if placa=="":
        print("La información es vacio")
        return agregarTransporte()
    marca=input("Ingrese la marca del transporte:  ")
    if marca=="":
        print("La información es vacio")
        return agregarTransporte()
    modelo=input("Ingrese el modelo del transporte:   ")
    if modelo=="":
        print("La información es vacio")
        return agregarTransporte()
    ano=input("Digite el año de distribución del transporte: ")
    if ano =="":
        print("La información es vacio")
        return agregarTransporte()
    print("Mostrando todas las empresa")
    print(f"{(mostraempresa1())}")
    print("\n")
    empresa=input("Digite el nombre de la empresa donde quiere asociar el transporte: ")
    if empresa =="":
        print("La información es vacio")
        return agregarTransporte()
    vip=input("Digite cúantos asientos VIP tiene: ")
    if vip=="":
        print("La información es vacio")
        return agregarTransporte()
    normal=input("Digite cúantos asientos de clase normal tiene: ")
    if normal =="":
        print("La información es vacio")
        return agregarTransporte()
    economico=input("Digite cúantos asientos de clase económico tiene: ")
    if economico=="":
        return agregarTransporte()
    return agregarTransporte1(placa,marca,modelo,ano,empresa,vip,normal,economico)

def agregarTransporte1(placa,marca,modelo,ano,empresa,vip,normal,economico):
    transporte1=transportes()
    validarP=validarPlaca(placa,transporte1)
    if(validarP):
        transporte=open("Transporte.txt","a")
        transporte.write("Placa:"+placa+"\n")
        transporte.write("Marca:"+marca +"\n")
        transporte.write("Modelo de Transporte: "+modelo+"\n")
        transporte.write("Año:"+ano+"\n")
        transporte.write("Nombre de la empresa: "+empresa+"\n")
        transporte.write("Asientos VIP:"+vip+"\n")
        transporte.write("Asientos clase normal:"+normal+"\n")
        transporte.write("Asientos económicos:"+economico+"\n")
        transporte.write("\n")
        transporte.close()
        print("Transporte agregada con exito")
        return GestionDetransEmpresa()
    else:
        print("Transporte ya registrado")
        return GestionDetransEmpresa()
#------------------------------------------------------------------------------------------
"""
Nombre: Eliminar Transporte
Entrada: Transporte1,indice,cont
Salida: No posee
Restricciones: No posee
Funcionalidades: Buscar el transporte a eliminar
"""
def eliminarTransporte(transporte1,indice,cont):
    if cont==8:
        return convertirstr(transporte1)
    else:
        print(transporte1[indice].strip())
        transporte1.pop(indice)
        return eliminarTransporte(transporte1,indice,cont+1)

def verificarT(transporte1,indice,cont,nombre):
    if cont > 0:
        return convertirstr(nombre)
    else:
        nombre+=[transporte1[indice].rstrip()]
        return verificarT (transporte1,indice,cont+1,nombre)
    
def  EliminarTransporte():
    placa=input("Digite la placa del transporte: ")
    return EliminarTransporte_aux(placa)

def EliminarTransporte_aux(placa):
    transporte=open("Transporte.txt")
    transporte1=transporte.readlines()
    if(seEncuentra(placa+"\n", transporte1)):
        print("-------------------------------------------------------\n")
        print("Eliminando Transporte\n")
        placa=str(placa)
        indice=transporte1.index("Placa:"+placa+"\n")
        transporte1=eliminarTransporte(transporte1,indice,0)
        transporte.close()
        transporte=open("Transporte.txt","w")
        transporte.write(transporte1)
        transporte.close()
        print("Transporte Eliminado con exito")
        print(".....................................................................................")
        return GestionDetransEmpresa()
    else:
        print("No existe tal placa: ",placa)
        transporte.close()
        return GestionDetransEmpresa()
#------------------------------------------------------------------------------------------
"""
Nombre: Mostrar Todos transporte
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidades: Le muestra al usuario la cantidad de transporte que tiene registrado
"""
def MostrarTodostranspo():
    print("\n")
    print("-----------VIENDO TODOS LOS TRANSPORTES-----------\n")
    transporte=open("Transporte.txt")
    transporte1=transporte.read()
    print(transporte1)
    input("Estos son todos tus transportes.\nPresiona enter para volver a Gestión de transporte")
    return GestionDetransEmpresa()
"""
Nombre: Mostrar todos transporte 1
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le permite al usuario ver los transporte disponibles a la hora de reservar un viaje
"""
def MostrarTodostranspo1():
    print("\n")
    print("-----------VIENDO TODOS LOS TRANSPORTES DISPONIBLES-----------\n")
    transporte=open("Transporte.txt")
    transporte1=transporte.read()
    print(transporte1)
    print("Estos son todos los transportes disponibles....")
    return ""
#------------------------------------------------------------------------------------------
"""
Nombre: Cantidad de transporte
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidades: Le muestra al usuario cuantos transporte se encuentran registrados
"""
def cantidadDetransporte():
    print("-----------TOTAL DE TRANSPORTE-----------\n")
    transporte= open("Transporte.txt")

    transporte1 = transporte.readlines()
    print(
        f"Tienes {int(cantidadDeindices(transporte1)/8)} transportes en total.")
    transporte.close()
    input("\nPresiona enter para volver al menú principal...")
    return GestionDetransEmpresa()
#------------------------------------------------------------------------------------------
"""
Nombre: Cantidad de VIP
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidades: Le muestra al usuario cuantos asientos VIP tiene registrados
"""
def cantidadDeVIP():
    print("-----------TOTAL DE ASIENTOS VIP-----------\n")
    transporte= open("Transporte.txt")
    transporte1 = transporte.readlines()
    print(f"Tienes {int(cantidadDeindices(transporte1)/7)}  asientos VIP")
    transporte.close()
    input("\nPresiona enter para volver al menú principal...")
    return GestionDetransEmpresa()

def cantidadDenormal():
    print("-----------TOTAL DE ASIENTOS CLASE NORMAL-----------\n")
    transporte= open("Transporte.txt")

    transporte1 = transporte.readlines()
    print(f"Tienes {int(cantidadDeindices(transporte1)/7)} asientos clase normal")
    transporte.close()
    input("\nPresiona enter para volver al menú principal...")
    return GestionDetransEmpresa()

def cantidadDeeconomico():
    print("-----------TOTAL DE ASIENTOS ECONÓMICOS-----------\n")
    transporte= open("Transporte.txt")
    transporte1 = transporte.readlines()
    print(f"Tienes {int(cantidadDeindices(transporte1)/7)}  asientos económicos")
    transporte.close()
    input("\nPresiona enter para volver al menú principal...")
    return GestionDetransEmpresa()

#------------------------------------------------------------------------------------------
"""
Nombre: Mostrar transporte
Entrada: Transporte1, indice,cont
Salida: No posee
Restricciones: No posee
Funcionalidades: Le muestra al toda la información de transporte que seleccionó 
"""
def mostrarTransporte(transporte1, indice, cont):
    if cont > 7:
        return True
    else:
        if(cont==0):
            print(transporte1[indice][0:-1])
            return mostrarTransporte(transporte1, indice + 1, cont + 1)
        elif(cont ==1):
            print(transporte1[indice][0:-1])
            return mostrarTransporte(transporte1,indice +1,cont+1)
        elif(cont ==2):
            print(transporte1[indice][0:-1])
            return mostrarTransporte(transporte1,indice +1 ,cont+1)
        elif(cont==3):
            print(transporte1[indice][0:-1])
            return mostrarTransporte(transporte1,indice+1,cont+1)
        elif(cont==4):
            print(transporte1[indice][0:-1])
            return mostrarTransporte(transporte1,indice+1,cont+1)
        elif(cont==5):
            print(transporte1[indice][0:-1])
            return mostrarTransporte(transporte1,indice+1,cont+1)
        elif(cont==6):
            print(transporte1[indice][0:-1])
            return mostrarTransporte(transporte1,indice+1,cont+1)
        else:
            print(transporte1[indice][0:-1])
            return mostrarTransporte(transporte1,indice+1,cont+1)
        
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Modificar Transporte
Entrada: Placa
Salida: No posee
Restricciones: No posee
Funcionalidades: Le muestra al usuario la información del usuario seleccionado
"""
def ModificarTransporte(placa):
    transporte1= transportes()
    if (seEncuentra(placa +"\n",transporte1)):
        print("\n")
        print("Información del transporte seleccionado\n")
        indice = transporte1.index("Placa:"+placa + "\n")
        mostrarTransporte(transporte1, indice, 0)
        transporteM= modificarTransporteA(transporte1, indice + 1, 0)
        transporte = open("Transporte.txt", "w")
        transporte.write(convertirstr(transporteM))
        transporte.close()
        print("El transporte ha sido modificando con exito")
        return GestionDetransEmpresa()
    else:
        print("No tienes ninguna placa con este número", placa)
        return GestionDetransEmpresa()
"""
Nombre: Modificar Transporte Auxiliar
Entrada: Transporte1, indice, cont
Salida: No posee
Restricciones: No posee
Funcionalidad: Le permite al usuario agregar la nueva información del transporte seleccionado
"""
def modificarTransporteA(transporte1, indice, cont):
    if cont == 7:
        return transporte1 
    else:
        if cont == 0:
            marca= input("\nDigite la nueva marca: ")
            transporte1[indice] = "Marca: "+marca + "\n"
            return modificarTransporteA(transporte1, indice+1, cont+1)
        elif cont == 1:
            modelo= input("Digite el nuevo modelo: ")
            transporte1[indice] = "Modelo: "+modelo + "\n"
            return modificarTransporteA(transporte1, indice+1, cont+1)
        elif cont ==2:
            ano=input("Digite el año de transporte: ")
            transporte1[indice]="Año: "+ano + "\n"
            return modificarTransporteA(transporte1,indice+1,cont+1)
        elif cont == 3:
            empresa = input("Digite la empresa asociadad: ")
            transporte1[indice] ="Nombre de la empresa: "+empresa + "\n"
            return modificarTransporteA(transporte1,indice+1,cont+1)
        elif cont==4:
            vip=input("Cantidad de asientos VIP: ")
            transporte1[indice]="Asientos VIP:"+vip+"\n"
            return modificarTransporteA(transporte1,indice+1,cont+1)
        elif cont==5:
            normal=input("Cantidad de asientos clase  normal: ")
            transporte1[indice]="Asientos clase normal:"+normal+"\n"
            return modificarTransporteA(transporte1,indice+1,cont+1)
        else:
            economico=input("Cantidad de asientos económicos: ")
            transporte1[indice]="Asientos económicos:"+economico+"\n"
            return modificarTransporteA(transporte1,indice+1,cont+1)
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Administración de viaje
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le permite al usuario modificar el archivo de viajes , dependiendo las opciones disponibles
"""
def AdministracionViaje():
    print("-------------------GESTIÓN DE VIAJES-----------------------\n")
    print("Digite algunas de las opción\n")
    print("1-Agregar un viaje\n2-Eliminar un viaje\n3-Modificar un viaje\n4-Ver todos los viajes\n5-Mostrar cantidad de viajes registrados\n6-Retornar a menu administrativo")
    opcion=input("\nDigite un opción: ")
    if(esValido(opcion)):
        if (opcion=="1"):
            return agregarViaje()
        elif(opcion=="2"):
            return eliminarViaje1()
        elif(opcion=="3"):
            numero1=input("Digite el número de viaje a modificar: ")
            return modificarA(numero1)
        elif(opcion=="4"):
            return Mostrarviajes()
        elif(opcion=="5"):
            return cantidadDeviajes()
        elif (opcion=="6"):
            return menuAdministrativo()
        else:
            print("Ningúna opción es correcta")
            return AdministracionViaje()
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Agregar viajes
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidades: Le permite al usuario agregar información de un nuevo viaje
"""
def agregarViaje():
    print("\n")
    print("--------------------AGREGANDO VIAJE--------------------\n")
    viaje2=open("viajes.txt")
    viaje=viaje2.readlines()
    numerov=generadordeN(viaje)
    numero1=str(numerov)
    ciudadS=input("La ciudad de salidad: ")
    if (ciudadS==""):
        print("La opción esta vacia: ")
        return agregarViaje()
    fechaS=input("La fecha de salidad: ")
    if(fechaS==""):
        print("La opción esta vacia: ")
        return agregarViaje()
    horaS=input("La hora de salida: ")
    if(horaS==""):
        return agregarViaje()
    ciudadL=input("La ciudad de llegada: ")
    if(ciudadL==""):
        print("La opción es vacia")
        return agregarViaje()
    fechaL=input("La fecha de llegada: ")
    if(fechaL==""):
        print("La opción es vacia")
        return agregarViaje()
    horaL=input("La hora de llegada: ")
    if(horaL==""):
        print("La opción es vacia")
        return agregarViaje()
    print("Mostrando todas las empresa")
    print(f"{(mostraempresa1())}")
    print("\n")
    empresa=input("Nombre de la empresa a elegir: ")
    if (empresa==""):
        print("La opción es vacia")
        return agregarViaje()
    print("Mostrando todos los transportes disponibles")
    print(f"{(MostrarTodostranspo1())}")
    print("\n")
    transporte=input("Modelo del transporte a registrar al viaje: ")
    if (transporte==""):
        print("La opción es vacia")
        return agregarViaje()
    valorv=input("Costo de asiento VIP: ")
    if (valorv==""):
        print("La opción es vacia")
        return agregarViaje()
    valorn=input("Costo de asiento normal: ")
    if(valorn==""):
        print("La opción es vacia")
        return agregarViaje()
    valore=input("Costo asiento económico: ")
    if (valore==""):
        print("La opción es vacia")
        return agregarViaje()
    return agregarViajeA(numero1,ciudadS,fechaS,horaS,ciudadL,fechaL,horaL,empresa,transporte,valorv,valorn,valore)
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Agregar Viaje Auxiliar
Entrada: numero1,ciudadS,fechaS,horaS,ciudadL,fechaL,horaL,empresa,transporte,valorv,valorn,valore
Salida: Agregar la información que el usuario digito para el nuevo viaje
Restricciones: No posee
"""
def agregarViajeA(numero1,ciudadS,fechaS,horaS,ciudadL,fechaL,horaL,empresa,transporte,valorv,valorn,valore):
    viaje=viajes()
    viaje2=open("viajes.txt","a")
    viaje2.write("Número de viaje: "+numero1+"\n")
    viaje2.write("Ciudad de salida: "+ciudadS+"\n")
    viaje2.write("Fecha de salida: "+fechaS+"\n")
    viaje2.write("Hora de salida: "+horaS+"\n")
    viaje2.write("Ciudad de llegada: "+ciudadL+"\n")
    viaje2.write("Fecha de llegada: "+fechaL+"\n")
    viaje2.write("Hora de llegada: "+horaL+"\n")
    viaje2.write("Empresa: "+empresa+"\n")
    viaje2.write("Modelo de Transporte: "+transporte+"\n")
    viaje2.write("Valor de asiento VIP: "+valorv+"\n")
    viaje2.write("Valor de asiento normal: "+valorn+"\n")
    viaje2.write("Valor de asiento económico: "+valore+"\n")
    viaje2.write("------------------------------------------------------"+"\n")
    viaje2.close()
    print("\nViaje agregado con exito")
    return AdministracionViaje()
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Verificar Transporte
Entrada: Transporte1, indice1, count, modelo
Salida: No posee
Restricciones: No posee
Funcionalidades: Revisa si el modelo de un transporte se encuentra registrado en un viaje
"""
"""
def verificarTrans(transporte1,indice1,cont,modelo):
    if cont >0:
        return convertirstr(modelo)
    else:
        modelo=[transporte1[indice1].rstrip()]
        return verificarTrans(transporte1,indice1,cont+1,modelo)
"""
"""
Nombre: Eliminar Viaje
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le pide al usuario el numero de viaje a eliminar
"""
def eliminarViaje1():
    viaje=open("viajes.txt")
    viaje1=viaje.readlines()
    numero1=input("Digite el número de viaje:  ")
    transporte=open("Transporte.txt")
    transporte1=transporte.readlines()
    indice=viaje1.index("Numero de viaje: "+numero1+"\n")
    verificar=viaje1[indice+1]
    print((verificar) in transporte1)
    if (verificar) in transporte1:
        print("\nEl viaje  se encuentra asociado a un transporte")
        return Gestiondeempresa()
    else:
        return EliminarEmpresa_aux(cedula)

"""
Nombre: Eliminar Viaje
Entrada: Numero1
Salida: La eliminación del viaje a buscar
Restricciones: No posee
"""
def eliminarViaje(numero1):
    viaje2=open("viajes.txt")
    viaje=viaje2.readlines()
    if(seEncuentra(numero1+"\n",viaje)):
        print("-------------------------------------------------------")
        print("Eliminando Viaje\n")
        numero1=str(numero1)
        indice=viaje.index("Número de viaje: "+ numero1+"\n")
        numero1=eliminarviajeA(viaje,indice,0)
        viaje2.close()
        viaje2=open("viajes.txt","w")
        viaje2.write(numero1)
        viaje2.close()
        print("Viaje eliminado con exito")
        print(".....................................................................................")
        return AdministracionViaje()
    else:
        print("\nNo existe ese número de viaje: ",numero1)
        viaje2.close()
        return AdministracionViaje()
"""
Nombre: Eliminar Viaje Auxiliar
Entrada: Viaje, indice,cont
Salida: La eliminación de la ubicación donde se encuentra el viaje
Restricciones: No posee
"""
def eliminarviajeA(viaje,indice,cont):
    if cont==13:
        return convertirstr(viaje)
    else:
        print(viaje[indice].strip())
        viaje.pop(indice)
        return eliminarviajeA(viaje,indice,cont+1)
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Mostrar Viajes1
Entrada: Viaje,indice,cont
Salida: No posee
Restricciones: No posee
Funcionalidades: Le muestra al usuario la información del viaje a buscar
"""
def mostrarviajes1(viaje, indice, cont):
    if cont > 11:
        print("-------------------------------------------")
    else:
        if(cont==0):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice + 1,cont+1)
        elif(cont ==1):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1,cont+1)
        elif(cont==2):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
        elif(cont==3):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
        elif(cont==4):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
        elif(cont==5):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
        elif(cont==6):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
        elif(cont==7):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
        elif(cont==8):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
        elif(cont==9):
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
        else:
            print(viaje[indice][0:-1])
            return mostrarviajes1(viaje,indice +1 ,cont+1)
"""
Nombre: Modificar Auxiliar
Entrada: Numero1
Salida: No posee
Restricciones: No posee
Funcionalidad: Verificiar si el viaje se encuentra en el archivo para ser eliminado
"""
def modificarA(numero1):
    viaje= viajes()
    if (seEncuentra(numero1+ "\n", viaje)):
        print("\n")
        print("Información del transporte seleccionado\n")
        indice = viaje.index("Número de viaje: "+numero1 + "\n")
        mostrarviajes1(viaje, indice, 0)
        viaje5= modificarviaje(viaje, indice + 1, 0)
        viaje1= open("viajes.txt", "w")
        viaje1.write(convertirstr(viaje5))
        viaje1.close()
        print("El viaje ha sido modificando con exito")
        return GestionDetransEmpresa()
    else:
        print("No tienes ningún viaje con este número", numero1)
        return GestionDetransEmpresa()

def modificarviaje(viaje, indice, cont):
    if cont == 11:
        return viaje 
    else:
        if cont == 0:
            ciudads= input("\nDigite la nueva ciudad de salida:  ")
            viaje[indice] = "Ciudad de salida: "+ciudads + "\n"
            return modificarviaje(viaje, indice+1, cont+1)
        elif cont == 1:
            fechas= input("Digite la nueva fecha de salida: ")
            viaje[indice] = "Fecha de salida: " + fechas + "\n"
            return modificarviaje(viaje, indice+1, cont+1)
        elif cont ==2:
            horas=input("Digite la nueva hora de salida: ")
            viaje[indice]="Hora de salida:  "+horas + "\n"
            return modificarviaje(viaje,indice+1,cont+1)
        elif cont == 3:
            ciudadl= input("Digite la nueva ciudad de llegada: ")
            viaje[indice] = "Ciudad de llegada: " +ciudadl + "\n"
            return modificarviaje(viaje,indice+1,cont+1)
        elif cont==4:
            fechal=input("Digite la nueva fecha de llegada: ")
            viaje[indice]="Fecha de llegada:  "+fechal+"\n"
            return modificarviaje(viaje,indice+1,cont+1)
        elif cont==5:
            horal=input("Digite la nueva hora de llegada: ")
            viaje[indice]="Hora de llegada: "+horal+"\n"
            return modificarviaje(viaje,indice+1,cont+1)
        elif cont==6:
            empresa=input("Digite la nueva empresa: ")
            viaje[indice]=" Empresa: "+empresa+"\n"
            return modificarviaje(viaje,indice+1,cont+1)
        elif cont==7:
            modelot=input("Digite el nuevo transporte: ")
            viaje[indice]="Modelo de Transporte: "+modelot+"\n"
            return modificarviaje(viaje,indice+1,cont+1)
        elif cont==8:
            valorvip=input("Digite el nuevo valor del asiento VIP: ")
            viaje[indice]="Valor de asiento VIP: "+valorvip+"\n"
            return modificarviaje(viaje,indice+1,cont+1)
        elif cont==9:
            valorn=input("Digite el nuevo valor del asiento clase normal: ")
            viaje[indice]="Valor de asiento normal: "+valorn+"\n"
            return modificarviaje(viaje,indice+1,cont+1)
        else:
            valore=input("Digite el nuevo valor del asiento económico: ")
            viaje[indice]="Valor de asiento económico: "+valore+"\n"
            return modificarviaje(viaje,indice+1,cont+1)
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Mostrar viajes
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le permite al usuario ver toda la información de los viajes registrados
"""
def Mostrarviajes():
    print("\n")
    print("-----------VIENDO TODOS LOS VIAJES-----------\n")
    viaje=open("viajes.txt")
    viaje1= viaje.read()
    if(viaje1 == []):
        return "No tienes ningún viaje"
    else:
        print(viaje1)
        input("Estos son todos tus viajes.\nPresiona enter para volver a mantenimiento de contactos...")
        return AdministracionViaje()
"""
Nombre: Mostrar Viajes1
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le muestra al usuario los viajes disponibles para seleccionar a la hora de reservar un viaje
"""
def Mostrarviajes1():
    print("\n")
    print("-----------VIENDO TODOS LOS VIAJES DISPONIBLES-----------\n")
    viaje=open("viajes.txt")
    viaje1= viaje.read()
    print(viaje1)
    print("\nEstos son todos tus viajes\n...")
    return ""
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Cantidad de viajes
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Le permite al usuario ver la cantidad de viajes registrados posee
"""
def cantidadDeviajes():
    print("-----------TOTAL DE VIAJES-----------\n")
    viaje= open("viajes.txt")
    viaje1 = viaje.readlines()
    print(f"Tienes {int(cantidadDeindices(viaje1)/11)} viajes en total.")
    viaje.close()
    input("\nPresiona enter para volver al menú principal...")
    return AdministracionViaje()
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Menú usuario
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Permite al usuario hacer diferentes actividades, según las opciones disponibles
"""
def menuusuario():
    print("BIENVENIDO AL MENÚ DE USUARIO")
    print("\nDigite una de las siguientes opciones\n")
    print("1-Consulta de viajes\n2-Reservación de viajes\n3-Cancelación de viajes\n4-Salir del menú de usuario\n")
    opcion=input("Digite una opción: ")
    if(esValido(opcion)):
        if opcion=="1":
            return "Falta condigo"
        elif opcion=="2":
            return reservacionviaje()
        elif opcion=="3":
            return menu
        else:
            print("Ningúna opción es correcta")
            return menuusuario()
#--------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Reservación de viaje
Entrada: No posee
Salida: No posee
Restricciones: No posee
Funcionalidad: Permite al usuario reservar un viaje
"""
"""
from datetime import datetime
def reservacionviaje():
    print("\nBIENVENIDO A RESERVACIÓN DE VIAJE.")
    print("\nSe le mostrara las empresas disponibles para un viaje\n")
    print(f"{(Mostrarviajes1())}")
    numeroviaje=input("\nDigite el número de viaje que desea reserva: ")
    if numeroviaje=="":
        print("Esta opción no puede estar vacia")
        return reservacionviaje()
    nombre=input("Digite su nombre: ")
    if nombre=="":
        print("Esta opción no puede estar vacia")
        return reservacionviaje()
    asientovip=input("Digite la cantidad de asientos a reservar clase vip: ")
    if asientovip=="":
        print("Esta opción no puede estar vacia")
        return reservacionviaje()
    asientonormal=input("Digite la cantidad de asientos a reservar clase normal: ")
    if asientonormal=="":
        print("Esta opción no puede estar vacia")
        return reservacionviaje()
    asientoeconomico=input("Digite la cantidad de asientos a reservar clase económico: ")
    if asientoeconomico=="":
        print("Esta opción no puede estar vacia")
        return reservacionviaje()
    return reservacion(numeroviaje,nombre,asientovip,asientonormal,asientoeconomico)
"""
"""
    reserva +=numeroviaje 
    reserva +=nombre
    reserva +=asientovip
    reserva +=asientonormal
    reserva +=asientoeconomico
    print(reserva)
"""
"""
def reservacion(numeroviaje,nombre,asientovip,asientonormal,asientoeconomico):
    reservacion=open("reservacion.txt")
    reservacion.write("Identificador de la reserva: ")
    reservacion.write("Nombre del cliente: "+nombre+"\n")
    reservacion.write("Fecha y hora de la reservación: ")
    reservacion.write("Cantidad asientos VIP: "+asientovip+"\n")
    reservacion.write("Cantidad asientos clase normal: "+asientonormal+"\n")
    reservacion.write("Cantidad asientos clase económico: "+asientoeconomico+"\n")
    reservacion.close()
    print("Viaje reservado con éxito")
    return menuusuario()
 """ 
    
#--------------------------------------------------------------------------------------------------------------------------
menu()
