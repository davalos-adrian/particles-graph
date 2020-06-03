from color import Color
from vector2 import Vector2
import math
class Particula(object):
	"""docstring for Particula"""
	def __init__(self, id, origen, destino, velocidad, color):
		super(Particula, self).__init__()
		self.id = id
		self.origen = Vector2(origen[0], origen[1])
		self.destino = Vector2(destino[0], destino[1])
		self.velocidad = velocidad
		self.color = Color(color[0], color[1], color[2])
		self.distancia = int(math.sqrt(
									(self.destino.x - self.origen.x) ** 2
									+ ((self.destino.y - self.origen.y) ** 2)
									))
	def toString(self):
		return " Id:" +  str(self.id) + '\n' +  \
			"Origen.x: " +  str(self.origen.x) + '\n' +  \
			"Origen.y: " +  str(self.origen.y) + '\n' +  \
			"Destino.x: " +  str(self.destino.x) + '\n' +  \
			"Destino.y: " +  str(self.destino.y) + '\n' +  \
			"Velocidad: " +  str(self.velocidad) + '\n' +  \
			"Color.r: " +  str(self.color.r) + '\n' +  \
			"Color.g: " +  str(self.color.g) + '\n' +  \
			"Color.b: " +  str(self.color.b) + '\n' +  \
			"Distancia: " +  str(self.distancia)
	def __lt__(self, other):
		return self.velocidad < other.velocidad