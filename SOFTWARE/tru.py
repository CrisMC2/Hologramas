from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QListWidget, QListWidgetItem

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit(self)
        self.listWidget = QListWidget(self)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.listWidget)
        
        self.listWidget.itemClicked.connect(self.onItemClicked)
        self.listWidget.hide()

        self.textEdit.mousePressEvent = self.showListWidget

    def showListWidget(self, event):
        print("showListWidget ejecutado")
        self.listWidget.show()
        self.listWidget.clear()
        elementos = ["Elemento 1", "Elemento 2", "Elemento 3"]
        for elemento in elementos:
            self.listWidget.addItem(elemento)

    def onItemClicked(self, item):
        print("Texto seleccionado:", item.text())
        self.textEdit.setText(item.text())
        self.listWidget.hide()

app = QApplication([])
ventana = MiVentana()
ventana.show()
app.exec_()
