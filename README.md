# Flask-intro
Proyecto de Flask para aprender a usar el framework
## Cómo conectar

1. Instalad la extensión de Code: `Remote-SSH` -> `ms-vscode-remote.remote-ssh`
2. Clic en botón verde abajo a la izq -> Conectar a Host -> Configurar nuevo host (`.../config`):
```
    Host Formacion-POO
        HostName 80.240.127.173
        User root
```
3. Guardad y salir de config.
4. Clic en icono y Conectar -> Elegimos host
5. Aceptar, elegid Linux si pregunta y contraseña para conectar

## Cómo levantar el servidor de desarrollo de Flask
1. `cd app`
2. `source bin/activate` -> Fijaros que el shell ahora tiene **(app)**
3. `cd src`
4. `python3 app.py` -> El servidor levanta en un puerto 500X -> del 5000 al 5009
- `deactivate` para salir del entorno virtual

## Comandos

- [Crear usuario](https://vivaubuntu.com/crear-usuarios-en-ubuntu/)
- [Clonar repo Flask](https://github.com/cesarlpb/Flask-intro.git)
- [Instalar code (solo root)](https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-20-04/) 
- Abrir carpeta:
    - Navegar hasta `/home/tu_usuario/carpeta_Flask` o
    - Desde Code con Abrir Carpeta -> `/home/tu_usuario/carpeta_Flask`