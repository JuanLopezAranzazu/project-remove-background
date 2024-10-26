import sys
from PyQt5.QtWidgets import (
  QApplication,
  QMainWindow,
  QPushButton,
  QLabel,
  QFileDialog,
  QGridLayout,
  QWidget,
)
from PyQt5.QtCore import Qt
from PIL import Image
from utils.remove_bg import remove_background
from utils.image import show_image
from constants import LABEL_WIDTH, LABEL_HEIGHT

class App(QMainWindow):
  def __init__(self):
    super().__init__()

    # Variables
    self.input_image_path = None

    self.create_widgets()
      
  def create_widgets(self):
    self.setWindowTitle("Proyecto eliminar fondo imagen")
    self.setGeometry(100, 100, 1000, 500)
    
    # Crear el layout de la cuadrícula
    grid_layout = QGridLayout()
    
    # Botón para seleccionar imagen
    self.btn_select = QPushButton("Seleccionar Imagen", self)
    self.btn_select.clicked.connect(self.select_image)
    
    # Botón para quitar el fondo
    self.btn_remove = QPushButton("Quitar Fondo", self)
    self.btn_remove.clicked.connect(self.on_remove_background)
    self.btn_remove.setEnabled(False)  # Desactivado hasta que se seleccione una imagen

    # Agregar botones a la cuadrícula
    grid_layout.addWidget(self.btn_select, 0, 0)  # Fila 0, Columna 0
    grid_layout.addWidget(self.btn_remove, 0, 1)  # Fila 0, Columna 1

    # Etiqueta para mostrar imagen original
    self.original_image_label = QLabel(self)
    self.original_image_label.setText("Imagen Original")
    self.original_image_label.setAlignment(Qt.AlignCenter)
    self.original_image_label.setFixedSize(LABEL_WIDTH, LABEL_HEIGHT)  # Establecer dimensiones específicas
    self.original_image_label.setStyleSheet("border: 2px solid black;")  # Añadir contorno negro
    self.original_image_label.setScaledContents(True)  # Adaptar la imagen al tamaño del label

    # Etiqueta para mostrar imagen sin fondo
    self.processed_image_label = QLabel(self)
    self.processed_image_label.setText("Imagen Procesada")
    self.processed_image_label.setAlignment(Qt.AlignCenter)
    self.processed_image_label.setFixedSize(LABEL_WIDTH, LABEL_HEIGHT)  # Establecer dimensiones específicas
    self.processed_image_label.setStyleSheet("border: 2px solid black;")  # Añadir contorno negro
    self.processed_image_label.setScaledContents(True)  # Adaptar la imagen al tamaño del label
 
    # Agregar etiquetas de imagen a la cuadrícula
    grid_layout.addWidget(self.original_image_label, 1, 0)  # Fila 1, Columna 0
    grid_layout.addWidget(self.processed_image_label, 1, 1)  # Fila 1, Columna 1
    
    # Configurar layout en un widget
    container = QWidget()
    container.setLayout(grid_layout)
    self.setCentralWidget(container)

  def select_image(self):
    # Abrir diálogo para seleccionar imagen
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar Imagen", "", "Images (*.png *.jpg *.jpeg)")
    
    if file_path:
      self.input_image_path = file_path
      self.btn_remove.setEnabled(True)
      show_image(self.original_image_label, file_path)
    
  def on_remove_background(self):
    if self.input_image_path:
      # Abrir diálogo para seleccionar la carpeta de destino y el nombre del archivo
      save_path, _ = QFileDialog.getSaveFileName(self, "Guardar Imagen Procesada", "", "PNG Files (*.png)")
      
      if save_path:
        # Asegurarse de que el archivo tenga la extensión .png
        if not save_path.lower().endswith('.png'):
            save_path += '.png'
        
        # Llamar a la función que quita el fondo
        remove_background(self.input_image_path, save_path)
        
        # Mostrar la imagen procesada en la interfaz
        show_image(self.processed_image_label, save_path)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = App()
  window.show()
  sys.exit(app.exec_())
