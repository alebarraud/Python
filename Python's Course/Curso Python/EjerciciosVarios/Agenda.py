def Menu():
    print("*****************************\n")
    print("Bievenido a MiAgenda2022 \n")
    print("1) Ingresar contacto \n")
    print("2) Ver contactos \n")
    print("3) Actualizar contacto \n")
    print("4) Eliminar contacto \n")
    print("5) Bloquear contacto \n")
    print("*****************************\n")
    return input("Disque una opcion \n")

def IngresarContacto(agenda):
    dni = input("Ingrese DNI de la persona que sea agregar \n")
    nombre = input("Ingrese nombre de la persona que sea agregar \n")
    apellido = input("Ingrese apellido de la persona que sea agregar \n")
    nroTelefono = input("Ingrese nroTelefono de la persona que sea agregar \n")
    

Menu()


