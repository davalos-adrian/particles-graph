from PySide2.QtWidgets import QMainWindow, QDialog, QFileDialog, QTableWidgetItem, QMessageBox, QHeaderView, QGraphicsScene, QGraphicsView, QWidget
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QColor, QBrush, QTransform, QPen, QPainter
from pprint import pformat
from random import randint
from inicioposwindow import InicioWindow
from queue import PriorityQueue
import json
import math
from particula import Particula
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.particulas = []
		self.puntos = []
		self.grafo = dict()
		self.scene = QGraphicsScene()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.btnAgregar.clicked.connect(self.agregar)
		self.ui.btnMostrar.clicked.connect(self.mostrar)
		self.ui.actionAbrir.triggered.connect(self.abrir)
		self.ui.actionGuardar.triggered.connect(self.guardar)
		self.ui.actionFuerzaBruta.triggered.connect(self.puntosCercanos)
		self.ui.actionVerPuntos.triggered.connect(self.dibujarPuntos)
		self.ui.actionSalir.triggered.connect(self.salir)
		self.ui.actionGrafo.triggered.connect(self.hacerGrafo)
		self.ui.actionBFSDFS.triggered.connect(self.BFSDFS)
		self.ui.btnMostrarTabla.clicked.connect(self.mostrarTabla)
		self.ui.btnBuscar.clicked.connect(self.buscar)
		self.ui.btnDibujar.clicked.connect(self.dibujar)
		self.ui.btnLimpiar.clicked.connect(self.limpiar)
		self.ui.graphicsView.setScene(self.scene)
		self.ui.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
		self.ui.btnOrdenar.clicked.connect(self.ordenar)
		self.ui.actionPrim.triggered.connect(self.prim)
	@Slot()
	def agregar(self):
		particula = Particula(
			self.ui.txtId.text(),
			self.ui.txtOrigen.text().split(','),
			self.ui.txtDestino.text().split(','),
			self.ui.txtVelocidad.text(),
			self.ui.txtColor.text().split(','),
		)
		self.ui.txtDistancia.setText(str(particula.distancia))
		self.particulas.append(particula)

	@Slot()
	def mostrar(self):
		self.ui.txtAreaParticula.document().setPlainText("")
		for x in self.particulas:
			self.ui.txtAreaParticula.insertPlainText(x.toString() + '\n' + '\n')
	
	@Slot()
	def salir(self):
		self.close()

	@Slot()
	def abrir(self):
		self.particulas = []
		ubicacion = QFileDialog().getOpenFileName(self,
										 "Abrir particulas"
										 , "."
										 ,"JSON Files (*.json)")
		with open(ubicacion[0], 'r') as archivo:
			reading = json.load(archivo)
		for particle in reading:
			particula = Particula(particle['id'],
									[particle['origen']['x'],particle['origen']['y']],
									[particle['destino']['x'], particle['destino']['y']],
								 	particle['velocidad'],
								  	[particle['color']['red'],
										particle['color']['green'],
										particle['color']['blue']
									])
			self.particulas.append(particula)

	@Slot()
	def guardar(self):
		save = []
		ubicacion = QFileDialog().getSaveFileName(self,
										 "Guardar particulas"
										 , "."
										 ,"JSON Files (*.json)")
		with open(ubicacion[0], 'w') as archivo:
			for particle in self.particulas:
				save.append({
					'id' : particle.id,
					'origen' : {
						'x' : particle.origen.x,
						'y' : particle.origen.y
					},
					'destino' : {
						'x' : particle.destino.x,
						'y' : particle.destino.y
					},
					'velocidad' : particle.velocidad,
					'color' : {
						'red' : particle.color.r,
						'green' : particle.color.g,
						'blue' : particle.color.b
					}
				})
			json.dump(save, archivo, indent = 4)

	@Slot()
	def mostrarTabla(self):
		self.particulasTabla(self.particulas)

	@Slot()
	def buscar(self):
		particulas = []
		id = self.ui.txtBuscar.text()
		for particula in self.particulas:
			if id == str(particula.id):
				particulas.append(particula)

		if len(particulas) == 0:
			QMessageBox.information(self, "Particulas", "No se encontraron particulas")
		else:
			self.particulasTabla(particulas)

	@Slot()
	def hacerGrafo(self):
		self.grafo = {}
		self.dibujar()
		for particula in self.particulas:
			origen = (particula.origen.x, particula.origen.y)
			destino = (particula.destino.x, particula.destino.y)
			if origen in self.grafo:
				self.grafo[origen].append((destino, particula.distancia))
			else:
				self.grafo[origen] = [(destino, particula.distancia)]
			if destino in self.grafo:
				self.grafo[destino].append((origen, particula.distancia))
			else:
				self.grafo[destino] = [(origen, particula.distancia)]
		str = pformat(self.grafo, width=40, indent=1)
		self.ui.txtAreaParticula.document().setPlainText("")
		self.ui.txtAreaParticula.insertPlainText(str)

	@Slot()
	def dibujar(self):
		pen = QPen()
		pen.setWidth(3)
		for particula in self.particulas:
			color = QColor(particula.color.r, particula.color.g, particula.color.b)
			pen.setColor(color)
			self.scene.addLine(particula.origen.x + 3, particula.origen.y + 3, particula.destino.x + 3, particula.destino.y + 3, pen)
		self.dibujarPuntos()

	def obtenerPuntos(self):
		self.puntos = []
		for particula in self.particulas:
			self.puntos.append({"x":particula.origen.x, "y":particula.origen.y, "color": particula.color})
			self.puntos.append({"x":particula.destino.x, "y":particula.destino.y, "color": particula.color})

	@Slot()
	def dibujarPuntos(self):
		pen = QPen()
		brush = QBrush()
		pen.setWidth(3)
		self.obtenerPuntos()
		for particula in self.particulas:
			color = QColor(particula.color.r, particula.color.g, particula.color.b)
			pen.setColor(color)
			brush.setColor(color)
			brush.setStyle(Qt.SolidPattern)
			self.scene.addEllipse(particula.origen.x, particula.origen.y, 6, 6, pen, brush)
			self.scene.addEllipse(particula.destino.x, particula.destino.y, 6, 6, pen, brush)

	@Slot()
	def limpiar(self):
		self.scene.clear()
		self.ui.graphicsView.setTransform(QTransform())

	def particulasTabla(self, particulas):
		labels = ['Id', 'origen', 'destino', 'velocidad', 'color', 'distancia']
		self.ui.tblParticulas.clear()
		self.ui.tblParticulas.setColumnCount(6)
		self.ui.tblParticulas.setRowCount(len(particulas))
		self.ui.tblParticulas.setHorizontalHeaderLabels(labels)
		row = 0
		for particula in particulas:
			idx = QTableWidgetItem(str(particula.id))
			origen = QTableWidgetItem('(' + str(particula.origen.x) + ',' + str(particula.origen.y) + ')')
			destino = QTableWidgetItem('(' + str(particula.destino.x) + ',' + str(particula.destino.y) + ')')
			velocidad = QTableWidgetItem(str(particula.velocidad))
			color = QTableWidgetItem("")
			color.setBackground(QBrush(QColor.fromRgb(particula.color.r,particula.color.g,particula.color.b)))
			distancia = QTableWidgetItem(str(particula.distancia))
			self.ui.tblParticulas.setItem(row, 0, idx)
			self.ui.tblParticulas.setItem(row, 1, origen)
			self.ui.tblParticulas.setItem(row, 2, destino)
			self.ui.tblParticulas.setItem(row, 3, velocidad)
			self.ui.tblParticulas.setItem(row, 4, color)
			self.ui.tblParticulas.setItem(row, 5, distancia)
			row += 1
		self.ui.tblParticulas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

	def wheelEvent(self, event):
		print(event.delta())
		if event.delta() > 0:
			self.ui.graphicsView.scale(1.2,1.2)
		else:
			self.ui.graphicsView.scale(0.8, 0.8)

	@Slot()
	def ordenar(self):
		#distancia : descendente
		#velocidad : ascendente
		self.limpiar()
		pen = QPen()
		pen.setWidth(1)
		if self.ui.comboOrdenar.currentText() == "Velocidad":
			self.particulas.sort()
			d = 0
			for particula in self.particulas:
				color = QColor(particula.color.r, particula.color.g, particula.color.b)
				pen.setColor(color)
				self.scene.addLine(0, d, particula.distancia, d, pen)
				d += 1


		elif self.ui.comboOrdenar.currentText() == "Distancia":
			self.particulas.sort(key=lambda particula:particula.distancia, reverse=True)
			d = 0
			for particula in self.particulas:
				color = QColor(particula.color.r, particula.color.g, particula.color.b)
				pen.setColor(color)
				self.scene.addLine(0, d, particula.distancia, d, pen)
				d += 1
	
	def getDistanceBetween(self, x1, y1, x2, y2):
		return math.sqrt(
							(x2 - x1) ** 2
							+ ((y2 - y1) ** 2)
							)
	def inputInitialVertex(self):
		inputDialog = InicioWindow(self)
		if inputDialog.exec() == QDialog.Rejected:
			return
		if not inputDialog.y or not inputDialog.x:
			QMessageBox.information(self, "Particulas", "Campo/s vacio/s")
			return
		x = int(inputDialog.x)
		y = int(inputDialog.y)
		if not (x,y) in self.grafo:
			QMessageBox.information(self, "Particulas", "Vertice no valido")
			return
		return (x,y)
	@Slot()
	def puntosCercanos(self):
		indice = 0
		objetivo = 0
		for punto in self.puntos:
			if indice == len(self.puntos) - 1:
				minimo = self.getDistanceBetween(punto['x'], punto['y'], self.puntos[0]['x'], self.puntos[0]['y'])
				objetivo = self.puntos[0]
			else:
				minimo = self.getDistanceBetween(punto['x'], punto['y'], self.puntos[indice + 1]['x'], self.puntos[indice + 1]['y'])
				objetivo = self.puntos[indice + 1]
			for puntoComparacion in self.puntos:
				if puntoComparacion == punto:
					continue
				distance = self.getDistanceBetween(punto['x']
											,punto['y']
											,puntoComparacion['x']
											,puntoComparacion['y'])
				if distance < minimo:
					minimo = distance
					objetivo = puntoComparacion
					#
			#Pintamos la linea
			pen = QPen()
			pen.setWidth(3)
			color = QColor(punto["color"].r, punto["color"].g, punto["color"].b)
			pen.setColor(color)
			self.scene.addLine(punto["x"] + 3, punto["y"] + 3, objetivo["x"] + 3, objetivo["y"] + 3, pen)
			indice += 1
	@Slot()
	def BFSDFS(self):
		vertex = self.inputInitialVertex()
		if not vertex:
			return
		x = vertex[0]
		y = vertex[1]
		self.DFS(x,y)
		self.BFS(x,y)
	def BFS(self,x,y):
		print("***Amplitud***")
		visitados = []
		cola = []
		visitados.append((x,y))
		cola.append((x,y))
		while cola:
			verticeActual = cola.pop(0)
			print(verticeActual)
			for vertice in self.grafo[verticeActual]:
				vertice = vertice[0]
				if not vertice in visitados:
					cola.append(vertice)
					visitados.append(vertice)
	def DFS(self,x,y):
		print("***Profundidad***")
		visitados = []
		pila = []
		visitados.append((x,y))
		pila.append((x,y))
		while pila:
			verticeActual = pila.pop()
			print(verticeActual)
			for vertice in self.grafo[verticeActual]:
				vertice = vertice[0]
				if not vertice in visitados:
					pila.append(vertice)
					visitados.append(vertice)
	@Slot()
	def prim(self):
		vertex = self.inputInitialVertex()
		if not vertex:
			return
		x = vertex[0]
		y = vertex[1]
		expansionMinima = []
		visitados = []
		pq = PriorityQueue()
		visitados.append((x,y))
		for vertice in self.grafo[(x,y)]:
			pq.put((vertice[1],[(x,y),vertice[0]]))
		while not pq.empty():
			actual = pq.get()
			if not actual[1][1] in visitados:
				visitados.append(actual[1][1])
				for vertice in self.grafo[actual[1][1]]:
					if not vertice[0] in visitados:
						pq.put((vertice[1],(actual[1][1],vertice[0])))
				expansionMinima.append(actual)
		print("")
		print("Minimo")
		for ver in expansionMinima:
			print (ver)
		pen = QPen()
		pen.setWidth(3)
		for particula in expansionMinima:
			color = QColor(255,0,0)
			pen.setColor(color)
			self.scene.addLine(particula[1][0][0] + 3, particula[1][0][1] + 3, particula[1][1][0] + 3, particula[1][1][1] + 3, pen)