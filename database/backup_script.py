import os
import subprocess
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('HOST')
db_user = os.getenv('USER')
db_password = os.getenv('PASSWORD')
db_name = os.getenv('DATABASE_NAME')
db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"

def backup_database(backup_path):
    engine = sqlalchemy.create_engine(db_url)
    
    db_name = engine.url.database
    db_user = engine.url.username
    db_password = engine.url.password
    db_host = engine.url.host
    # Establecer un puerto predeterminado si db_port es None
    db_port = engine.url.port if engine.url.port else '3306'

    backup_command = f"mysqldump -h {db_host} -P {db_port} -u {db_user} --password={db_password} {db_name} > {backup_path}"

    # Ejecutar el comando de respaldo
    try:
        subprocess.run(backup_command, check=True, shell=True)
        # print(f"Respaldo realizado con éxito en {backup_path}")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error al realizar el respaldo: {e}")
