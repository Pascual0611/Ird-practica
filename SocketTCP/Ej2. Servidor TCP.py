##' Ejercicio 2: Servidor TCP
#Opciones de comando: 5000
#En moba funciona con localhost y con 127.0.0.1
#Con d[0] y d[1] se expresa correctamente el print de la linea 31
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
            sc, d = socketServidor.accept()
            # Recibimos el mensaje
            mensaje, direccion = sc.recvfrom(4096)
            a1=direccion[0]
            a2=direccion[1]            
            print("Recibido mensaje: {} de: {}:{}".format(mensaje.decode('UTF-8'), a1, a2))
            # Enviamos el mensaje
            sc.send(mensaje)
            sc.close()
    except socket.timeout:
        print("{} segundos sin recibir nada.".format(timeout))
    except:
        print("Error: {}".format(sys.exc_info()[0]))
        raise
    finally:
        socketServidor.close()

if __name__ == "__main__":
    main()