#Ejercicio 1: Cliente TCP
#Opciones de comando: 127.0.0.1 5000 "Funciona" o localhost 5000 "Funciona"
#En moba no funciona con localhost, solo con 127.0.0.1
#Problema: la dirección del servidor en el reducido no aparece de forma normal, con puerto y maquina se expresaria bien
import sys
import socket

def main():
    if len(sys.argv)!=4:
        print('Formato Cliente TCP <maquina> <puerto> <mensaje>')
        sys.exit()
    try:
        #Leemos los datos necesitados
        maquina = sys.argv[1]
        puerto = int(sys.argv[2])
        mensaje = sys.argv[3]
        #Creamos el Socket
        socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Establecer el time out del cliente
        timeout = 300
        socketCliente.settimeout(timeout)
        print("CLIENTE: Enviando {} a {}:{}".format(mensaje,maquina,puerto))
        #Crear conexión
        socketCliente.connect((maquina, puerto))
        #Envio
        socketCliente.send(mensaje.encode('UTF-8'))
        #Recibir
        mensajeEco, a = socketCliente.recvfrom(len(mensaje))
        print("CLIENTE: Recibido {} de {}:{}".format(mensajeEco.decode('UTF-8'), a[0],a[1]))
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