class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad  

    def imprimir_persona(self):
        print(" nombre: " + self.nombre)
        print(" apellido: " + self.apellido)
        print(" edad: " + self.edad)


class Agenda:
    def __init__(self):
       self.agenda = [] 

    def agregar_persona(self):
        self.nombre = input(" ingrese nombre de la persona que desea agregar a la lista \n")
        self.apellido = input(" ingrese apellido de la persona que desea agregar a la lista \n")
        self.edad = input(" ingrese edad de la persona que desea agregar a la lista \n")
        persona = Persona(self.nombre, self.apellido, self.edad)
        self.agenda = [persona]

    def imprimir_agenda(self):
        for x in self.agenda:
            Persona.imprimir_persona(x)

    def buscar_persona(self):
        self.nombre = input(" ingrese nombre de la persona a buscar \n")
        self.apellido = input(" ingrese apellido de la persona a buscar \n")
        for x in self.agenda:
            if(x.nombre == self.nombre and x.apellido == self.apellido):
                return True
        return False

    def eliminar_persona(self):
        self.nombre = input(" ingrese nombre de la persona a eliminar \n")
        self.apellido = input(" ingrese apellido de la persona a eliminar \n")
        self.posicion = 0
        for x in self.agenda:
            if(x.nombre == self.nombre and x.apellido == self.apellido):
                self.agenda.pop(self.posicion)
                print("Elemento eliminado con exito")
                return
            self.posicion = self.posicion + 1
        print("No se pudo eliminar el elemento ya que no se encuentra en la lista")
    
