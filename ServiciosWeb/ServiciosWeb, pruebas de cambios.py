#Servicios Web
import gmg
import requests
import bs4
import time
import lxml

ayuntamiento = []
n = int(input('Numero de Ayuntamientos: '))
for i in range(n):
    temp = str(input('Ayuntamiento nº{}: '.format(str(i+1))))
    ayuntamiento.append(temp)
print('')

#Iterador 4, convertirlo en una función, o en un bucle
def Locate (x):
    #Interador 1
    code = requests.get('https://irdgcdinfo.data.blog/ayuntamientos/')
    tabla = bs4.BeautifulSoup(code.content, 'html.parser')
    tabla = tabla.find_all('table')
    info = str(tabla).split('<tr><th>')
    info = info[1:316]
    for i in range(len(info)):
        temp = info[i]
        temp = temp.split('>')
        if temp[2][:len(temp[2])-4] == x:
            codigo_ayu = temp[0][:len(temp[0])-4]

    respuesta = ('Codigo Ayuntamiento: {} \tNombre Ayuntamiento: {}'.format(
        codigo_ayu, x))

    #Interador 2
    code = requests.get('https://servizos.meteogalicia.gal/rss/predicion/jsonPredConcellos.action?idConc={}'.format(codigo_ayu))
    meteo = code.json()
    tiempo = meteo['predConcello']['listaPredDiaConcello']
    codigo_cielo = tiempo[0]['ceo']['manha']
    
    code = requests.get('https://irdgcdinfo.data.blog/codigos/')
    tabla = bs4.BeautifulSoup(code.content, 'html.parser')
    tabla = str(tabla.table)
    tabla = tabla.split('<tr><th>')
    tabla = tabla[1:len(tabla)-1]
    info = tabla[1:len(tabla)-1]
    for i in range(len(info)):
        temp = info[i]
        temp = temp.split('>')
        if int(temp[0][:len(temp[0])-4]) == codigo_cielo:
            estado_cielo = temp[2][:len(temp[2])-4]

    respuesta = (respuesta+'\nEstado del Cielo: {}'.format(estado_cielo))

    #Iterador 3
    code = requests.get('https://eu1.locationiq.com/v1/search.php?key=pk.b6a238bbe6098eb42bad4fc149b84e25&q={}&format=xml'.format(x))
    tabla = bs4.BeautifulSoup(code.content, 'lxml')
    tabla = list(tabla.find_all('place'))
    for i in range(len(tabla)):
        temp = str(tabla[i])
        tabla[i] = temp
    imp = []
    lat = []
    lon = []
    for i in range(len(tabla)):
        dato = tabla[i].split(' ')
        for j in dato:
            if j.startswith('impo'):
                temp = j.split("\"")
                imp.append(temp[1])
            elif j.startswith('lat'):
                temp = j.split("\"")
                lat.append(temp[1])
            elif j.startswith('lon'):
                temp = j.split("\"")
                lon.append(temp[1])

    ind = imp.index(max(imp))

    respuesta = respuesta+'\nCoordenadas: lat = {} y lon = {}\n'.format(lat[ind], lon[ind])
    print(respuesta)
    
    return([codigo_cielo, (lon[ind], lat[ind])])

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

print(puntos)

gmg.plotMap(puntos)