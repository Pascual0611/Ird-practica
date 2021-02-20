#Eje3. Multihilo
#En algunos casos, al reiniciar la consola el programa da error, vovler a ejecutar y se soluciona
#Opciones de comando: 5000
#Problema, en el print del la linea 31 se dan los datos de forma anomala, se soluciona con d[0] y d[1]
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
                mensaje, direccion = x.recvfrom(4096) #Len de Cliente?
                a1 = direccion[0]
                a2 = direccion[1]
                print("Recibido mensaje: {} de: {}:{}".format(mensaje.decode('UTF-8'), a1, a2))
                # Enviamos el mensaje
                x.send(mensaje)
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