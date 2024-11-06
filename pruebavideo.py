import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QMovie

class GifPlayer(QMainWindow):
    def __init__(self):
        super(GifPlayer, self).__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Reproductor de GIF")
        self.setGeometry(100, 100, 800, 600)

        # Crear un QLabel para mostrar el GIF
        self.gif_label = QLabel(self)
        self.gif_label.setScaledContents(True)  # Ajustar el tamaño si es necesario

        # Cargar el GIF
        gif_path = "loading.gif"  # Cambia esta ruta a tu archivo GIF
        movie = QMovie(gif_path)
        self.gif_label.setMovie(movie)
        movie.start()  # Comienza la reproducción del GIF

        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.gif_label)

        # Crear un contenedor y establecer el layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = GifPlayer()
    player.show()
    sys.exit(app.exec_())