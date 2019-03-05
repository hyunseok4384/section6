import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
from PyQt5 import uic
from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
import datetime
import re

#form_class = uic.loadUiType(r"C:\section6\ui\you_viewer_v1.0.ui")[0]

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #초기화
        self.setupUi(self)
        #초기 잠금
        self.initAuthLock()
        #시그널 초기화
        self.initSignal()

        #로그인 관련 변수 선언
        self.user_id = None
        self.user_pwd = None

        #재생 여부
        self.is_play = False

    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg("인증안됨")

    #기본 UI 활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg("인증완료")

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
        self.previewButton.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def append_log_msg(self,act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
        app_msg = self.user_id + " : " + act + " - (" + nowDatetime + ")"
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg) #insertPlainText

        #활동 로그 저장(또는 DB를 사용 추천)
        with open(r"C:\section6\log\log.txt","a") as f:
            f.write(app_msg+"\n")

    @pyqtSlot()
    def authCheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pwd = dlg.user_pwd

        #이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        #유저 정보 및 유효기간을 체크하는 코드를 넣어주세요.
        #code
        #code
        #print("id : %s password : %s" %(self.user_id, self.user_pwd))

        if True:
            self.initAuthActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
            self.append_log_msg("login Success")
        else:
            QMessageBox.about(self,"인증오류","아이디 또는 비번 오류")

    def load_url(self):
        url = self.urlTextEdit.text().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play:
            pass
        else:
            if v.match(url) is not None:
                self.append_log_msg("Play Click")
                self.webEngineView.load(QUrl(url))
                self.showStatusMsg(url+"재생 중")
                self.previewButton.setText("중지")
                self.is_play = True
                self.startButton.setEnabled(True)
            else:
                QMessageBox.about(self,"URL 형식 오류","유튜브 주소형식이 아닙니다")
                self.urlTextEdit.clear()
                self.urlTextEdit.setFocus(True)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
