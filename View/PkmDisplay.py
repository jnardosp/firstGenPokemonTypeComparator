# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PkmDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
"""
Este documento tiene la definición de la pantalla donde se puede buscar de a un pokemon. 
"""

class Ui_PkmDisplay(object):
    def setupUi(self, Ui_PkmDisplay):
        Ui_PkmDisplay.setObjectName("Ui_PkmDisplay")
        Ui_PkmDisplay.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ui_PkmDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 30, 531, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.getPokemon = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.getPokemon.setObjectName("getPokemon")
        self.gridLayout.addWidget(self.getPokemon, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.type = QtWidgets.QLabel(self.gridLayoutWidget)
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.nombre = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nombre.setObjectName("nombre")
        self.gridLayout.addWidget(self.nombre, 1, 1, 1, 1)
        self.img = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img.setObjectName("img")
        self.gridLayout.addWidget(self.img, 3, 1, 1, 1)
        Ui_PkmDisplay.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_PkmDisplay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName("menubar")
        self.menuPokedex = QtWidgets.QMenu(self.menubar)
        self.menuPokedex.setObjectName("menuPokedex")
        Ui_PkmDisplay.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_PkmDisplay)
        self.statusbar.setObjectName("statusbar")
        Ui_PkmDisplay.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPokedex.menuAction())

        self.retranslateUi(Ui_PkmDisplay)
        QtCore.QMetaObject.connectSlotsByName(Ui_PkmDisplay)

    def retranslateUi(self, Ui_PkmDisplay):
        _translate = QtCore.QCoreApplication.translate
        Ui_PkmDisplay.setWindowTitle(_translate("Ui_PkmDisplay", "MainWindow"))
        self.getPokemon.setText(_translate("Ui_PkmDisplay", "Buscar"))
        self.type.setText(_translate("Ui_PkmDisplay", "tipo"))
        self.nombre.setText(_translate("Ui_PkmDisplay", "Nombre"))
        self.img.setText(_translate("Ui_PkmDisplay", "img"))
        self.menuPokedex.setTitle(_translate("Ui_PkmDisplay", "Pokedex"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_PkmDisplay = QtWidgets.QMainWindow()
    ui = Ui_PkmDisplay()
    ui.setupUi(Ui_PkmDisplay)
    Ui_PkmDisplay.show()
    sys.exit(app.exec_())
'''