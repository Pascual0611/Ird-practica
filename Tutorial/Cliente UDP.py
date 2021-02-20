#Practicas de IRD
import socket
import sys

def main():
    if len(sys.argv) !=4:
        print("Formato ClienteUDP <maquina> <puerto> <mensaje>")
        sys.exit()
    try:
        #Instruciones sockets
        # Leemos los argumentos necesarios
        maquina = sys.argv[1]
        puerto = int(sys.argv[2])
        mensaje = sys.argv[3]
        # Creamos el socket no orientado a conexion
        socketCliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        # Establecemos un timeout de 300 segs
        timeout = 300
        socketCliente.settimeout(timeout)
        print("CLIENTE: Enviando {} a {}:{}".format(mensaje,maquina,puerto))
        # Enviamos el mensaje a la maquina y puerto indicados
        socketCliente.sendto(mensaje.encode('UTF-8'),(maquina, puerto))
        # Recibimos el mensaje de respuesta
        mensajeEco, a = socketCliente.recvfrom(len(mensaje))
        print(len(mensaje),','+str(mensajeEco)+','+str(a))
        print("CLIENTE: Recibido {} de {}:{}".format(mensajeEco.decode('UTF-8'),a[0],a[1]))
    except socket.timeout:
        #Captura excepcion si el tiempo de espera  se agota.
        print("{} segundos sin recibir nada.".format(timeout))
    except:
        # Captura excepcion generica.
        print("Error: {}".format(sys.exc_info()[0]))
        raise
    finally:
        # En cualquier caso cierra el socket.
        socketCliente.close()

if __name__ == "__main__":
    main()