#Servicios Web
import gmg
import requests
import bs4
import lxml

ayuntamiento = 'Culleredo'

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
    if a[1] == ayuntamiento:
        indice_info = i

respuesta = ('Codigo Ayuntamiento: {}\tNombre Ayuntamiento: {}'.format(
    info[indice_info][0], info[indice_info][1]))

#Interador 2
code = requests.get('https://servizos.meteogalicia.gal/rss/predicion/jsonPredConcellos.action?idConc={}'.format(info[indice_info][0]))
meteo = code.json()
tiempo = meteo['predConcello']
lista = tiempo['listaPredDiaConcello']
estado_c = lista[0]['ceo']['manha']

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

respuesta = (respuesta+'\tEstado del Cielo: {}'.format(codigo[indice_codigo][1]))
print(respuesta)

#Iterador 3