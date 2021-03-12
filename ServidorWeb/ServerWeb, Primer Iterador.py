#Servidor Web
#navegador/Cliente utilizado: Firefox
#Revisar el Open (Linea 47), User y Host (linea 38 y 39) no son necesarios
import sys
import socket
import threading
import datetime
from datetime import datetime
import os

def main():
    if len(sys.argv) !=2:
        print("Formato ServidorUDP <puerto>")
        sys.exit()
    try:
        # Leemos los argumentos necesarios
        puerto = int(sys.argv[1])
        # Creamos el socket no orientado a conexon
        socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # Asociamos el socket a cualquier direccon local
        socketServidor.bind(('', puerto))
         # Establecemos un timeout de 300 segs
        timeout = 300
        socketServidor.settimeout(timeout)
        print("Iniciando servidor en PUERTO: ",puerto)    
        #Modo Listen
        socketServidor.listen()
        while True:
            def multiples(x, b):
                # Recibimos el mensaje
                mensaje, direccion = x.recvfrom(4096) #Len de Cliente
                
                a = mensaje.decode('UTF-8')
                b = a.split(sep = '\n') #Ahora mi mensaje es una lista
                c = b[0].split(' ')
                version = 'HTTP/1.1'
                try:
                    metodo = c[0]
                    recurso = c[1]
                    version = c[2]
                    if recurso[0] == '/':
                        recurso = recurso[1:]
                    else:
                        pass
                    if metodo not in ['GET', 'HEAD']:
                        8/0
                    else:
                        pass
                    archivo = ('data/'+recurso)
                    print("{} /{} {}\n".format(metodo, recurso, version))
                    #Leer Archivo
                    if archivo.endswith('.txt'):
                        clase = 'text/plain'
                        with open (archivo, 'r') as f:
                            contenido = f.read()
                    elif archivo.endswith('.html'):
                        clase = 'text/html'
                        with open (archivo, 'r') as f:
                            contenido = f.read()
                    elif archivo.endswith('.jpg'):
                        clase = 'image/jpeg'
                        with open (archivo, 'rb') as f:
                            contenido = f.read()
                    elif archivo.endswith('.gif'):
                        clase = 'image/gif'
                        with open (archivo, 'rb') as f:
                            contenido = f.read()
                    else:
                        clase = 'application/octet-stream'
                    tamano = str(os.path.getsize(archivo))
                    mod = datetime.fromtimestamp(
                        os.path.getmtime(archivo)).strftime("%a, %d %b %Y %H:%M:%S %Z")
                    clave = '200 Ok'
                except (FileNotFoundError):
                    clave = '404 NOT FOUND'
                except(PermissionError, IndexError, ZeroDivisionError):
                    clave = '400 BAD REQUEST'
                finally:
                    fecha = datetime.now()
                    respuesta = ('{} {} \n'.format(version, clave))
                    x.send(respuesta.encode('UTF-8'))
                    if clave == '200 Ok':
                        cabecera = ('Date {}\nServer localhost:5000\n').format(fecha)
                        cabecera = cabecera + ('Content-Length {}\n').format(tamano)
                        cabecera = cabecera + ('Content-Type {}\n').format(clase)
                        cabecera = cabecera + ('Last-Modified {}\n\n').format(mod)
                        x.send(cabecera.encode('UTF-8'))
                        if metodo in ['GET']:
                            try:
                                if clase in ['text/plain', 'text/html']:
                                    x.send(contenido.encode('UTF-8'))
                                elif clase in ['image/jpeg', 'image/gif']:
                                    x.send(contenido)
                            except UnboundLocalError:
                                pass
                        else:
                            pass
                    else:
                        pass
                x.close()
            sc, d = socketServidor.accept()
            threading.Thread(target=multiples,args=(sc, d)).start() #Da problemas el threading
    except socket.timeout:
        print("{} segundos sin recibir nada.".format(timeout))
    except:
        print(1)
        print("Error: {}".format(sys.exc_info()[0]))
        raise
    finally:
        socketServidor.close()

if __name__ == "__main__":
    main()