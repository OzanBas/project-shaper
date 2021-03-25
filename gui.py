from PyQt5 import QtCore, QtGui, QtWidgetsimport functions as fcsclass Ui_mainwindow(object):    def setupUi(self, mainwindow):        mainwindow.setObjectName("mainwindow")        mainwindow.resize(497, 322)        font = QtGui.QFont()        font.setBold(False)        font.setWeight(50)        mainwindow.setFont(font)        self.centralwidget = QtWidgets.QWidget(mainwindow)        self.centralwidget.setObjectName("centralwidget")        b1 = self.pushButton = QtWidgets.QPushButton('show messagebox', self.centralwidget)        self.pushButton.setGeometry(QtCore.QRect(10, 60, 141, 41))        self.pushButton.setObjectName("pushButton")        b1.clicked.connect(fcs.func_Single)        b2 = self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)        self.pushButton_2.setGeometry(QtCore.QRect(10, 110, 141, 41))        self.pushButton_2.setObjectName("pushButton_2")        b2.clicked.connect(fcs.func_Multiple)        b3 = self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)        self.pushButton_3.setGeometry(QtCore.QRect(10, 160, 141, 41))        self.pushButton_3.setObjectName("pushButton_3")        b3.clicked.connect(fcs.func_Clean)        b4 = self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)        self.pushButton_4.setGeometry(QtCore.QRect(10, 210, 141, 41))        self.pushButton_4.setObjectName("pushButton_4")        b4.clicked.connect(QtWidgets.qApp.quit)        self.label = QtWidgets.QLabel(self.centralwidget)        self.label.setGeometry(QtCore.QRect(160, 70, 311, 21))        self.label.setObjectName("label")        self.label_2 = QtWidgets.QLabel(self.centralwidget)        self.label_2.setGeometry(QtCore.QRect(160, 120, 341, 21))        self.label_2.setObjectName("label_2")        self.label_3 = QtWidgets.QLabel(self.centralwidget)        self.label_3.setGeometry(QtCore.QRect(160, 170, 331, 21))        self.label_3.setObjectName("label_3")        self.label_4 = QtWidgets.QLabel(self.centralwidget)        self.label_4.setGeometry(QtCore.QRect(160, 220, 231, 21))        self.label_4.setObjectName("label_4")        self.label_5 = QtWidgets.QLabel(self.centralwidget)        self.label_5.setGeometry(QtCore.QRect(170, 0, 200, 31))        font = QtGui.QFont()        font.setPointSize(13)        font.setBold(True)        font.setWeight(75)        font.setStrikeOut(False)        self.label_5.setFont(font)        self.label_5.setObjectName("label_5")        mainwindow.setCentralWidget(self.centralwidget)        self.menubar = QtWidgets.QMenuBar(mainwindow)        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 22))        self.menubar.setObjectName("menubar")        mainwindow.setMenuBar(self.menubar)        self.statusbar = QtWidgets.QStatusBar(mainwindow)        self.statusbar.setObjectName("statusbar")        mainwindow.setStatusBar(self.statusbar)        self.retranslateUi(mainwindow)        QtCore.QMetaObject.connectSlotsByName(mainwindow)    def retranslateUi(self, mainwindow):        _translate = QtCore.QCoreApplication.translate        mainwindow.setWindowTitle(_translate("mainwindow", "Shaper3.0"))        self.pushButton.setText(_translate("mainwindow", "Tek Dosya"))        self.pushButton_2.setText(_translate("mainwindow", "Çoklu Dosya"))        self.pushButton_3.setText(_translate("mainwindow", "Mutfak Reçete"))        self.pushButton_4.setText(_translate("mainwindow", "Çıkış"))        self.label.setText(_translate("mainwindow", "Tek bir reçeteyi aynı excel üzerinde düzenler."))        self.label_2.setText(_translate("mainwindow", "Çok sayıda reçeteyi düzenleyip yeni klasöre alır."))        self.label_3.setText(_translate("mainwindow", "Reçeteyi mutfağın istediği formatta düzenler." ))        self.label_4.setText(_translate("mainwindow", "Geliştirme Mayıs2020 // Güncelleme Mart2021"))        self.label_5.setText(_translate("mainwindow", "REÇETE FORMATLAMA"))if __name__ == "__main__":    import sys    app = QtWidgets.QApplication(sys.argv)    mainwindow = QtWidgets.QMainWindow()    ui = Ui_mainwindow()    ui.setupUi(mainwindow)    mainwindow.show()    sys.exit(app.exec())