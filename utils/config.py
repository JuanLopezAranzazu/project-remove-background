import os
import json

# Archivo de configuración para guardar la última ruta
CONFIG_FILE = "config.json"
DEFAULT_IMAGE_PATH = os.path.expanduser("~")

# Función para guardar la última ruta en un archivo JSON
def save_last_path(path):
  with open(CONFIG_FILE, 'w') as config_file:
    json.dump({"last_path": path}, config_file)

# Función para cargar la última ruta desde un archivo JSON
def load_last_path():
  if os.path.exists(CONFIG_FILE):
    
    with open(CONFIG_FILE, 'r') as config_file:
      
      config = json.load(config_file)
      
      return config.get("last_path", DEFAULT_IMAGE_PATH)
  
  return DEFAULT_IMAGE_PATH
