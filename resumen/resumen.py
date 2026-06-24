# 1. Variables y Tipos de Datos Primitivos
print("-------------------")
print("Variables y tipo de datos primitivos")
print("-------------------")
# Creación e invocación de variables primitivas
edad = 25                  # int
altura = 1.75              # float
nombre = "GIC"            # str
es_estudiante = True       # bool

print(f"Hola, me llamo {nombre}, mido {altura}m y tengo {edad} años. ¿Estudio? {es_estudiante}")

# 2. Estructuras de Control (Condicionales y Ciclos/Loops)
print("-------------------")
print("Condicional")
print("-------------------")
#Condicional if, elif, else
clima = "lluvia"

if clima == "soleado":
    print("Vamos a la playa")
elif clima == "lluvia":
    print("Llevo paraguas")
else:
    print("Me quedo en casa")

#for comun recorre un numero fijo
print("-------------------")
print("For")
print("-------------------")
# Imprime los números del 0 al 4
for i in range(5):
    print("Iteración número:", i)

#While repite con una condicion
print("-------------------")
print("While")
print("-------------------")
contador = 0
while contador < 3:
    print("El contador es:", contador)
    contador += 1 # Es lo mismo que contador = contador + 1

#Importante respetar el identado o esapcion de sangrias

#3. Estructuras de Datos
#En py no existen los array pero se usan las listas o list
#listas(list), tupla(tuple), set(set), diccionario(dict)

#A Lista (list)
print("-------------------")
print("List")
print("-------------------")
# Son colecciones ordenadas que puedes modificar en cualquier momento.
# ¿Cuándo usar? Cuando tienes un grupo de elementos (como nombres, números, correos)
# que pueden cambiar, crecer o reducirse en el tiempo.

# Creación
frutas = ["manzana", "banana", "cereza"]

# Invocación y modificación
print(frutas[0])        # Imprime "manzana" (el índice empieza en 0)
frutas.append("kiwi")   # Agrega un elemento al final
frutas[1] = "pera"      # Reemplaza "banana" por "pera"
print(frutas)           # ['manzana', 'pera', 'cereza', 'kiwi']

# B. Tuplas (tuple)
print("-------------------")
print("Tuples")
print("-------------------")
# Iguales a las listas, pero no se pueden modificar una vez creadas.
# ¿Cuándo usar? Cuando tienes datos fijos que no deben alterarse por accidente
# (ej: coordenadas geográficas, configuraciones, meses del año).

# Creación
coordenadas = (40.7128, -74.0060)

# Invocación
print(coordenadas[1])   # Imprime -74.0060
# coordenadas[0] = 50.0 # ¡ESTO DARÁ ERROR! Las tuplas son intocables.

# C. Sets (set)
print("-------------------")
print("Set")
print("-------------------")
# Colecciones desordenadas que no permiten elementos duplicados.
# ¿Cuándo usar? Cuando necesitas eliminar duplicados de una lista rápido,
# o para operaciones matemáticas (uniones, intersecciones).

# Creación
numeros_unicos = {1, 2, 2, 3, 4, 4, 4}

print(numeros_unicos) # Imprime {1, 2, 3, 4} (ignoró los repetidos)
numeros_unicos.add(5) # Agrega el 5

# D. Diccionarios (dict)
print("-------------------")
print("Diccionarios")
print("-------------------")
# Guardan los datos en pares de "llave: valor". En lugar de usar números
# para buscar (como el índice 0 en listas), usas la "llave" (nombre).
# ¿Cuándo usar? Para modelar objetos de la vida real o configuraciones.
# Son excelentes para búsquedas ultra rápidas, como si buscaras una palabra
# en un diccionario real para ver su definición.

# Creación
usuario = {
    "nombre": "Ana",
    "edad": 28,
    "rol": "Admin"
}

# Invocación y modificación
print(usuario["nombre"])  # Imprime "Ana"
usuario["edad"] = 29      # Modifica la edad
usuario["activo"] = True  # Agrega un nuevo par llave:valor
print(usuario)
# print(usuario["Lechuza"]) Da error, ya que no existe esta llave

# 4. Programación Orientada a Objetos (POO)
print("-------------------")
print("Class POO")
print("-------------------")
class Persona:
    #Constructor
    def __init__(self, nombre, edad, rol):
        self.aura = "GIC"       #atributo por default
        self.edad = edad        #atributo
        self.rol = rol          #atributo
        self.nombre = nombre    #atributo

    #Metodos
    def pedir_Ayuda(self):
        print(f"La persona {self.nombre} con edad , {self.edad} y un rol {self.rol}, esta pidiendo ayuda")

    def dar_Ayuda(self, nombre_ayudar: str) -> str:
        frase = f"La persona {self.nombre} va a dar ayuda a la persona {nombre_ayudar}"
        return frase

#Creamos los objetos
persona_1 = Persona("GIC", 29, "Admin")
persona_2 = Persona("GIC2", 20, "Colab")

#Invocamos sus atributos y metodos
print(persona_1.nombre)
print(persona_2)
persona_2.pedir_Ayuda()
persona_1.dar_Ayuda(persona_2.nombre)


# En resumen sobre las estructuras y clases:
# Si solo tienes una lista de nombres sueltos, usa una list.
# Si tienes datos de un usuario, usa un dict.
# Pero si tienes un Usuario que no solo tiene datos (nombre, correo)
# sino que también hace acciones (iniciar sesión, enviar mensaje),
# ahí es momento de usar una Clase.

#Diferencias con respecto a los lenguajes fuertemente estructurados

# 1. Métodos con parámetros que devuelven null y métodos que devuelven Objetos
# En Python, el equivalente a null es None. Por default, si una función o
# método en Python no tiene la palabra reservada return, devuelve None automáticamente.
# Es muy común que los métodos que modifican el estado interno de un objeto (mutadores)
# devuelvan None, mientras que otros devuelvan objetos
# (ya sean de la misma clase o de otras).

print("-------------------")
print("Class POO Diferencias")
print("-------------------")
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.items = []  # Inicializamos una lista vacía

    # Método con parámetros que devuelve None (implícitamente)
    def agregar_producto(self, producto: Producto) -> None:
        self.items.append(producto)
        # No hay 'return', por lo que devuelve None

    # Método que devuelve un Objeto (instancia de Producto)
    def obtener_producto_mas_caro(self) -> Producto:
        if not self.items:
            return None  # Podemos devolver None explícitamente si está vacío

        # Lógica para encontrar el más caro
        producto_caro = max(self.items, key=lambda p: p.precio)
        return producto_caro

#Explicacion del metodo obtener_producto_mas_caro
#En Python, las listas vacías [] se evalúan como False en un contexto booleano
# (a esto se le llama truthiness). Por lo tanto, not self.items significa:
# "Si la lista de items está vacía, no hagas nada y devuelve None".
# Es una forma elegante de evitar un error (Exception) si intentamos
# buscar el máximo en una lista que no tiene nada.

# Linea de producto_caro = max(self.items, key=lambda p: p.precio)
# Si tuvieras una lista de números simple [10, 50, 20], usar la función nativa max()
# es fácil: max([10, 50, 20]) devolvería 50.
#
# El problema: self.items no es una lista de números, es una lista de Objetos de tipo
# Producto. Si tú le dices a Python max(self.items), Python va a lanzar un error
# diciendo: "Oye, tengo dos objetos Producto, ¿cómo se supone que sepa cuál de
# los dos es 'mayor'?".
#
# Ahí es donde entran key y lambda
# La función max() acepta un parámetro opcional llamado key.
# Este parámetro sirve para decirle a Python: "Oye, para saber cuál es el mayor,
# quiero que te fijes específicamente en este atributo de cada objeto"

# En Python, lambda es una palabra reservada para crear una función anónima
# (una función de una sola línea que no tiene nombre ni necesita definirse con def).
# Su estructura es: lambda argumentos: lo_que_devuelve
# Entonces, lambda p: p.precio se traduce mentalmente a esto:
#
# Una función normal haría esto:
# def obtener_precio(p):
#     return p.precio

# Cuando ejecutas max(self.items, key=lambda p: p.precio),
# por debajo Python hace lo siguiente de forma invisible e instantánea:
#
# Toma el primer objeto Producto de la lista y lo pasa a la lambda como la variable p.
#
# La lambda devuelve p.precio (ej. 1.5).
#
# Toma el segundo objeto Producto y lo pasa a la lambda.
#
# La lambda devuelve p.precio (ej. 500.0).
#
# Compara los precios, determina que 500.0 es mayor, y te devuelve el objeto
# original que tenía ese precio.

#IMPORTACIONES DE LIBRERIAS Y CLASES
# A. Importar el módulo completo
# import math
#
# # Tengo que escribir "math." para poder usar la función de raíz cuadrada (sqrt)
# resultado = math.sqrt(25)
# print(resultado)

# B. Importar el módulo completo, pero con un Alias (as)
# # Importo la librería de fechas, pero le digo a Python que en mi código se llamará "fechitas"
# import datetime as fechitas
#
# # Ahora la uso con su alias
# hoy = fechitas.datetime.now()

# C. Importar cosas específicas (from ... import ...)
# from math import sqrt, pi
#
# # Ya no escribo "math.sqrt", uso la función directamente
# resultado = sqrt(25)
# print(f"El valor de pi es: {pi}")

# D. Importar cosas específicas con Alias
# from math import factorial as fact
#
# # Renombré la función "factorial" a simplemente "fact"
# print(fact(5)) # Imprime 120

#Llamado de clases particulares
# # from [nombre_carpeta].[nombre_archivo_sin_py] import [NombreDeLaClase]
# from servicios.pagos import ProcesadorPagos
#
# # Instancio el objeto
# mi_procesador = ProcesadorPagos()
# mi_procesador.cobrar()

#Uso de la libreria Protocol para simular interfaces (averiguar)

# --- CÓMO SE INVOCAN ---
mi_carrito = Carrito()
manzana = Producto("Manzana", 1.5)
tv = Producto("Televisor", 500.0)

# Llamada que devuelve None (solo hace una acción)
mi_carrito.agregar_producto(manzana)
mi_carrito.agregar_producto(tv)

# Llamada que devuelve un objeto
item_caro = mi_carrito.obtener_producto_mas_caro()
print(f"El producto más caro es: {item_caro.nombre} y precio: {item_caro.precio}")  # Imprime: Televisor

# 2. ¿Sobrecarga de Métodos (Method Overloading)?
print("-------------------")
print("Class POO SobreCarga Metodo")
print("-------------------")
# Respuesta corta: No existe de forma nativa como en Java.
# En Java puedes tener sumar(int a, int b) y sumar(int a, int b, int c).
# Si intentas hacer esto en Python, el último método que definas
#  sobreescribirá al anterior.
# ¿Cómo se resuelve en Python? Usando parámetros por defecto (opcionales)
# o un número variable de argumentos (*args).

class Calculadora:
    # Simulamos sobrecarga usando parámetros por defecto (None o 0)
    def sumar(self, a, b, c=None):
        if c is not None:
            return a + b + c
        return a + b

calc = Calculadora()
print(calc.sumar(2, 3))    # Finge ser sumar(a, b) -> Devuelve 5
print(calc.sumar(2, 3, 5)) # Finge ser sumar(a, b, c) -> Devuelve 10

# 3. Múltiples Constructores
print("-------------------")
print("Class POO Múltiples constructores")
print("-------------------")
# Al igual que con la sobrecarga de métodos, en Python solo puedes
# tener un método __init__. Si escribes dos, el último anula al primero.
# ¿Cómo se resuelve? Usando el decorador @classmethod para crear
# "Métodos de Fábrica" (Factory Methods). Esta es la forma más profesional
# y "Pythónica" de tener múltiples constructores.

class Usuario:
    # Este es el constructor principal y ÚNICO
    def __init__(self, username, email):
        self.username = username
        self.email = email

    # "Constructor" alternativo 1: Crear usuario solo desde un email
    @classmethod
    def desde_email(cls, email):
        username = email.split("@")[0] # Extrae lo que está antes del @
        return cls(username, email)    # Llama al __init__ principal

    # "Constructor" alternativo 2: Crear usuario invitado
    @classmethod
    def crear_invitado(cls):
        return cls("Invitado", "sin_correo@ejemplo.com")

# --- CÓMO SE INVOCAN ---
# Usando el constructor normal
user1 = Usuario("pepe123", "pepe@gmail.com")

# Usando los constructores alternativos (Factory Methods)
user2 = Usuario.desde_email("ana@empresa.com")
user3 = Usuario.crear_invitado()

print(user2.username) # Imprime: ana

# 4. Herencia de Clases
print("-------------------")
print("Class POO Herencia de Clases")
print("-------------------")
# La herencia en Python es súper directa.
# Simplemente pones la clase padre entre paréntesis
# al definir la clase hija. Para llamar al constructor del padre,
# usamos super() (igual que en Java).

# Clase Padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Clase Hija
class Gato(Animal):
    def __init__(self, nombre, color):
        # Llamamos al constructor de la clase Animal
        super().__init__(nombre)
        self.color = color

    # Sobreescribimos un método (Overriding) o creamos nuevos
    def maullar(self):
        print("¡Miau!")

# Uso
mi_gato = Gato("Michi", "Negro")
mi_gato.comer()   # Heredado de Animal
mi_gato.maullar() # Propio de Gato

# 5. Clases Abstractas
print("-------------------")
print("Class POO Clases Abstracta")
print("-------------------")
# Python no tiene la palabra reservada abstract ni la palabra interface.
# Todo esto se maneja importando un módulo nativo llamado abc (Abstract Base Classes).
# Una clase abstracta puede tener métodos implementados (con código real)
# y métodos abstractos (que obligan a los hijos a implementarlos).

from abc import ABC, abstractmethod

# Al heredar de ABC, la convertimos en abstracta
class FormaGeometrica(ABC):

    def presentarse(self):  # Método normal (ya implementado)
        print("Soy una forma geométrica.")

    @abstractmethod
    def calcular_area(self):  # Método abstracto (sin implementación)
        pass  # "pass" significa "no hace nada, pasa de largo"


class Cuadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    # Si no implementamos este método, Python dará error al crear el objeto
    def calcular_area(self):
        return self.lado * self.lado


# mi_forma = FormaGeometrica() # ¡ERROR! No se puede instanciar una clase abstracta
mi_cuadrado = Cuadrado(4)
mi_cuadrado.presentarse()
print(f"Área: {mi_cuadrado.calcular_area()}")

#6. Interfaces
print("-------------------")
print("Class POO Interfaces")
print("-------------------")
# Como no existe la palabra interface, en Python una interfaz
# es simplemente una Clase Abstracta donde TODOS sus métodos son abstractos.

from abc import ABC, abstractmethod
# Esto actúa 100% como una Interfaz en Java
class BaseDeDatosInterface(ABC):

    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def guardar(self, datos):
        pass

# Implementación concreta
class MySQLDatabase(BaseDeDatosInterface):
    def conectar(self):
        print("Conectando a MySQL...")

    def guardar(self, datos):
        print(f"Guardando {datos} en MySQL...")

db = MySQLDatabase()
db.conectar()
#TODO
#Arquitectura recomenda en python

# 1. Estructura General de un Proyecto Python (Buenas Prácticas)
# mi_proyecto/
# ├── .venv/                 # Entorno virtual (tus dependencias aisladas, ¡nunca se sube a Git!)
# ├── src/                   # Carpeta principal de tu código fuente
# │   ├── mi_paquete/        # El nombre real de tu aplicación
# │   │   ├── __init__.py    # Indica que esta carpeta es un módulo de Python
# │   │   └── main.py        # Punto de entrada principal
# ├── tests/                 # Pruebas unitarias y de integración (espeja la estructura de src)
# │   ├── __init__.py
# │   └── test_main.py
# ├── .gitignore             # Archivos a ignorar por Git (.venv, __pycache__, etc.)
# ├── requirements.txt       # Lista de dependencias (o pyproject.toml si usas Poetry/Pipenv)
# └── README.md              # Documentación del proyecto

# 2. Arquitectura de un Caso de Uso: Frontend, Backend y Base de Datos
# API + Lógica + BD
# la arquitectura en Python suele dividirse en capas, muy similar a la arquitectura Hexagonal
# o MVC que seguro conoces en Java (como Spring Boot)
# En el desarrollo web moderno con Python, el lenguaje rara vez se encarga del
# Frontend directamente en el navegador (eso lo hace React, Vue o Angular con JavaScript).
# Python actúa como un Backend robusto (API Rest o GraphQL)
#
# mi_paquete/
# ├── main.py                # Inicializa la app (el servidor web)
# ├── api/                   # (Controllers) - Los "Endpoints"
# │   ├── __init__.py
# │   ├── rutas_usuarios.py  # Ej: @app.get("/usuarios")
# │   └── rutas_ventas.py
# ├── core/                  # Configuraciones globales
# │   ├── config.py          # Variables de entorno (URLs, contraseñas)
# │   └── security.py        # Lógica de JWT, encriptación, CORS
# ├── db/                    # La capa de acceso a datos (Database)
# │   ├── __init__.py
# │   ├── session.py         # Configuración de conexión a la BD
# │   └── models.py          # (Entities) - Clases que mapean tablas usando un ORM
# ├── schemas/               # (DTOs) - Validadores de datos de entrada/salida (usando Pydantic)
# │   ├── __init__.py
# │   └── usuario_schema.py
# └── services/              # Lógica de negocio (¡Aquí va lo grueso!)
#     ├── __init__.py
#     └── usuario_service.py # Funciones que la API llama, procesa reglas de negocio y guarda en BD

# ¿Cómo interactúan estas capas? (El flujo de vida de una petición)
# Frontend (Cliente): Una app en React hace un POST a tuservidor.com/usuarios.
#
# API (Controllers): rutas_usuarios.py recibe la petición. Usa schemas para validar
# automáticamente que el JSON recibido tenga los campos correctos (ej.
# que el email tenga arroba).
#
# Services (Lógica): La ruta llama a usuario_service.py. Aquí validas si el
# usuario ya existe, aplicas descuentos, etc.
#
# DB (Modelos): El servicio llama a models.py (usando un ORM como SQLAlchemy,
# que es el "Hibernate" de Python) para guardar el nuevo usuario en
# la base de datos (PostgreSQL, MySQL, etc.).

#Comparativa con Java

