opcion = 100
i = 0
print('***Empanadas inteligentes***')
print('1. Agregar Clientes: ')
print('2. Mostrar Cliente ')
print('3. Buscar usuario por cedula ')
print('0. Salir')

#LISTA
clientes = []

#DICCIONARIO
cliente = {}



while opcion != 0:
    opcion = int(input('Elija una opcion: '))
    
    if opcion == 1:
        cliente['cedula'] = input('Digite su cedula: ')
        cliente['nombre'] = input('Digite su nombre: ')
        clientes.append(cliente)

    elif opcion == 2:
        print(clientes)

    elif opcion == 3:
        cedula = input('Digitel la cedula que va buscar: ')
        for cliente in clientes:
            if cliente['cedula'] == cedula:
                print(f'Cliente encontrado: {cliente["cedula"]}')
            else:
                print('Usuario no encontrado')        

    elif opcion == 0:
        break
    
    else:
        print('Digite una opción valida')

else:
    print('BYE')