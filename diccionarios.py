diccionario = {
    'nombre': 'Mateo',
    'edad': 20,
    'estatura': 1.68,
    'hobie': 'Escuchar audiolibros',
    'profesion': 'estudiante',
    'estadoCivil': 'Union libre',
    'colorFavorito': 'Negro',
}


#Accendiendo de forma individual a los atributos y valores de un diccionario
""" print(diccionario.get('edad'))
print(diccionario['edad']) """

#Acceder a todos los atributos y valores de un diccionario al mismo tiempo, recorrer un diccionario

for clave, valor in diccionario.items():
    print(clave, valor)

