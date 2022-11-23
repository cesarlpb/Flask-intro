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

# Colecciones
