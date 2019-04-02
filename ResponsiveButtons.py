# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResponsiveButtons.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 821, 621))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color:\"red\";color:\"white\";padding:30px;border-radius:10px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setStyleSheet("background-color:\"red\";color:\"white\";padding:30px;border-radius:10px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_7.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("background-color:\"red\";color:\"white\";padding:30px;border-radius:10px")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setStyleSheet("background-color:\"red\";color:\"white\";padding:30px;border-radius:10px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.on_button_1_click)
        self.pushButton_3.clicked.connect(self.on_button_2_click)
        self.pushButton.clicked.connect(self.on_button_3_click)
        self.pushButton_4.clicked.connect(self.on_button_4_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton1"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton2"))
        self.pushButton.setText(_translate("MainWindow", "PushButton3"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton4"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

    def on_button_1_click(self):
        self.label.setText("Testing button 1")

    def on_button_2_click(self):
        self.label.setText("Testing button 2")

    def on_button_3_click(self):
        self.label.setText("Testing button 3")

    def on_button_4_click(self):
        self.label.setText("Testing button 4") 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    MainWindow.show()
    sys.exit(app.exec_())

