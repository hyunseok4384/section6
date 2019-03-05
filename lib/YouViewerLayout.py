# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'you_viewer_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 728)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 728))
        MainWindow.setMaximumSize(QtCore.QSize(800, 728))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/title_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 231, 411))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../resource/you_viewer_logo.png"))
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(self.groupBox)
        self.loginButton.setGeometry(QtCore.QRect(10, 130, 211, 51))
        self.loginButton.setObjectName("loginButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 200, 211, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 10, 531, 411))
        self.groupBox_2.setObjectName("groupBox_2")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.groupBox_2)
        self.webEngineView.setGeometry(QtCore.QRect(10, 20, 511, 381))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 420, 781, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 430, 391, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.label_6.setObjectName("label_6")
        self.urlTextEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.urlTextEdit.setGeometry(QtCore.QRect(90, 30, 231, 31))
        self.urlTextEdit.setObjectName("urlTextEdit")
        self.previewButton = QtWidgets.QPushButton(self.groupBox_3)
        self.previewButton.setGeometry(QtCore.QRect(332, 30, 51, 31))
        self.previewButton.setObjectName("previewButton")
        self.pathTextEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.pathTextEdit.setGeometry(QtCore.QRect(90, 80, 231, 31))
        self.pathTextEdit.setObjectName("pathTextEdit")
        self.fileNavButton = QtWidgets.QToolButton(self.groupBox_3)
        self.fileNavButton.setGeometry(QtCore.QRect(330, 80, 51, 31))
        self.fileNavButton.setObjectName("fileNavButton")
        self.streamCombobox = QtWidgets.QComboBox(self.groupBox_3)
        self.streamCombobox.setGeometry(QtCore.QRect(90, 130, 291, 31))
        self.streamCombobox.setObjectName("streamCombobox")
        self.startButton = QtWidgets.QPushButton(self.groupBox_3)
        self.startButton.setGeometry(QtCore.QRect(190, 170, 93, 51))
        self.startButton.setObjectName("startButton")
        self.exitButton = QtWidgets.QPushButton(self.groupBox_3)
        self.exitButton.setGeometry(QtCore.QRect(290, 170, 93, 51))
        self.exitButton.setObjectName("exitButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(410, 430, 381, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 361, 201))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 660, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 670, 101, 16))
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(100, 670, 20, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 670, 271, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(510, 670, 281, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 670, 101, 16))
        self.label_3.setObjectName("label_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(490, 670, 20, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "기본정보"))
        self.loginButton.setText(_translate("MainWindow", "인증"))
        self.groupBox_2.setTitle(_translate("MainWindow", "미리보기"))
        self.groupBox_3.setTitle(_translate("MainWindow", "다운로드 URL 및 저장 위치 지정"))
        self.label_4.setText(_translate("MainWindow", "Video URL :"))
        self.label_5.setText(_translate("MainWindow", "Save URL :"))
        self.label_6.setText(_translate("MainWindow", "Stream :"))
        self.previewButton.setText(_translate("MainWindow", "확인"))
        self.fileNavButton.setText(_translate("MainWindow", "..."))
        self.startButton.setText(_translate("MainWindow", "시작"))
        self.exitButton.setText(_translate("MainWindow", "종료"))
        self.groupBox_4.setTitle(_translate("MainWindow", "로그"))
        self.label_2.setText(_translate("MainWindow", "브라우저 로딩"))
        self.label_3.setText(_translate("MainWindow", "다운로드 로딩"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
