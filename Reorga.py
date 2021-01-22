import os, os.path, getpass, shutil,pyfiglet,sys
from re import split
from os import system

listado=[]
ext=[]
resultado=[]

usuario=getpass.getuser()
directorioNvo= "C:\\Users\\" + usuario + "\\Desktop\\OrganizadorPy"

def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def crearDirectorio():
    try:
        os.mkdir(directorioNvo)
    except OSError:
        print("La creación del directorio %s falló" % directorioNvo)
    else:
        print("Se ha creado el directorio: %s " % directorioNvo)

def listarArchivos(directorio):
       for root, dirs, files in os.walk(directorio):
           for name in files:
               listado.append(os.path.join(root, name))
    
       for e in range(0,len(listado)):
           file = open(directorioNvo +"\\listadoArchivos.txt" ,"a")
           nombreArchivo, extension = os.path.splitext(listado[e])
           ext.append(extension)
           file.write(listado[e] + "\n")
           file.close()

def crearListado(directorio):
    if os.path.isfile(directorioNvo +"\\listadoArchivos.txt"):
        print("Archivo ya existe, se creará uno nuevo.")
        file = open(directorioNvo +"\\listadoArchivos.txt" ,"w")
        file.close()
        print("Archivo Creado")
    else:
        file = open(directorioNvo +"\\listadoArchivos.txt" ,"w")
        file.close()
        print("Archivo Creado")

def crearListadoExtensiones(directorio):
    if os.path.isfile(directorioNvo +"\\ExtensionesArchivos.txt"):
        print("Archivo ya existe, se creará uno nuevo.")
        file = open(directorioNvo +"\\ExtensionesArchivos.txt" ,"w")
        file.close()
        print("Archivo Creado")
    else:
        file = open(directorioNvo +"\\ExtensionesArchivos.txt" ,"w")
        file.close()
        print("Archivo Creado")

def listarExtensiones(directorio):
    for elemento in ext:
        if elemento not in resultado:
            resultado.append(elemento)
            for e in range(0,len(resultado)):
                file = open(directorioNvo +"\\ExtensionesArchivos.txt" ,"a")
                file.write(resultado[e] + "\n")
                file.close()
def crearCarpetasExt():
    for ext in resultado:
        extension=ext
        if os.path.isdir(directorioNvo + "\\" + str(extension).replace(".","").upper()):
            print("Carpeta " + str(extension).upper().replace(".","") + " ya existe")
        else:
            os.mkdir(directorioNvo + "\\" + extension.replace(".","").upper())

def moverArchivos():
    for a in range(0,len(listado)):
        nombreArchivo, extension = os.path.splitext(listado[a])
        arc=os.path.basename(nombreArchivo) 
        ruta = directorioNvo + "\\" + str(extension).replace(".","").upper() + "\\" + arc 

        if os.path.isfile(ruta + extension):
            print("El archivo: " + ruta + " ya existe.\n copie/mueva manualmente, o bien renombre la carpeta Organizador.py y corra el script nuevamente.\n")
        else:
            shutil.move(nombreArchivo + extension, ruta + extension)

def copiarArchivos():
    for a in range(0,len(listado)):
        nombreArchivo, extension = os.path.splitext(listado[a])
        arc=os.path.basename(nombreArchivo) 
        ruta = directorioNvo + "\\" + str(extension).replace(".","").upper() + "\\" + arc 

        if os.path.isfile(ruta + extension):
            print("El archivo: " + ruta + " ya existe.\n copie/mueva manualmente, o bien renombre la carpeta Organizador.py y corra el script nuevamente.\n")
            #print(arc,nombreArchivo)
            #print("Archivo existente, se renombrará a: " + ruta + "I" + extension)
            #shutil.copy2(nombreArchivo + extension, ruta + "I" + extension)
        else:
            shutil.copy2(nombreArchivo + extension, ruta + extension)
            #shutil.move(nombreArchivo + extension, ruta + extension)

def banner(): 
    banner1 = pyfiglet.figlet_format("Reorga.Py", font="slant")
    print(banner1 + "                             -By: Scott-")

def menu():
    banner()
    
    print("\n(1) - Reorganizar una carpeta (Copiar).")
    print("(2) - Reorganizar una carpeta (Mover).\n")
    print("Uso: Reorga.py te ayudará a relizar copia/mover archivos de un directorio a otro, creando carpetas por extensión de archivo evitando duplicidad. ")
    opcion=input("\n Ingrese una opción: ")
    
    if int(opcion) == 1:
        print("(1) - Reorganizar una carpeta (Copiar).")
        ruta=input("Ingrese la ruta dónde desea buscar el archivo.\n Ruta: ")
        crearDirectorio()
        crearListado(ruta)
        crearListadoExtensiones(ruta)
        listarArchivos(ruta)
        listarExtensiones(ruta)
        crearCarpetasExt()
        copiarArchivos()
        print("TAREA FINALIZADA.")
        continuar=input("Desea realizar otra tarea S/N?")
        if continuar == "s" or continuar == "S":
            system("cls")
        elif continuar == "n" or continuar == "N":
            print("Hasta pronto!")
            sys.exit()
    elif int(opcion) == 2:
        print("(2) - Reorganizar una carpeta (Mover).")
        ruta=input("Ingrese la ruta dónde desea buscar el archivo.\n Ruta: ")
        crearDirectorio()
        crearListado(ruta)
        crearListadoExtensiones(ruta)
        listarArchivos(ruta)
        listarExtensiones(ruta)
        crearCarpetasExt()
        moverArchivos()
        print("TAREA FINALIZADA.")
        continuar=input("Desea realizar otra tarea S/N?")
        if continuar == "s" or continuar == "S":
            system("cls")
        elif continuar == "n" or continuar == "N":
            print("Hasta pronto!")
            sys.exit()
    else:
        system("cls")
        menu()


while True:
    menu()





