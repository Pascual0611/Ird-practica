#Servicios Web
import gmg
import requests
import bs4
import lxml

ayuntamiento = 'Culleredo'

#Interador 1
code = requests.get('https://irdgcdinfo.data.blog/ayuntamientos/')
tabla = bs4.BeautifulSoup(code.content, 'html.parser')
prueba = (tabla.prettify()).split('</tr>')
prueba = prueba[1:316]
for i in range(len(prueba)):
    temp = prueba[i]
    temp = temp.split('>')
    temp[2] = temp[2].rstrip('</th')
    temp[2] = temp[2].rstrip('              ')
    temp[2] = temp[2][14:len(temp[2])-1]
    temp[4] = temp[4].rstrip('</th')
    temp[4] = temp[4].rstrip('              ')
    temp[4] = temp[4][14:len(temp[4])-1]
    dato = [temp[2], temp[4]]
    prueba[i]=dato

for i in range(len(prueba)):
    a = prueba[i]
    if a[1] == ayuntamiento:
        indice = i

print('Codigo Ayuntamiento: {}\tNombre Ayuntamiento: {}'.format(
    prueba[indice][0], prueba[indice][1]))

#Interador 2
