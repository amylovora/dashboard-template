from os import getenv
import pymssql
import pandas as pd

server   = '172.16.101.70'
user     = 'vreyes'
password = 'Tq3L31QN3&4'



lista=[]
# ve el ingreso a la base de datos con mi ususario y contraseña y BI creo que le dice donde debe
# buscar en la base de datos
with pymssql.connect(server, user, password, "SINCWEBSO") as db:
     # el cursor es el que va apuntar a lo que yo busco
    cursor = db.cursor(as_dict = True)
     # aca pongo la consulta como un str
    query = """SELECT * FROM reportes.dinamicaVentas"""
    cursor.execute(query)
    row = cursor.fetchone()
    while row:
        lista.append(row)
        row = cursor.fetchone()
    
    df = pd.DataFrame(lista)
    print(df.head(3))


