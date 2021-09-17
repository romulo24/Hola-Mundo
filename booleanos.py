# Programacion con Python
# Autor: Estudiante Torres LLivipuma Romulo Jesus <rtorresll@est.ups.edu.ec>
# Universidad Politecnica Salesiana

#Operaciones logicas

#Booleano
#Relacionales
print(10 >= 9)
print("otras palabras" != "otras palabras")
print("test" in "testing")
a = 'testing'
print('test' in a)

#EJERCICIO
a=5
b=7
c=8

print(a>b)
print(a<b)
print(a+b<c)


x= (a + b > c) | (a + b < c)
y=(a + b > c) & (a + b < c)
print(x,y)

#Comparaciones
#Mayor que; < Menor que
3 > 2
#True

3 < 2
#False

#>= Mayor o igual que; <= Menor o igual que
2 >= 1 + 1
#True

4 - 2 <= 1
#False

#== Igual que; != Distinto de
2 == 1 + 1
#Tue

6 / 2 != 3
#False

4 == 3 + 1 > 2
#True

2 != 1 + 1 > 0
#False

4 == 3 + 1 > 2
#True

2 != 1 + 1 > 0
#False
