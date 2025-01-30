Antes de lanzar los contenedores hay que crear directorio mariadb_data
Después, ejecutaremos el comando; sudo docker compose -f docker-composePython.yml up
Una vez lanzada cargar el archivo Gimnasio.sql en maridadb para que 
la base de datos y la tabla de productos exista: 
   HAY QUE ACCEDER A http://localhost:9093

si se desea arrancar los contenedores de BBDD sólo y lanzar la aplicación python a mano:
  Lanzar docker-compose.yaml  
  Ejecuta: cd web
  Ejecuta: virtualenv env
  Ejecuta: source env/bin/activate en linux o env\Scripts\activate.bat en Windows
  Ejecuta: pip install -r requirements.txt   (instala los paquetes necesarios)
  Ejecuta: python app.py
  Probar la aplicación con: localhost:7777/
