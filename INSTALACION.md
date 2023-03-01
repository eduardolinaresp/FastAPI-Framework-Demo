# Instalación 

## 1 Preparar entorno virtual

    python -m venv .venv 
    .venv\scripts\activate

### seleccionar interprete en vscode

    ctrl + p  + >  python interpreter

## 2 Instalar paquetes 

    pip install uvicorn
    pip install fastapi
    pip install sqlalchemy
    pip install pymysql

## Establecer en archivo de proyecto librerias utilizadas.

    pip freeze > requeriment.txt   

    pip install -r requeriment.txt 


