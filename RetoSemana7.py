lista_alumnos = []

print("--- Sistema de Gestión Escolar ---")

while True:
    opcion = input('\n¿Desea agregar un alumno? (1) Sí | (2) Terminar y mostrar promedios: ')
    
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        notas_alumno = []
        
        for i in range(1, 4):
            if i == 1:
                nota = int(input(f'Ingrese la calificación {i} (obligatoria): '))
                notas_alumno.append(nota)
            else:
                resp = input(f'¿Desea agregar la calificación {i}? (s/n): ').lower()
                if resp == 's':
                    nota = int(input(f'Ingrese la calificación {i}: '))
                    notas_alumno.append(nota)
                else:
                    break 
        
        promedio = sum(notas_alumno) / len(notas_alumno)
        
        lista_alumnos.append([nombre, promedio])
        print(f'Registro de {nombre} completado.')

    elif opcion == '2':
        if not lista_alumnos:
            print("No se registraron alumnos.")
        else:
            print('\n--- Resultados Finales ---')
            for alumno in lista_alumnos:
                print(f'Alumno: {alumno[0]} | Promedio Final: {alumno[1]:.2f}')
        break
    else:
        print('Opción no válida, intenta de nuevo.')

print('\nPrograma finalizado.')