from PySide2.QtWidgets import QApplication
import sys
from mainwindow import MainWindow

# Aplicación de Qt
app = QApplication()
window = MainWindow()
window.show()
# Qt loop
sys.exit(app.exec_())