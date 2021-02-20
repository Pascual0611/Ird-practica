#Ejercicio 2: Servidor TCP
import sys
import socket

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
            Cliente = socketServidor.accept() 
            # Recibimos el mensaje
            mensaje, direccion = socketServidor.recv() #Len de Cliente?
            print("Recibido mensaje: {} de: {}:{}".format(direccion[0],direccion[1]))
            # Enviamos el mensaje
            socketServidor.send(mensaje, direccion)
    except socket.timeout:
        print("{} segundos sin recibir nada.".format(timeout))
    except:
        print("Error: {}".format(sys.exc_info()[0]))
        raise
    finally:
        socketServidor.close()

if __name__ == "__main__":
    main()
