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