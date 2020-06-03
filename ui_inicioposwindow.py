# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicioposwindow.ui'
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


class Ui_inicioPos(object):
    def setupUi(self, inicioPos):
        if inicioPos.objectName():
            inicioPos.setObjectName(u"inicioPos")
        inicioPos.setWindowModality(Qt.ApplicationModal)
        inicioPos.resize(400, 300)
        self.verticalLayout_3 = QVBoxLayout(inicioPos)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(inicioPos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(inicioPos)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txtX = QLineEdit(inicioPos)
        self.txtX.setObjectName(u"txtX")

        self.horizontalLayout.addWidget(self.txtX)

        self.label_2 = QLabel(inicioPos)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.txtY = QLineEdit(inicioPos)
        self.txtY.setObjectName(u"txtY")

        self.horizontalLayout.addWidget(self.txtY)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAceptar = QPushButton(inicioPos)
        self.btnAceptar.setObjectName(u"btnAceptar")

        self.horizontalLayout_2.addWidget(self.btnAceptar)

        self.btnCancelar = QPushButton(inicioPos)
        self.btnCancelar.setObjectName(u"btnCancelar")

        self.horizontalLayout_2.addWidget(self.btnCancelar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(inicioPos)

        QMetaObject.connectSlotsByName(inicioPos)
    # setupUi

    def retranslateUi(self, inicioPos):
        inicioPos.setWindowTitle(QCoreApplication.translate("inicioPos", u"Inicio", None))
        self.label_3.setText(QCoreApplication.translate("inicioPos", u"Vertice inicial", None))
        self.label.setText(QCoreApplication.translate("inicioPos", u"X:", None))
        self.label_2.setText(QCoreApplication.translate("inicioPos", u"Y:", None))
        self.btnAceptar.setText(QCoreApplication.translate("inicioPos", u"Aceptar", None))
        self.btnCancelar.setText(QCoreApplication.translate("inicioPos", u"Cancelar", None))
    # retranslateUi

