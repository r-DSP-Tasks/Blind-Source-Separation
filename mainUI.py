# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 320)
        MainWindow.setMaximumSize(QtCore.QSize(460, 320))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.result2 = QtWidgets.QPushButton(self.centralwidget)
        self.result2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-play-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.result2.setIcon(icon)
        self.result2.setIconSize(QtCore.QSize(60, 60))
        self.result2.setFlat(True)
        self.result2.setObjectName("result2")
        self.gridLayout.addWidget(self.result2, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/icons8-save-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon1)
        self.save.setIconSize(QtCore.QSize(96, 96))
        self.save.setFlat(True)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 3, 1, 1, 1)
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/icons8-import-file-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load.setIcon(icon2)
        self.load.setIconSize(QtCore.QSize(60, 60))
        self.load.setFlat(True)
        self.load.setObjectName("load")
        self.gridLayout.addWidget(self.load, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.result1 = QtWidgets.QPushButton(self.centralwidget)
        self.result1.setText("")
        self.result1.setIcon(icon)
        self.result1.setIconSize(QtCore.QSize(60, 60))
        self.result1.setFlat(True)
        self.result1.setObjectName("result1")
        self.gridLayout.addWidget(self.result1, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Component Analysis"))
        self.label_2.setText(_translate("MainWindow", "Result 1"))
        self.label_3.setText(_translate("MainWindow", "Result 2"))
        self.label.setText(_translate("MainWindow", "Load file"))
        self.label_4.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

