"""Variables en python """

nombre_docente = "Jorge"

x = 5

puntaje = 9.9

publicado = True

print(puntaje)

# Strings en python

nombre_docente_dos = "Jorge Hurtado"
desc = """
Hola estudiantes 
como estan 
kdoibnbvuwvuobw
"""

# print(nombre_docente_dos)
# print(desc)

print(nombre_docente_dos[0:5])
print(nombre_docente_dos[6:])
# print(nombre_docente_dos[:])

# name = "Jorge"
# last_name = "Hurtado"
# full_name = name + " " + last_name

# full_name2 = f"{name[0:2]} {last_name}"

# print(full_name)
# print(full_name2)

animal = " dragon azul "
print(animal.upper())
print(animal.lower())

print(animal.capitalize())
print(animal.title())

print(animal.strip().title().lower())

print(animal.find("dra"))

print("dra" in animal)
print(animal.replace("azul", "rojo"))
