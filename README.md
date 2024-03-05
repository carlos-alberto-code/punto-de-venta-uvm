# Inicio

Antes de cualquier cosa, asegúrate de tener instalado Python 3.8 o superior. El proyecto comenzó con Python 3.10 (versionado al más reciente).

Crea un nuevo proyecto en el editor de tu preferencia y abre una terminal en la carpeta del proyecto. Yo llame al proyecto simplemente ``punto_de_venta``, aunque cada uno puede tener un nombre diferente.

Estando dentro del proyecto(carpeta), crea un nuevo entrono virtual. Para crear un entorno virtual, ejecuta:

``` powershell
python -m venv .venv
```

Esto creará una carpeta llamada ``.venv`` en la raíz del proyecto.

Entra al entorno virtual para instalar las dependencias necesarias. Para entrar al entorno virtual, ejecuta:

``` powershell
.venv\Scripts\Activate
```

Una vez dentro del entorno virtual, deberías ver algo como esto en la terminal:

```powershell
(.venv) C:\Users\Usuario\Documents\punto_de_venta>
```

Ahora que estás dentro del entorno virtual, vas a inicializar un repositorio en la carpeta raíz del proyecto. Para inicializar has:

```git
git init
```

Ahora ya tienes un entorno virtual y un repositorio inicializado en la carpeta raíz del proyecto. Por ahora no agregues nada, y jala el código del repositorio de GitHub. Para hacer esto, primero deberás agregar el repositorio remoto. Para agregar el repositorio remoto, ejecuta:

``` git
git remote add origin https://github.com/cabh-000/punto-de-venta-uvm.git
```

Ahora debemos jalar el código del repositorio de GitHub. Para hacer esto, ejecuta:

``` git
git pull origin master
```

Si tu rama principal es ``main`` en lugar de ``master``, sólo cambia el nombre.

Ya que tienes el código en local, confirma lo que haz traído del repositorio remoto haciendo:

``` git
git add .
git commit - m 'Inicio del proyecto. Jalón inicial'
```

Lo que está en comillas simples es un mensaje, cambialo por uno que te ayude a entender que cambios hiciste en el código.

Al extraer el código del repositorio, deberías ver un archivo importante para que puedas usar el comando ``git add .`` que te mostré anteriormente. El archivo que deberías ver es ``.gitignore``. Este archivo es importante para que no subas archivos innecesarios al repositorio. No es necesaario modificar este archivo, pero es importante que no lo borres.

Ahora, que tienes el código, necesitamos instalar las dependencias necesarias. Para instalar las dependencias necesarias, ejecuta:

``` powershell
pip install -r requirements.txt
```

En este momento deberías tener el código en local, el entorno virtual activado y las dependencias instaladas. Las dependencias instaladas son recursos que se han ocupado en el código, cosas como paquetes, librerías, etc.
