# TCP Project
Proyecto en el que se implementa un Servidor TCP y un cliente TCP

## Estructura del Proyecto
- `src/server/server.py`: Contiene el código del servidor TCP.
- `src/client/client.py`: Contiene el código del cliente TCP.

## Instrucciones de Ejecución

### Ejecutar el Servidor
1. Abre una terminal y navega a la carpeta `TCP_Server/src/server` de tu projecto:
    ```bash
   cd src/server
   
2. Ejecuta el servidor
    ```bash
    python server.py
    
### Ejecutar el Cliente
1. Abre una nueva terminal y navega a la carpeta `TCP_Server/src/client` de tu projecto:
    ```bash
   cd src/server
   
2. Ejecuta el cliente
    ```bash
    python client.py
    
## Instrucciones de Ejecución de las pruebas manuales
Deben de estar iniciados ambos servidores para realizar las pruebas

### Prueba 1: Enviar un mensaje de texto normal
1. En el cliente, ingresa un mensaje cualquiera (por ejemplo, "hola servidor").
2. Verifica que el servidor responda con el mensaje en mayúsculas (por ejemplo, "HOLA SERVIDOR").

### Prueba 2: Enviar el mensaje "DESCONEXION"
1. En el cliente, ingresa el mensaje "DESCONEXION".
2. Verifica que el cliente muestre "Cerrando conexión con el servidor..." y finalice.
3. Verifica que el servidor muestre "Desconectando al cliente..." y continúe esperando nuevas conexiones.

