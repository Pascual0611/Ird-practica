#Primer Iterador
#Servidor Web
#navegador/Cliente utilizado: Firefox
#Revisar el Open (Linea 47), User y Host (linea 38 y 39) no son necesarios
import sys
import socket
import threading

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
                print(c)
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
                    print(archivo)
                    print("{} /{} {}\n".format(metodo, recurso, version))
                    #Leer Archivo
                    with open (archivo, 'r') as f:
                        contenido = f.read()
                    clave = '200 Ok'
                except (FileNotFoundError):
                    clave = '404 NOT FOUND'
                except(PermissionError, IndexError, ZeroDivisionError):
                    clave = '400 BAD REQUEST'
                finally:
                    respuesta = ('{} {} \n\n'.format(version, clave))
                    x.send(respuesta.encode('UTF-8'))
                    if clave == '200 Ok':
                        x.send(contenido.encode('UTF-8'))
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