# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Heap.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Heap(object):
    def setupUi(self, Heap):
        Heap.setObjectName("Heap")
        Heap.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Heap)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 30, 671, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sortAZ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sortAZ.setObjectName("sortAZ")
        self.gridLayout_2.addWidget(self.sortAZ, 0, 3, 1, 1)
        self.sortMax = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sortMax.setObjectName("sortMax")
        self.gridLayout_2.addWidget(self.sortMax, 0, 2, 1, 1)
        self.sortMin = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sortMin.setObjectName("sortMin")
        self.gridLayout_2.addWidget(self.sortMin, 0, 1, 1, 1)
        self.sortZA = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sortZA.setObjectName("sortZA")
        self.gridLayout_2.addWidget(self.sortZA, 0, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 1, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 2, 1)
        Heap.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Heap)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName("menubar")
        Heap.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Heap)
        self.statusbar.setObjectName("statusbar")
        Heap.setStatusBar(self.statusbar)

        self.retranslateUi(Heap)
        QtCore.QMetaObject.connectSlotsByName(Heap)

    def retranslateUi(self, Heap):
        _translate = QtCore.QCoreApplication.translate
        Heap.setWindowTitle(_translate("Heap", "MainWindow"))
        self.pushButton.setText(_translate("Heap", "Volver"))
        self.sortAZ.setText(_translate("Heap", "A-Z"))
        self.sortMax.setText(_translate("Heap", "151 - 1"))
        self.sortMin.setText(_translate("Heap", "1 - 151"))
        self.sortZA.setText(_translate("Heap", "Z-A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Heap = QtWidgets.QMainWindow()
    ui = Ui_Heap()
    ui.setupUi(Heap)
    Heap.show()
    sys.exit(app.exec_())
