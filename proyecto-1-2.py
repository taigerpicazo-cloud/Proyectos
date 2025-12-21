#programa para calcular el imc de una persona

print('calcularemos tu indice de masa corporal')

#aplicamos los datos de validacion
def solicitar_dato(mensaje):
        while True: 
                dato = input(mensaje).strip()
                if dato:
                    return dato
                else:
                       print('Este campo es obligatorio, por favor, ingresa la información')

def solicitar_numero(mensaje, es_entero=False):
       while True:
              dato = solicitar_dato(mensaje)
              try:
                     if es_entero:
                            return int(dato)
                     else:
                            return float(dato)
              except ValueError: 
                     print('Este campo es obligatorio, por favor, ingresa la información')

                     

#solicitud de datos del paciente
nom = solicitar_dato('Escribe tu nombre por favor: ')
apeP = solicitar_dato('Escribe tu apellido paterno por favor: ')
apeM = solicitar_dato('Escribe tu apellido materno por favor: ')
 

# solicitud de datos numericos
ed = solicitar_numero('¿Que edad tienes?: ', es_entero=True)
pes = solicitar_numero('¿Cual es tu peso en kilogramos? (ejemplo 65.7): ')
est = solicitar_numero('¿cual es tu estaura en metros? (ejemplo 1.65): ')

#calculo de imc del usuario
imc = pes / est **2 
#datos oms del indice de masa corporal
if imc <= 18.5:
        clasificacion = 'bajo peso'
elif 18.5 <= imc <24.9:
        clasificacion = 'un peso normal'
elif 25 <= imc < 29.9:
        clasificacion = 'sobrepeso'
else:
        clasificacion = 'obesidad'

#impresion de datos del usuario
print('Tus datos generales basado en tu imc son los siguientes: ')
print(f'nombre del paciente: {nom } {apeP } {apeM }')
print(f'tu edad es de {ed} años. ')
print(f'Basado en la informacion proporcionada ')
print(f'tu IMC es: {imc: .2f}')
print(f'Tu tienes {clasificacion}')

