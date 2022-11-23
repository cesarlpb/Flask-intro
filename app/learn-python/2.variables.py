#%% Variables
a = 2
b = 3
a + b
#%% Es posible reasignar o cambiar tipo
x = 1
# código
x = "Algo"
print(x)
# %% Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
# %% Sacamos tipos
print(type(x))
print(type(y))
print(type(z))
#%% Strings
mi_str = "string"
mi_str2 = 'string 2'
mi_str3 = """
    string multilínea
    """
mi_str4 = '''
    otro str multilínea
'''
print(mi_str, mi_str2, mi_str3, mi_str4)
print("inline:", mi_str, mi_str, 1+1, mi_str, "algo más",mi_str, ".")
#%% Case sensitive
var = "una cosa"
Var = "otra cosa"
print(var, Var)
#%% Nombre de variables
_esto_vale = True   # para algunos casos particulares
esto_vale = True    # notación más habitual en Python
estoVale = True     # camelCase no se usa en Python
EstoVale = False    # case sensitive!!!
print(esto_vale, estoVale, EstoVale)
#%% Múltiples asignaciones de vars
x, y, z, a = "X", "Y", "Z", "A"
print(x, y, z, a)
#%% Varias variables = un solo valor
x = y = z = "Valen lo mismo"
print(x, y, z)
#%% Desempaquetar una colección
nums = [1, 2, 3]
uno, dos, tres = nums
print(nums)
print(uno, dos, tres)
#%% Concatenar
print("string" + "otro string")
print("string" + " otro string con espacio")
print("string1", "string2") # salida con espacios
#%% Print de operaciones numéricas

# print("1"-1)  # Esto arroja TypeError en Python
print("1", 1)   # Esto no tiene problema porque no aplica un operando entre tipos
print( 2 * 3 - 1 )
print( 2 * (3 - 1) )

#%% Variables Globales
x = "awesome"

# Función
def my_func():
  print("Python is " + x)
# Fin de función

my_func()
#%% Variable dentro de función
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()                # fantastic

print("Python is " + x) # "awesome"
#%% Variable global desde dentro de fun
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#%% Editar valor de variable global desde dentro de fun
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()    # La fun() reescribe al variable x global

print("Python is " + x) # x es "fantastic"