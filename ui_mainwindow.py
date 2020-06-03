# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(958, 819)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionVerPuntos = QAction(MainWindow)
        self.actionVerPuntos.setObjectName(u"actionVerPuntos")
        self.actionFuerzaBruta = QAction(MainWindow)
        self.actionFuerzaBruta.setObjectName(u"actionFuerzaBruta")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.actionBFSDFS = QAction(MainWindow)
        self.actionBFSDFS.setObjectName(u"actionBFSDFS")
        self.actionPrim = QAction(MainWindow)
        self.actionPrim.setObjectName(u"actionPrim")
        self.actionKruskal = QAction(MainWindow)
        self.actionKruskal.setObjectName(u"actionKruskal")
        self.actionDijkstra = QAction(MainWindow)
        self.actionDijkstra.setObjectName(u"actionDijkstra")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txtAreaParticula = QPlainTextEdit(self.tab)
        self.txtAreaParticula.setObjectName(u"txtAreaParticula")

        self.gridLayout_2.addWidget(self.txtAreaParticula, 0, 1, 3, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAgregar = QPushButton(self.tab)
        self.btnAgregar.setObjectName(u"btnAgregar")

        self.horizontalLayout.addWidget(self.btnAgregar)

        self.btnMostrar = QPushButton(self.tab)
        self.btnMostrar.setObjectName(u"btnMostrar")

        self.horizontalLayout.addWidget(self.btnMostrar)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(36)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.RightToLeft)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.txtId = QLineEdit(self.tab)
        self.txtId.setObjectName(u"txtId")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtId)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.txtOrigen = QLineEdit(self.tab)
        self.txtOrigen.setObjectName(u"txtOrigen")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtOrigen)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.txtDestino = QLineEdit(self.tab)
        self.txtDestino.setObjectName(u"txtDestino")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtDestino)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.txtVelocidad = QLineEdit(self.tab)
        self.txtVelocidad.setObjectName(u"txtVelocidad")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txtVelocidad)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.txtColor = QLineEdit(self.tab)
        self.txtColor.setObjectName(u"txtColor")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.txtColor)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.txtDistancia = QLineEdit(self.tab)
        self.txtDistancia.setObjectName(u"txtDistancia")
        self.txtDistancia.setEnabled(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.txtDistancia)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.txtBuscar = QLineEdit(self.tab_2)
        self.txtBuscar.setObjectName(u"txtBuscar")

        self.horizontalLayout_2.addWidget(self.txtBuscar)

        self.btnBuscar = QPushButton(self.tab_2)
        self.btnBuscar.setObjectName(u"btnBuscar")

        self.horizontalLayout_2.addWidget(self.btnBuscar)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.btnMostrarTabla = QPushButton(self.tab_2)
        self.btnMostrarTabla.setObjectName(u"btnMostrarTabla")
        self.btnMostrarTabla.setMaximumSize(QSize(1000000, 16777215))

        self.gridLayout_3.addWidget(self.btnMostrarTabla, 2, 0, 1, 1)

        self.tblParticulas = QTableWidget(self.tab_2)
        self.tblParticulas.setObjectName(u"tblParticulas")
        self.tblParticulas.setMinimumSize(QSize(0, 500))
        self.tblParticulas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tblParticulas.setRowCount(0)
        self.tblParticulas.setColumnCount(0)
        self.tblParticulas.horizontalHeader().setCascadingSectionResizes(False)
        self.tblParticulas.horizontalHeader().setMinimumSectionSize(100)
        self.tblParticulas.horizontalHeader().setDefaultSectionSize(100)
        self.tblParticulas.horizontalHeader().setStretchLastSection(False)
        self.tblParticulas.verticalHeader().setDefaultSectionSize(30)

        self.gridLayout_3.addWidget(self.tblParticulas, 1, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 5)
        self.gridLayout_3.setRowStretch(1, 90)
        self.gridLayout_3.setRowStretch(2, 5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnLimpiar = QPushButton(self.tab_3)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLimpiar.sizePolicy().hasHeightForWidth())
        self.btnLimpiar.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.btnLimpiar, 1, 1, 1, 1)

        self.btnDibujar = QPushButton(self.tab_3)
        self.btnDibujar.setObjectName(u"btnDibujar")

        self.gridLayout_4.addWidget(self.btnDibujar, 1, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.btnOrdenar = QPushButton(self.tab_3)
        self.btnOrdenar.setObjectName(u"btnOrdenar")

        self.gridLayout_4.addWidget(self.btnOrdenar, 2, 0, 1, 1)

        self.comboOrdenar = QComboBox(self.tab_3)
        self.comboOrdenar.addItem("")
        self.comboOrdenar.addItem("")
        self.comboOrdenar.setObjectName(u"comboOrdenar")
        self.comboOrdenar.setStyleSheet(u"")
        self.comboOrdenar.setEditable(False)
        self.comboOrdenar.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_4.addWidget(self.comboOrdenar, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 958, 19))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        self.menuAlgoritmos_2 = QMenu(self.menubar)
        self.menuAlgoritmos_2.setObjectName(u"menuAlgoritmos_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menubar.addAction(self.menuAlgoritmos_2.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAlgoritmos.addAction(self.actionVerPuntos)
        self.menuAlgoritmos.addAction(self.actionGrafo)
        self.menuAlgoritmos_2.addAction(self.actionFuerzaBruta)
        self.menuAlgoritmos_2.addAction(self.actionBFSDFS)
        self.menuAlgoritmos_2.addAction(self.actionPrim)
        self.menuAlgoritmos_2.addAction(self.actionKruskal)
        self.menuAlgoritmos_2.addAction(self.actionDijkstra)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionVerPuntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.actionFuerzaBruta.setText(QCoreApplication.translate("MainWindow", u"Puntos mas cercanos", None))
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.actionBFSDFS.setText(QCoreApplication.translate("MainWindow", u"Recorrido profundidad/amplitud", None))
        self.actionPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.actionKruskal.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.actionDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.btnAgregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen(x,y)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destino(x,y)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Color(r,g,b)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Distancia", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnMostrarTabla.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnDibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.btnOrdenar.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.comboOrdenar.setItemText(0, QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.comboOrdenar.setItemText(1, QCoreApplication.translate("MainWindow", u"Distancia", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Grafico", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAlgoritmos_2.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

