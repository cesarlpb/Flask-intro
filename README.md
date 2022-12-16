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

## Configuración del Git (usuario y email)
```
sudo su - tu_usuario
git config --global user.name “Nombre”
git config --global user.email tu_email@dominio.com
git config -- list
```
- Ir a un repo > `git pull`

## Cómo levantar el servidor de desarrollo (en consola) de Flask
1. `cd app`
2. `source bin/activate` -> Fijaros que el shell ahora tiene **(app)**
3. `cd src`
4. `python3 app.py` -> El servidor levanta en un puerto 500X -> del 5000 al 5009
- `deactivate` para salir del entorno virtual

## Cómo levantar el servidor de desarrollo (en PM2) de Flask

**No instaleis de nuevo node, npm o pm2 en el servidor compartido**

1. Una vez instalados NodeJS, npm y `PM2` global (lo hace el admin), podemos ejecutar los comandos de `pm2`
2. Navegar a la carpeta donde está `archivo.py` y añadir el proceso a PM2 con:
```
pm2 start --name "nombre_de_tu_app 5001" archivo.py --interpreter python3
```
    - Indicad el puerto entre el 5001 y el 5009
    - Personalizad el nombre de la app, ej: "usuario|nombre 5007"
3. Para ver el listado de procesos: `pm2 ls` o `pm2 list`
4. Para reiniciar un proceso con id: `pm2 restart id` siendo id el número que aparece en `pm2 ls`
5. Para detener proceso: `pm2 stop id`
6. Para ver log de proceso: `pm2 log id`

### Añadir PM2 como servicio automático en reinicio como root (no ejecutar sin avisar)

1. `pm2 startup` -> añade el servicio de PM2 para empezar tras reinicio
2. `pm2 save` -> Guarda la lista de los servicios actuales
[Más info](https://stackoverflow.com/questions/34821063/pm2-startup-not-starting-up-on-ubuntu)

Más info: [Post oficial](https://pm2.io/blog/2018/09/19/Manage-Python-Processes)

**No instaleis de nuevo node, npm o pm2 en el servidor compartido**

## Comandos

- [Crear usuario](https://vivaubuntu.com/crear-usuarios-en-ubuntu/)
- [Clonar repo Flask](https://github.com/cesarlpb/Flask-intro.git)
- [Instalar code (solo root)](https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-20-04/) 
- Abrir carpeta:
    - Navegar hasta `/home/tu_usuario/carpeta_Flask` o
    - Desde Code con Abrir Carpeta -> `/home/tu_usuario/carpeta_Flask`