#Autor: Daniel Niño
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def mostrar_libros_disponibles(self):
        return [libro.mostrar_informacion() for libro in self.libros]

class Libros:
    def __init__(self, titulo, autor, ano_publicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.genero = genero

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.ano_publicacion}, Género: {self.genero}"
    
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)
        
Biblioteca1 = Biblioteca()
X= True
while X == True:
        opcion = input("¿Qué desea hacer? (1: Agregar libro, 2: Ingresar Usuario), 3: Pedir un libro), 4: SALIR) : ")
        if opcion == "1":
         nombre_libro = input("Ingrese el nombre del libro: ")
         autor_libro = input("Ingrese el autor del libro: ")
         ano_libro = input("Ingrese el año de publicación del libro: ")
         genero_libro = input("Ingrese el género del libro: ")
         libro = Libros(nombre_libro, autor_libro, ano_libro, genero_libro)
         Biblioteca1.agregar_libro(libro)
         print("Libros disponibles en la biblioteca:")
         for info in Biblioteca1.mostrar_libros_disponibles():
          print(info)
        elif opcion == "2":
         nombre_usuario = input("Ingrese el nombre del usuario: ")
         id_usuario = input("Ingrese el ID del usuario: ")
         usuario = Usuario(nombre_usuario, id_usuario)
         Biblioteca1.registrar_usuario(usuario)
        elif opcion == "3":
            escoger_usuario= input("Ingrese su ID de usuario: ")
            user_found = None
            for user in Biblioteca1.usuarios:
             if user.id_usuario == escoger_usuario:
              user_found = user
              break
            if not user_found:
             print("Usuario no encontrado. Por favor, registrese primero.")
             continue
            titulo_buscar = input("Ingrese el título del libro que desea pedir: ")
            libro_encontrado = Biblioteca1.buscar_libro(titulo_buscar)
            if libro_encontrado:
             print(f"El libro '{libro_encontrado.titulo}' ha sido prestado.")
            else:
             print("El libro no está disponible en la biblioteca.")
        elif opcion == "4":
            X = False
            print("Saliendo del programa.")
def main():

        if __name__ == "__main__":
         main()
    
