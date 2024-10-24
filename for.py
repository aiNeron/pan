empieza = 1
termina = 11
for contador in range(empieza,termina):
     print(contador)
booleano = 20 >= 16
booleano = not(1==1)
print(booleano)

# el for auto incrementa
# el while hay que incremetarlo mas 1
# ejemplos: booleano = True or False, booleano = True and False, booleano = not True, booleano = 18 < 20 True
# booleano = 1 == 1, booleano = empieza == 1 compara dos valores para comprobar si son iguales
#_________|_________|_________
#true     |true     | true
#true     |false    | true
#false    |true     | true
#false    |false    | false

#             and    resultado
#_________|_________|_________
#true     |true     | true
#true     |false    | false
#false    |true     | false
#false    |false    | false

#             not    resultado
#_________|_________|_________
#true     |true     | false
#true     |false    | true
