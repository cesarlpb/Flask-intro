# Data Types

#%% string
a = "string a"
b = str("string b")
print("1.", a, b)
# Concatenación
print("2. " + a + b) 
print("3. " + a + " " + b)
print(f'4. La variable a es {a} y la b es {b}')
#%% numerics -> int, float, complex
# int
i = 1
print(i + 1)    # Operaciones en la salida
print(i - 3)    
print("Entero: " + str(i))  # Concatenar con casting int -> str
print(f"Interpolando: {i}") # Interpolación de cadena no necesita casting manual
# float
f = 20.12
print(f"Este producto cuesta {f} €.")
# complex
c = 1j # número complejo -> a + b * j
print(c)
print(1 + c)
print(c * 2)
print(c ** 2)

#%% Colecciones
# Array / lista o list
arr = [1, 2, 3]
print(arr)
print(type(arr))    # list

for el in arr:
    el += 1
    print(el)
#%% Tupla o tuple
#mi_arr = [1, 2, "3"] # mala idea
tupla = ("Pepe", 5.0)   # Tupla de alumno (str), nota (float)  

print(tupla)
print(f"({type(tupla[0])}, {type(tupla[1])})")
# print(dir(type(tupla[0]))) # podemos ver todas las opciones de una variable con dir

for el in tupla:
    print(el, type(el))

#%% Rango o range
ran = range(5, 10)
print(ran, type(ran))
# lista de números con range:
print(list(range(10)))      # Obtenemos los dígitos del 0 al 9
print(list(range(1, 11)))    # 1 ... 10 
print(list(range(2, 11, 2))) # pares del 2 al 10
print(list(range(1, 11, 2))) # impares del 1 al 10

suma = 0
# colocamos 101 para que se incluya el 100
for i in range(1, 101):
    suma += i
print(suma) # suma del 1 al 100

# Suma de números pares del 1 al 100
pares = 0
for num in range(2, 101, 2):
    pares += num
print(pares)

#%% Diccionarios o dict
# Alumnos y notas
dic = {"Pepe": 5.0, "María": 7.5, "Juan": 6.75}
print(type(dic))
print(dic)
# print(dic["asas"]) # Como la key no existe en dic -> arroja KeyError

# Frutas
# Declaramos stock inicial
inventario = {"manzanas": 430, "bananas": 312, "naranjas": 525, "peras": 217}
print(f"Stock inicial: {inventario}")
# Añadimos 100 u a las manzanas
inventario["manzanas"] += 100
print(f"Añadimos 100 manzanas: {inventario}")
# Editamos "peras"
inventario["peras"] = 0
print(f"Se agotan las peras: {inventario}")
print("Antes de eliminar peras:", len(inventario))
# Si ya no vamos a esperar o usar la entrada la podemos borrar
del inventario["peras"]
print(f"Ya no necesitamos la entrada: {inventario}")
print("Después de eliminar peras:", len(inventario))

#%% 
inventario = {"manzanas": 430, "bananas": 312, "naranjas": 525, "peras": 217}
# keys y values de un dict
print(f"Llaves: {inventario.keys()}")
print(f"Valores: {inventario.values()}")
print(type(inventario.keys())) # 
llaves = list(inventario.keys())    # lista de las keys de inventario
valores = list(inventario.values()) # lista de los values de inventario
print(llaves)
print(valores)

# Iteración con for / in
print("{")
for key in inventario:
    print(f"\t'{key}': '{inventario[key]}'")
print("}")
