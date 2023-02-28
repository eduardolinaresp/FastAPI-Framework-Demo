## Tutorial

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
         


    