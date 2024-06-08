from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

# Obtener las variables de entorno
DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DB_HOST = os.getenv('HOST')
DB_NAME = os.getenv('DATABASE_NAME')

# Configurar la URL de la base de datos
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Esta es la configuración de Alembic, que proporciona
# acceso a los valores dentro del archivo .ini en uso.
config = context.config

# Interpretar el archivo de configuración para Python logging.
# Esta línea básicamente configura los loggers.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Añadir aquí el objeto MetaData de tu modelo para soporte de 'autogenerate'
# Importa tus modelos aquí
from database.models import Base  # Asegúrate de ajustar el import a tu estructura de proyecto
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Ejecuta las migraciones en modo 'offline'.

    Esto configura el contexto solo con una URL
    y no con un Engine, aunque un Engine también es aceptable
    aquí. Al omitir la creación del Engine
    ni siquiera necesitamos que un DBAPI esté disponible.

    Las llamadas a context.execute() aquí emiten la cadena dada a la
    salida del script.
    """
    url = DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Ejecuta las migraciones en modo 'online'.

    En este escenario, necesitamos crear un Engine
    y asociar una conexión con el contexto.
    """
    configuration = config.get_section(config.config_ini_section) or {}
    configuration['sqlalchemy.url'] = DATABASE_URL
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
