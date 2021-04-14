#Servicios Web
import gmg
import requests
import bs4
import time
import lxml

ayuntamiento = []
n = int(input('Numero de Ayuntamientos: '))
for i in range(n):
    temp = str(input('Ayuntamiento nº{}:'.format(str(i+1))))
    ayuntamiento.append(temp)
print('')

#Iterador 4, convertirlo en una función, o en un bucle
def Locate (x):
    #Interador 1
    code = requests.get('https://irdgcdinfo.data.blog/ayuntamientos/')
    tabla = bs4.BeautifulSoup(code.content, 'html.parser')
    info = (tabla.prettify()).split('</tr>')
    info = info[1:316]
    for i in range(len(info)):
        temp = info[i]
        temp = temp.split('>')
        temp[2] = temp[2].rstrip('</th')
        temp[2] = temp[2].rstrip('              ')
        temp[2] = temp[2][14:len(temp[2])-1]
        temp[4] = temp[4].rstrip('</th')
        temp[4] = temp[4].rstrip('              ')
        temp[4] = temp[4][14:len(temp[4])-1]
        dato = [temp[2], temp[4]]
        info[i]=dato

    for i in range(len(info)):
        a = info[i]
        if a[1] == x:
            indice_info = i

    respuesta = ('Codigo Ayuntamiento: {} \tNombre Ayuntamiento: {}'.format(
        info[indice_info][0], info[indice_info][1]))

    #Interador 2
    code = requests.get('https://servizos.meteogalicia.gal/rss/predicion/jsonPredConcellos.action?idConc={}'.format(info[indice_info][0]))
    meteo = code.json()
    tiempo = meteo['predConcello']['listaPredDiaConcello']
    estado_c = tiempo[0]['ceo']['manha']

    code = requests.get('https://irdgcdinfo.data.blog/codigos/')
    tabla = bs4.BeautifulSoup(code.content, 'html.parser')
    codigo = (tabla.prettify()).split('</tr>')
    codigo = codigo[1:46]
    for i in range(len(codigo)):
        temp = codigo[i]
        temp = temp.split('>')
        temp[2] = temp[2].rstrip('</th')
        temp[2] = temp[2].rstrip('              ')
        temp[2] = temp[2][14:len(temp[2])-1]
        temp[4] = temp[4].rstrip('</th')
        temp[4] = temp[4].rstrip('              ')
        temp[4] = temp[4][14:len(temp[4])-1]
        dato = [temp[2], temp[4]]
        codigo[i]=dato

    for i in range(len(codigo)):
        a = codigo[i]
        if a[0] == str(estado_c):
            indice_codigo = i

    respuesta = (respuesta+'\nEstado del Cielo: {}'.format(codigo[indice_codigo][1]))

    #Iterador 3
    total = []
    code = requests.get('https://eu1.locationiq.com/v1/search.php?key=pk.b6a238bbe6098eb42bad4fc149b84e25&q={}&format=xml'.format(x))
    tabla = bs4.BeautifulSoup(code.content, 'lxml')
    prueba = (tabla.prettify()).split('<place')
    prueba = prueba[1:]
    for i in range(len(prueba)):
        temp = prueba[i]
        temp = temp.split(sep = ' ')
        for i in range(len(temp)):
            if temp[i].startswith('importance='):
                a = i
            elif temp[i].startswith('lat='):
                b = i
            elif temp[i].startswith('lon='):
                c = i
        recursos = [float(temp[a].split(sep = '"')[1]),
                    float(temp[b].split(sep = '"')[1]), 
                    float(temp[c].split(sep = '"')[1])]
        total.append(recursos)
    
    prioridad = []
    for i in range(len(total)):
        prioridad.append(float(total[i][0]))

    opcion = -1
    temp = 0

    for i in range(len(prioridad)):
        if temp < prioridad[i]:
            temp = prioridad[i]
            opcion = i

    coord = total[opcion][1:]

    respuesta = respuesta+'\nCoordenadas: lat = {} y lon = {}\n'.format(coord[0], coord[1])
    print(respuesta)
    
    return([estado_c, (coord[1], coord[0])])

conj = dict() 
for i in ayuntamiento:
    temp = Locate(i)
    conj[i] = temp
    time.sleep(1)

#Iterador 4
#Orden de la funcion gmg: Codigo cielo, longitud y latitud
puntos = []
for i in ayuntamiento:
    puntos.append(((conj[i][0], conj[i][1])))

gmg.plotMap(points = puntos)