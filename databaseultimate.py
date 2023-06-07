import psycopg2

class femafe:
    def __init__(self, host, port, database, user, password):
        self.conn = psycopg2.connect(
            host="192.168.0.3",
            port="5432",
            database="postgres",
            user="postgres",
            password="1234")

        self.cursor = self.conn.cursor()

    def ejecutar_query(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error ejecutando la consulta:", error)
            
    def consultar_datos(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error consultando datos:", error)

    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")


clase_bd = femafe(host='192.168.0.3', port='5432', database='postgres', user='postgres', password='1234')

# Ejecutar una consulta de modificación (INSERT, UPDATE, DELETE)
#clase_bd.ejecutar_query("INSERT INTO actor (first_name, last_name) VALUES ('Matias', 'Armijo')")

# Ejecutar una consulta de selección (SELECT)
resultado = clase_bd.consultar_datos("SELECT actor_id,first_name,last_name FROM actor")

clase_bd.ejecutar_query("DELETE FROM actor WHERE actor_id > 201")

resultado2 = clase_bd.consultar_datos("SELECT actor_id FROM actor")

for fila in resultado:
    print(fila)
    
for fila3 in resultado2:
    print(fila3)
    
resultado3 = clase_bd.consultar_datos("SELECT actor.first_name,actor.last_name FROM actor JOIN film_actor ON actor.actor_id = film_actor.actor_id JOIN film ON film_actor.film_id = film.film_id WHERE film.title = 'Dumbo Lust'")

for fila2 in resultado3:
    print(fila2)
    
# Cerrar la conexión
clase_bd.cerrar_conexion()