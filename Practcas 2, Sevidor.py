#
import sys
import socket

def main():
    if len(sys.argv) != 2:
        print("Formato ServidorUDP <puerto>")
        sys.exit()
    try:
        # Instrucciones sockets
        pass
    except socket.timeout:
        print("{} segundos sin recibir nada.".format(timeout))
    except:
        print("Error: {}".format(sys.exc_info()[0]))
        raise
    finally:
        socketServidor.close()

# Leemos los argumentos necesarios
puerto = int(sys.argv[1])
# Creamos el socket no orientado a conexion
socketServidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Asociamos el socket a cualquier direccion local
# en el puerto indicado
socketServidor.bind(("", puerto))
# Establecemos un timeout de 300 segs
timeout = 300
socketServidor.settimeout(timeout)

print("Iniciando servidor en PUERTO: ",puerto)

# Recibimos el mensaje
mensaje, direccion = socketServidor.recvfrom(4096)
print("Recibido mensaje: {} de: {}:{}".format(
mensaje.decode('UTF-8'),direccion[0],direccion[1]))
# Enviamos el mensaje
socketServidor.sendto(mensaje, direccion)

if __name__ == "__main__":
    main()