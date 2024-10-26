## Proyecto eliminar fondo imágenes

### Descripción:

Programa para generar eliminar los fondos de las imágenes usando PyQt5

### Estructura de archivos

```
app/
│
├── main.py                   # Archivo principal para ejecutar la aplicación
├── constants.py              # Archivo que contiene las constantes usadas en la aplicación
└── utils/
    ├── __init__.py           # Hace que la carpeta sea un módulo de Python
    ├── config.py             # Lógica para guardar la última ruta de las imágenes
    ├── image.py              # Funciones de utilidad para la interfaz gráfica
    └── remove_bg.py          # Lógica para eliminar el fondo de las imágenes
```

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