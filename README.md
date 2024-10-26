## Proyecto eliminar fondo imágenes

### Descripción:

Programa para generar eliminar los fondos de las imágenes usando PyQt5

### Crear entorno virtual

Para crear un entorno virtual se debe ejecutar los siguientes comandos:

```bash
python -m venv venv
.\venv\Scripts\activate
```

### Instalar dependencias

Para instalar las dependencias especificadas en `requirements.txt`, abre una terminal y navega hasta el directorio del proyecto. Luego, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

### Ejecución del programa

Para ejecutar el programa, ejecuta el siguiente comando:

```bash
python main.py
```

### Generar ejecutable

Para generar el ejecutable del programa, ejecuta el siguiente comando:

```bash
pyinstaller --onefile --windowed main.py
```