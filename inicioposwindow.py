from PySide2.QtWidgets import QDialog, QFileDialog, QTableWidgetItem, QMessageBox, QHeaderView, QGraphicsScene, QGraphicsView
from ui_inicioposwindow import Ui_inicioPos
from PySide2.QtCore import Slot
class InicioWindow(QDialog):
	def __init__(self, Parent):
		super(InicioWindow, self).__init__()
		self.x = 0
		self.y = 0
		self.ui = Ui_inicioPos()
		self.ui.setupUi(self)
		self.ui.btnAceptar.clicked.connect(self.aceptar)
		self.ui.btnCancelar.clicked.connect(self.cancelar)
	@Slot()
	def aceptar(self):
		self.x = self.ui.txtX.text()
		self.y = self.ui.txtY.text()
		self.accept()
	@Slot()
	def cancelar(self):
		self.reject()
