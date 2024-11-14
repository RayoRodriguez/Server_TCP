import socket


def start_server():
    host = 'localhost'
    port = 5000
    obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    obj_socket.bind((host, port))
    obj_socket.listen(5)
    print(f"Servidor escuchando en {host}:{port}")

    while True:
        conn , addr = obj_socket.accept()
        print(f"Conexión establecida desde {addr}")

        while True:
            message = conn.recv(1024).decode()
            if not message:
                break

            print(f"Mensaje recibido: \n {message}")

            if message.strip().upper() == "DESCONEXION":
                print("Cliente desconectado")
                conn.close()
                break

            elif message.strip().upper() == "APAGAR SERVIDOR":
                print("Apagando el servidor...")
                response = "SERVIDOR APAGADO"
                conn.send(response.encode())
                conn.close()
                obj_socket.close()
                return
            
            else:
                response = message.strip().upper()
                conn.send(response.encode())
                print(f"Respuesta enviada: \n {response}")

if __name__ == '__main__':
    start_server()