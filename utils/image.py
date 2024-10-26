from PyQt5.QtGui import QPixmap

def show_image(label, image_path):
  # Función genérica para mostrar imagen en un QLabel
  pixmap = QPixmap(image_path)
  label.setPixmap(pixmap)
