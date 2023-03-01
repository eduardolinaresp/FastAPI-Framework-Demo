## Tutorial


https://www.youtube.com/watch?v=6eVj33l5e9M&t=18s

### Definir SQLALCHEMY

    1-Ejecutar MYSQL crear base de datos storedb
    2-En archivo config/db.py agregar conexion

            from sqlalchemy import create_engine, MetaData
            engine = create_engine("mysql+pymysql://fastapi:fastapi@localhost:3306/storedb")
            metadata = MetaData
            conn = engine.connect()

### generar modelos 

     1- En carpeta models crear archivo user.py
     2- importar 
         from sqlalchemy import Table, Column
         from config.db import meta
     3- Mapping objetos
         user = Table("users", meta)
         

### Fromatear codigo

    ctrl + p  > format document
    VSCODE solicitará permisos para instalar autopep8 indicamos que si.
    repetir ctrl + p  > format document para dar formato 
    conclusion el formateador es malo
    