# Programacion con Python
# Autor: Estudiante Torres LLivipuma Romulo Jesus <rtorresll@est.ups.edu.ec>
# Universidad Politecnica Salesiana

#Cadenas de Texto
#Comillas simples y dobles
print('Romulo Jesus')
print("Torres Llivipuma")

#Comillas triples
print("""Esto es una cadena
    que ocupa
 varias líneas
    puede ecribir y salatar varias lineas hasta que las 
 estime convenientes""")

#Comillas dentro de comillas
print("Las comillas simples ' delimitan cadenas.")
print('Las comillas dobles "&" delimitan cadenas.')

print('Las comillas simples \' delimitan cadenas.')
print("Las comillas dobles \" delimitan cadenas.")

#Caracteres especiales
print("Las comillas dobles \" delimitan cadenas.")
print('Las comillas simples \' delimitan cadenas.')

print("Una línea\nOtra línea")
print("1\t2\t3")

#Cadenas largas
print("Esta línea está cortada en dos líneas de menos de 79 caracteres "
          "partiendo la cadena en dos")
print("Esta línea está cortada en dos líneas de menos de 79 caracteres\
partiendo la cadena en dos")

for i in range(5):
    print("a b c "
          "d e f ")

for i in range(3):
    print("a b c \
d e f ")

nombre = 'Romulo'
edad =19
print(f'\nHola mi Nombre es {nombre} y tengo {edad} ')

dia=17
mes ='9'
anio=2021
print(f"Hoy es Viernes {dia} de {5+int(mes)} del {anio}" )

print("¡Feliz", anio, "!")
print(f"¡Feliz {anio}!")
print("¡Viernes "+ mes)
print(f"Si escribe {{nombre}} se escribirá el valor de la variable nombre, "
      f"en este caso {nombre}.")