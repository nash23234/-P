"""
Nombre: Convertir la lista en string
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
Nombre: Validar si es str
"""
def esValido(opcion):
    if (isinstance(opcion, str)):
        return True
    else:
        print("La opción que digitaste es errónea")
        return menu()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Cantidad de indices
"""
def cantidadDeindices(convertirstr):
    if convertirstr == "" or convertirstr==[]:
        return 0
    else:
        return 1+ cantidadDeindices(convertirstr[1:])
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Verificar si el indice se encuentra
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
        if buscar== cadena [0: indicesBuscar]:
            return True
        else:
            return seEncuentraEnstring(buscar,cadena[1:], indicesBuscar)
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Es númerico
Entrada: cadena
salida: True si todos los caracteres de la entrada corresponde a númerico
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
Nombre: Abre el archivo claves
"""
def claves():
    clave2=open("usuario.txt")
    clave=clave2.readlines()
    clave2.close()
    return clave
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Abrir el archivo viaje
"""
def Empresa():
    viaje=open("Empresas.txt")
    viaje1=viaje.readlines()
    viaje.close()
    return viaje1
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Abrir archivo transporte
"""
def transportes():
    transporte=open("Transporte.txt")
    transporte1=transporte.readlines()
    transporte.close()
    return transporte1
"""
Nombre: Boletos de viajes 
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
        return print("Falta código")
    elif(opcion=="3"):
        print("*********************")
        print("* HASTA LUEGO*")
        print("**********************")
    else:
        print("Ningúna opción es correcta")
        return menu()
#------------------------------------------------------------------------------------------------------------------------------------------------
        
"""
Nombre: Esta función sirve para verificar la clave de acceso al menu administrativo
"""
def validarC():
    print("\n")
    print("---------INICIE SESIÓN----------\n")
    usuario=input("Digite el usuario: ")
    contrasena=input("Digite la contraseña: ")
    return validador(usuario,contrasena)

def validarU_aux(usuario,clave):
    if(seEncuentra("usuario:"+usuario + "\n",clave)):
        return"Usuario valido"
    else:
        print("El usuario no existe, por favor registrarse")
        return Crearnuevousuario()

def validarContrasena(contrasena,clave):
    if(seEncuentra("contraseña:"+contrasena + "\n", clave)):
        return menuAdministrativo()
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
Nombre: agregar nuevo usuario
"""
def Crearnuevousuario():
    print("-----------Bienvenido al registro de usuario--------------\n")
    usuario=input("Digite su nombre de usuario:")
    contrasena=input("Digite una contraseña:")
    return agregarUsuario(usuario,contrasena)

def agregarUsuario(usuario,contrasena):
        claves=open("usuario.txt","a")
        claves.write("--------------------------------------------------------------"+"\n")
        claves.write("usuario:"+usuario+"\n")
        claves.write("contraseña:"+contrasena+"\n")
        claves.close()
        print("Usuario agregado con exito")
        return menu()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: funciones administrativas
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
        return print("Falta código")
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
Nombre: Mantenimiento de empresa 
"""
def Gestiondeempresa():
    print("\n")
    print("--------------Gestión  de empresas-----------------------\n")
    print("1-Incluir empresa\n2-Eliminar Empresa\n3-Modificar Viajes\n4-Mostrar todos los viajes\n5-Cantidad de empresas registradas posees\n6-Retonar a menú principal")
    opcion=input("\nDigite una opción:   ")
    viaje=open("Empresas.txt")
    viaje1=viaje.readlines()
    viaje.close()
    if(esValido(opcion)):
        if opcion=="1":
            return IncluirEmpresa()
        elif opcion=="2":
            return EliminarEmpresa()
        elif opcion=="3":
            cedula=input("Digite el número de cédula de la empresa: ")
            return modificarEmpresa(cedula)
        elif opcion=="4":
            return mostrarviajes()
        elif opcion =="5":
            return cantidadDeviajes()
        elif  opcion=="6":
            return menuAdministrativo()
        else:
            print("Ningúna opción es correcta")
            return Gestiondeempresa()

#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Validación de la cédula 
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
Nombre: Agregar empresa de viaje
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
        print("Empresa agregada con exito")
        return Gestiondeempresa()
    else:
        print("Empresa ya registrada")
        return Gestiondeempresa()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Nombre: Función para eliminar los datos del archivo de viaje
"""
def eliminarempresa(viaje2,indice,contador):
    if contador==4:
        return convertirstr(viaje2)
    else:
        print(viaje2[indice].strip())
        viaje2.pop(indice)
        return eliminarempresa(viaje2,indice,contador+1)

def Eliminar2(viaje1,indice,cont,nombre):
    if cont >0:
        return convertirstr(nombre)
    else:
        nombre=[viaje1[indice].rstrip()]
        return Eliminar2(viaje1,indice,cont+1,nombre)
    
def  EliminarEmpresa():
    viaje=open("Empresas.txt")
    viaje1=viaje.readlines()
    cedula=input("Digite la cédula juridica: ")
    transporte=open("Transporte.txt")
    transporte1=transporte.readlines()
    indice=viaje1.index("Cedula: "+cedula+"\n")
    verificar= Eliminar2(viaje1,indice+1,0,[])
    print(verificar)
    if ((verificar +"\n") in transporte1 ) ==False:
        return EliminarEmpresa_aux(cedula)
    else:
        print("\nLa empresa se encuentra asociada a un transporte")
        return Gestiondeempresa()
        

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
Nombre: Para modificar los nombres de las empresas 
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
Nombre: Mostrar todos los viajes
"""
def mostrarviajes():
    print("\n")
    print("-----------VIENDO TODAS LAS EMPRESAS-----------\n")
    viaje = open("Empresas.txt", "r")
    print(viaje.read())
    input("Estos son todos tus viajes.\nPresiona enter para volver a mantenimiento de contactos...")
    return Gestiondeempresa()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Muestra la cantidad de empresas registradas
"""

def cantidadDeviajes():
    print("-----------TOTAL DE EMPRESAS-----------\n")
    viaje = open("Empresas.txt")
    viaje1 = viaje.readlines()
    print(
        f"Tienes {int(cantidadDeindices(viaje1)/4)} empresas en total.")
    viaje.close()
    input("\nPresiona enter para volver al menú principal...")
    return Gestiondeempresa()




#------------------------------------------------------------------------------------------------------------------------------------------------
"""
Funcion: Mostrar las funciones del Menu de gestion de transporte por empresa
Nombre: Gestion de transporte por empresa
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
            return menuAdministrativo
        else:
            print("Ningúna opción es correcta")
            return GestionDetransEmpresa()
#------------------------------------------------------------------------------------------
def validarPlaca( placa,transporte1):
    if (seEncuentra(placa + "\n", transporte1)):
        return False
    else:
        if(cantidadDeindices(placa) == 6 and isinstance(int(placa), int)):
            return True
        else:
            print("ERROR\nLa placa no contiene 6 dígitos exactos")
            return GestionDetransEmpresa()

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
    empresa=input("Digite el nombre de la empresa donde esta asociado el transporte: ")
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
        transporte.write("Modelo:"+modelo+"\n")
        transporte.write("Año:"+ano+"\n")
        transporte.write("Nombre de la empresa: "+empresa+"\n")
        transporte.write("Asientos VIP:"+vip+"\n")
        transporte.write("Asientos clase normal:"+normal+"\n")
        transporte.write("Asientos económicos:"+economico+"\n")
        transporte.write("-------------------------------------"+"\n")
        transporte.close()
        print("Transporte agregada con exito")
        return GestionDetransEmpresa()
    else:
        print("Transporte ya registrado")
        return GestionDetransEmpresa()
#------------------------------------------------------------------------------------------
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
    transporte=open("Transporte.txt")
    transporte1=transporte.readlines()
    placa=input("Digite la placa del transporte: ")
    viaje=open("Empresas.txt")
    viaje1=viaje.readlines()
    indice=transporte1.index("Placa: "+placa+"\n")
    verificarP=verificarT(transporte1,indice+1,0,[])
    if (verificarP +"\n" in viaje1) ==False:
        return EliminarTransporte_aux(placa)
    else:
        print("\nEl transporte se encuentra registrado en una empresa")
        return GestionDetransEmpresa()

def EliminarTransporte_aux(placa):
    transporte=open("Transporte.txt")
    transporte1=transporte.readlines()
    if(seEncuentra(placa+"\n", transporte1)):
        print("-------------------------------------------------------")
        print("Eliminando Transporte\n")
        placa=str(placa)
        indice=transporte1.index("Placa:"+placa+"\n")
        transporte1=eliminarTransporte(transporte1,indice,0)
        transporte.close()
        transporte=open("Transporte.txt","w")
        transporte.write(transporte1)
        transporte.close()
        print("Empresa Eliminada con exito")
        print(".....................................................................................")
        return GestionDetransEmpresa()
    else:
        print("No existe tal placa: ",placa)
        transporte.close()
        return GestionDetransEmpresa()
#------------------------------------------------------------------------------------------
def MostrarTodostranspo():
    print("\n")
    print("-----------VIENDO TODOS LOS TRANSPORTES-----------")
    transporte = open("Transporte.txt", "r")
    print(transporte.read())
    input("Estos son todos tus transportes.\nPresiona enter para volver a mantenimiento de contactos...")
    return GestionDetransEmpresa()

#------------------------------------------------------------------------------------------
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
def cantidadDeVIP():
    print("-----------TOTAL DE ASIENTOS VIP-----------\n")
    transporte= open("Transporte.txt")

    transporte1 = transporte.readlines()
    print(
        f"Tienes {int(cantidadDeindices(transporte1)/7)}  asientos VIP")
    transporte.close()
    input("\nPresiona enter para volver al menú principal...")
    return GestionDetransEmpresa()

def cantidadDenormal():
    print("-----------TOTAL DE ASIENTOS CLASE NORMAL-----------\n")
    transporte= open("Transporte.txt")

    transporte1 = transporte.readlines()
    print(
        f"Tienes {int(cantidadDeindices(transporte1)/7)} asientos clase normal")
    transporte.close()
    input("\nPresiona enter para volver al menú principal...")
    return GestionDetransEmpresa()

def cantidadDeeconomico():
    print("-----------TOTAL DE ASIENTOS ECONÓMICOS-----------\n")
    transporte= open("Transporte.txt")

    transporte1 = transporte.readlines()
    print(
        f"Tienes {int(cantidadDeindices(transporte1)/7)}  asientos económicos")
    transporte.close()
    input("\nPresiona enter para volver al menú principal...")
    return GestionDetransEmpresa()

#------------------------------------------------------------------------------------------
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
Nombre: Para modificar los nombres de las empresas 
"""
def ModificarTransporte(placa):
    transporte1= transportes()
    if (seEncuentra(placa + "\n",transporte1)):
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
            transporte1[indice] = "Empresa: "+empresa + "\n"
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
menu()
