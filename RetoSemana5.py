
print('Hola y bienvenido al reto de la semana 5')
entrada = input('Por favor excribe el año actual ')
#primero solicitaremos los datos que cargara el usuario
añoIntro = 0
añoAlea = 0

if entrada.isnumeric() :
    añoIntro = int(entrada)
else :
    print('Por favor introduce unicamente numeros, intentalo nuevamente.')
    exit()

entradaalea = input('Ahora introduce un año Aleatorio ')

if entradaalea.isnumeric() :
    añoAlea = int(entradaalea)
else :
    print('Por favor introduce unicmanete numeros, intentalo nuevamente')
    exit()

#ahora haremos los calculos y lo expresaremos

if añoIntro < añoAlea :
    diferencia = añoAlea - añoIntro

    if diferencia == 1:
         print(f'Falta solo {diferencia} año para el año que introdujiste. ')
    else:
        print(f'Faltan {diferencia} años para el año que introdujiste.')
elif añoIntro > añoAlea:
    diferencia = añoIntro - añoAlea

    if diferencia == 1:
        print(f'Ha pasado solo {diferencia} año desde el año que introdujiste.')
    else:
        print(f'Han pasado {diferencia} años desde el año que introdujiste.')
else:
    print('Has introducido el mismo año que el actual')
