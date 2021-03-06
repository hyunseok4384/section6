import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TestForm(QMainWindow): #QMainWindow가 QtWidgets보다 더 좋음
    def __init__(self):
        super().__init__() #이거 뭐임??
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test") #타이틀
        self.setGeometry(800,400,500,300) #실행되는 위치 지정(x, y, 가로길이, 세로길이)

        btn_1 = QPushButton("Click1", self)
        btn_2 = QPushButton("Click2", self)
        btn_3 = QPushButton("Click3", self)

        btn_1.move(20,20) #버튼 위치(x, y)
        btn_2.move(20,60)
        btn_3.move(20,100)

        btn_1.clicked.connect(self.btn_1_clicked) #btn_1이 클릭되면 btn_1_clicked함수에 연결
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit)

    def btn_1_clicked(self):
        QMessageBox.about(self,"message","clicked")

    def btn_2_clicked(self):
        print("Button Click")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()


    app.exec_()
