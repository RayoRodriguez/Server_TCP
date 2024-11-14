import socket

def start_client():
    host = 'localhost'
    port = 5000
    obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    obj_socket.connect((host, port))
    print(f"Conectando al servidor en {host}:{port}")

    while True:
        message = input("Ingrese un mensaje para enviar al servidor: ")
        obj_socket.send(message.encode())

        if message.strip().upper() == "DESCONEXION":
            print("Cerrando conexión...")
            obj_socket.close()
            break

        if message.strip().upper() == "APAGAR SERVIDOR":
            print("Cerrando conexión...")
            response = obj_socket.recv(1024).decode()
            print(f"Respuesta del servidor: \n {response}")
            obj_socket.close()
            break

        response = obj_socket.recv(1024).decode()
        print(f"Respuesta del servidor: \n {response}")

if __name__ == "__main__":
    start_client()