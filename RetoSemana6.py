# --- Bucle para asegurar que la contraseña inicial sea válida ---
while True:
    pass_inicial = input("Ingrese una contraseña: ")
    
    # Verificamos si la cadena no está vacía y si el primer carácter es número
    if len(pass_inicial) > 0 and pass_inicial[0].isdigit():
        break
    elif len(pass_inicial) == 0:
        print("La contraseña no puede estar vacía")
    else:
        print("La contraseña debe comenzar con un número")

# --- Bucle con FOR para los 3 intentos de confirmación ---
for intento in range(3):
    confirmacion = input("Ingrese la contraseña nuevamente: ")
    
    if confirmacion == pass_inicial:
        print("Contraseña correcta")
        break 
    else:
        intentos_restantes = 2 - intento
        if intentos_restantes > 0:
            print("Las contraseñas no coinciden")
        else:
            print("Las contraseñas no coinciden")

# --- Bloque Final --- 
else:
    print("Demasiados intentos fallidos.")

print("Fin del programa")