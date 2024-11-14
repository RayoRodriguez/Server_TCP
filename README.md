# TCP Project
Proyecto en el que se implementa un Servidor TCP y un cliente TCP.

[![Static Badge](https://img.shields.io/badge/python-v3.13-blue)](https://www.python.org/downloads/)

## Estructura del Proyecto
- `src/server/server.py`: Contiene el código del servidor TCP.
- `src/client/client.py`: Contiene el código del cliente TCP.

## Instrucciones de Ejecución

### Ejecutar el Servidor
1. Abre una terminal y navega a la carpeta `src/server` de tu projecto:
    ```bash
   cd src/server
   
2. Ejecuta el servidor
    ```bash
    python server.py
    
### Ejecutar el Cliente
1. Abre una nueva terminal y navega a la carpeta `src/server` de tu projecto:
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
2. Verifica que el cliente muestre "Cerrando conexión..." y finalice.
3. Verifica que el servidor muestre "Cliente desconectado" y continúe esperando nuevas conexiones.

### Prueba 3: Enviar el mensaje "APAGAR SERVIDOR"
1. En el cliente, ingresa el mensaje "APAGAR SERVIDOR".
2. Verifica que el cliente muestre "Cerrando conexión ...", Reciba una respuesta del servidor que muestre "SERVIDOR APAGADO" y finalice.
3. Verifica que el servidor muestre "Apagando el servidor..." y finalice.