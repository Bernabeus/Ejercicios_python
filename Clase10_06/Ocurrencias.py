print('Contar el número de ocurrencias de las palabras en un archivo de texto')
repetidos = {}

def leertxt():
    archi=open('Clase10_06/Starwars.txt','r')
    linea= archi.readline()
    while linea:
        palabras = []
        palabras = linea.split()
        for i in palabras:
            if i in repetidos:
                repetidos[i] += 1
            else:
                repetidos[i] = 1
        linea = archi.readline()
    for i in repetidos:
        print('({},{})'.format(i,repetidos[i]))

    archi.close()

leertxt()