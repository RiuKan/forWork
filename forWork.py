import webbrowser
from re import findall
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from tkinter import *
import tkinter.filedialog
import os

from requests import get, post

from bs4 import BeautifulSoup
from time import strftime, localtime, time


        #날짜 비교 elif 넣기


class MakingLabel(QLabel):

    def __init__(self,text):
        super(MakingLabel, self).__init__(text)
        self.setText(text)
class MakingButton(QPushButton):
    def __init__(self,text):
        super(MakingButton, self).__init__(text)
        self.setText(text)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(60, 110, 1011, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 3, 1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QRect(120, 30, 171, 51))
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_today = QPushButton(self.centralwidget)
        self.pushButton_today.setGeometry(QRect(50, 50, 61, 31))
        self.pushButton_today.setObjectName("pushButton_today")
        self.pushButton_sym = QPushButton(self.centralwidget)
        self.pushButton_sym.setGeometry(QRect(10, 110, 41, 51))
        self.pushButton_sym.setObjectName("pushButton_sym")
        self.pushButton_bog = QPushButton(self.centralwidget)
        self.pushButton_bog.setGeometry(QRect(10, 430, 41, 51))
        self.pushButton_bog.setObjectName("pushButton_bog")
        self.pushButton_web = QPushButton(self.centralwidget)
        self.pushButton_web.setGeometry(QRect(880, 30, 151, 28))
        self.pushButton_web.setObjectName("pushButton_web")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1141, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "보건복지부"))
        self.label.setText(_translate("MainWindow", "심평원"))
        self.pushButton_today.setText(_translate("MainWindow", "오늘"))
        self.pushButton_sym.setText(_translate("MainWindow", "목록"))
        self.pushButton_bog.setText(_translate("MainWindow", "목록"))
        self.pushButton_web.setText(_translate("MainWindow", "브라우저 파일 지정"))


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setUI()
        self.getList(strftime('%Y-%m-%d', localtime(time())))
        self.dateEdit.setDate(QDate.currentDate())
        self.pushButton_today.clicked.connect(lambda: self.today_button_clicked())
        self.pushButton_sym.clicked.connect(lambda : self.sym_button_clicked())
        self.pushButton_bog.clicked.connect(lambda : self.bog_button_clicked())
        self.pushButton_web.clicked.connect(lambda: self.web_button_clicked())
        global web_localURL
        web_localURL = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        webbrowser.register("wb", None,webbrowser.BackgroundBrowser(web_localURL))







        # for 이중 loop로 리스트 안의 리스트 뽑아서 공간에 넣기 (마지막은 버튼)
        self.dateEdit.dateChanged.connect(lambda: self.getList(self.dateEdit.date().toString("yyyy-MM-dd")))
    def today_button_clicked(self):
        self.dateEdit.setDate(QDate.currentDate())
    def bog_button_clicked(self):
        webbrowser.get("wb").open("http://www.mohw.go.kr/react/jb/sjb0406ls.jsp?PAR_MENU_ID=03&MENU_ID=030406#")
    def web_button_clicked(self):
        global web_localURL

        web_select = QMessageBox.question(self, "웹브라우저 경로 설정",
                                          "현재 경로:\n'%s'\n바꾸시겠습니까?\n\n(원하는 웹브라우저의 exe 파일을 지정해주시면 됩니다.)"%web_localURL,
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if web_select == QMessageBox.Yes:

            roots = Tk()
            pre_url = tkinter.filedialog.askopenfilename()
            if pre_url == "":
                pass
            else:
                web_localURL = pre_url
                webbrowser.register("wb", None,webbrowser.BackgroundBrowser(pre_url))

# TODO 매번 새롭게 불러오는 것 보단, 이미 불러온 자료는 임시로 변수 저장해놓는게 좋지 않을까? 다만, 실시간으로 새로뜨는 공시가 나올 수 있어서 더 생각,
# TODO 다시 봐도 쉽게 파악할 수 있도록, 기능 기록을 습관화 하자.
# TODO 읽음 처리 방법 생각. (체크박스 파일 저장 csv로)
# TODO 두개 버전으로 커스톰 가능하도록,
# TODO 창크기 유연하게 바뀌도록
# TODO 달력에 표시, 해당 달꺼만
# TODO 오늘 공시가 올라온 사이트는 버튼 색 표시
# TODO 로딩에 필요한 것들 분산하기 (속도 분산)
# TODO 파일을 다운로드 받아 바로 열 수 있도록, 파일 선택 가능하도록
# TODO 링크와 내용 분리(팝업으로 내용(표 나타내는법 알아내야함) 보여주고, 링크는 버튼으로 놔두기)

# TODO 기억할 것은 최소한 바로가기 해놓은 것 보다 편리해야하고, 뇌의 처리과정을 단축시켜줘야한다.
# TODO 오늘 공시가 올라온 사이트가 뭘까 -> 다 켜는것이 아닌, 버튼의 색깔로 한번에 구분
# TODO 사이트를 다 켜고도, 날짜를 구분해 확인해야하는 번거로움, 해당 날짜만 뽑아서 보여주기.
            roots.destroy()

    def sym_button_clicked(self):



        webbrowser.get("wb").open("http://www.hira.or.kr/bbsDummy.do?pgmid=HIRAA020002000100")

        # TODO 중복되는 함수들 한 변수로 받고 넘겨주기,strftime('%Y-%m-%d', localtime(time()))


    def loop_bog(self, date):
        response_bog = get("http://www.mohw.go.kr/react/jb/sjb0406ls.jsp?PAR_MENU_ID=03&MENU_ID=030406&page=1")
        soup_bog = BeautifulSoup(response_bog.text, 'html.parser')
        texts_bog = soup_bog.select("table>tbody>tr")
        global list_all_bog
        list_all_bog = []
        for i in range(0, 30, 2):
                # "%s" % time.strftime('%Y-%m-%d', time.localtime(time.time()))

            if texts_bog[i].select("td")[4].get_text() == date:
                list = []
                for s in range(1, 6):
                    if s == 2 or s == 3 or s == 4:

                        list.append(texts_bog[i].select("td")[s].get_text())
                    elif s == 1:
                        rep = texts_bog[i].select("td")[s].get_text()
                        rep = rep.lstrip("\r\n\t")
                        rep = rep.rstrip("\t\n\r")

                        list.append(rep)
                    elif s == 5:


                            site_number = soup_bog.select("table>tbody>tr>td>a")[i]['onclick']
                            site_number = site_number.replace("","")
                            site_number = site_number.rstrip(";)'")
                            site_number = site_number.lstrip("moveAction('")
                            list.append(site_number)






                list_all_bog.append(list)
        self.gridLayout_2.setHorizontalSpacing(len(list_all_bog))
        for i in reversed(range(self.gridLayout_2.count())):
            self.gridLayout_2.itemAt(i).widget().deleteLater()
        if len(list_all_bog) == 0:
            cell = MakingLabel("공시 없음")

            self.gridLayout_2.addWidget(cell, 0, 0)

        else:
            for x in range(0, len(list_all_bog)):
                for y in range(0, 5):
                    if y == 0 or y ==1 or y == 3:
                        cell = MakingLabel(list_all_bog[x][y])


                        self.gridLayout_2.addWidget(cell, x, y)
                    elif y == 2:
                        cell = MakingLabel('<a href = "http://www.mohw.go.kr/react/jb/sjb0406vw.jsp?PAR_MENU_ID=03&MENU_ID=030406&SEARCHKEY=&SEARCHVALUE=&page=1&CONT_SEQ=%s&nowRowCnt=15">%s</a>' % (list_all_bog[x][4], list_all_bog[x][y]))

                        cell.linkActivated.connect(lambda: self.link_activated("bog"))
                        self.gridLayout_2.addWidget(cell, x, y)
                    elif y == 4:
                        button = MakingButton("문서")

                        button.clicked.connect(lambda:self.buttonClicked("bog"))
                        self.gridLayout_2.addWidget(button,x,y)
    def link_activated(self,str):
        if str == "bog":
            a = self.sender().text()
            soup = BeautifulSoup(a,"html.parser")
            webbrowser.get("wb").open(soup.select("a")[0]['href'])
        elif str == "sym":
            a = self.sender().text()
            soup = BeautifulSoup(a, "html.parser")
            webbrowser.get("wb").open(soup.select("a")[0]['href'])


    def loop_sym(self, date):
        response_sym = get("http://www.hira.or.kr/bbsDummy.do?pgmid=HIRAA020002000100")
        soup_sym = BeautifulSoup(response_sym.text, 'html.parser')
        texts_sym = soup_sym.select("tbody>tr")

        global list_all_sym
        list_all_sym = []
        # http://www.hira.or.kr/bbsDummy.do?
        for i in range(0, 10):
                # "%s" % time.strftime('%Y-%m-%d', time.localtime(time.time()))

            if texts_sym[i].select("td")[3].get_text() == date:
                list = []
                for s in range(1, 5):

                    if s != 4:
                        list.append(texts_sym[i].select("td")[s].get_text())
                    elif s == 4:
                        list.append("http://www.hira.or.kr/bbsDummy.do" + soup_sym.select('tbody>tr>td>a')[i]['href'])
                list_all_sym.append(list)
        self.gridLayout.setHorizontalSpacing(len(list_all_sym))
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().deleteLater()
        if len(list_all_sym) == 0:
            cell = MakingLabel("공시 없음")

            self.gridLayout.addWidget(cell, 0, 0)

        else:
            for x in range(0, len(list_all_sym)):
                for y in range(0, 4):
                    if y == 1 or y == 2:
                        cell = MakingLabel(list_all_sym[x][y])


#<a href=\"http://www.google.com\">'Click this link to go to Google'</a>

    #TODO 반복적으로 쓰이는 list_all_sym[x][3]는 전역변수 설정해서 한번에 갖다쓰게 하는게 낫지 않을까?

                        self.gridLayout.addWidget(cell, x, y)
                    elif y == 0:
                        cell = MakingLabel('<a href="%s">%s</a>' % (list_all_sym[x][3], list_all_sym[x][y]))
                        cell.linkActivated.connect(lambda: self.link_activated("sym"))
                        self.gridLayout.addWidget(cell, x, y)
                        # TODO 굳이 라벨 만들때 하이퍼링크 길게, 레퍼런스 해서 넣을 필요 없긴 함. 그냥 아무거나해줘서 하이퍼만 걸면 됨.
                    elif y == 3:
                        # TODO 따로 다운받아지게 하는 것

                        button = MakingButton("문서")


                        button.clicked.connect(lambda : self.buttonClicked("sym"))

                        self.gridLayout.addWidget(button, x, y)

    def buttonClicked(self,str):
        if str == "sym":
            x = self.gridLayout.indexOf(self.sender())//4

            response_button_sym = get(list_all_sym[x][3])
            soup_button_sym = BeautifulSoup(response_button_sym.text, 'html.parser')
            download_numbers = soup_button_sym.select("tbody>tr>td>ul>li>a")

            numbers = []
            names = []
            for i in range(len(download_numbers)):
                numbers.append(findall("\d+", download_numbers[i]['onclick']))
                names.append(download_numbers[i].get_text())
            if download_numbers != []:


                message_box = QMessageBox.question(self,"문서 다운로드","%s"%names,QMessageBox.
                                                  Yes|QMessageBox.No,QMessageBox.No)
                if message_box == QMessageBox.Yes:
                    root = Tk()
                    root.directory = tkinter.filedialog.askdirectory()


                    if root.directory != "":
                        for i in range(0, len(numbers)):

                            response = get("http://www.hira.or.kr/bbs/bbsCDownLoad.do?apndNo=%s&apndBrdBltNo=%s&apndBrdTyNo=%s&apndBltNo=%s" % (numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3]))

                            filename = response.headers['Content-Disposition'].replace("attachment; filename=","")



                            with open(root.directory+"/"+"%s%s"%(names[i],filename[filename.rfind("."):-1]), "wb") as file:

                                file.write(response.content)
                        root.destroy()

                    elif root.directory == "":
                        root.destroy()


            else:
                w = QWidget
                message_box = QMessageBox.question(self, "", "파일이 없습니다. 링크를 확인하시겠습니까?",
                                                   QMessageBox.
                                                   Yes | QMessageBox.No, QMessageBox.No)
                if message_box == QMessageBox.Yes:
                    webbrowser.get("wb").open(list_all_sym[x][3])





        elif str == "bog":
            x = self.gridLayout_2.indexOf(self.sender()) // 5

            data = {"PAR_MENU_ID":"03","MENU_ID":"030406","SEARCHKEY":"","SEARCHVALUE":"","page":"1","CONT_SEQ":"%s"%list_all_bog[x][4],"nowRowCnt":"15"}
            response_button_bog = post("http://www.mohw.go.kr/react/jb/sjb0406vw.jsp", data = data)
            soup_button_bog = BeautifulSoup(response_button_bog.text, 'html.parser')

            download_urls_before = soup_button_bog.select("div.container div.bv_file div.bvf_lst li a")
            download_urls = []
            titles = []
            for i in range(0,len(download_urls_before), 2):
                download_urls.append(download_urls_before[i]['href'])
                titles.append(download_urls_before[i]['title'].replace(" 파일 다운로드",""))
            if download_urls != []:

                message_box = QMessageBox.question(self, "문서 다운로드", "%s" % titles, QMessageBox.
                                                   Yes | QMessageBox.No, QMessageBox.No)
                if message_box == QMessageBox.Yes:
                    root = Tk()

                    root.directory = tkinter.filedialog.askdirectory()


                    if root.directory != "":
                        for (index,i) in enumerate(download_urls):
                            response = get(i)


                            with open(root.directory + "/" + titles[index],"wb") as file:
                                file.write(response.content)
                        root.destroy()

                    elif root.directory == "":
                        root.destroy()



            else:

                message_box = QMessageBox.question(self, "", "파일이 없습니다. 링크를 확인하시겠습니까?",
                                                   QMessageBox.
                                                   Yes | QMessageBox.No, QMessageBox.No)
                if message_box == QMessageBox.Yes:
                    webbrowser.get("wb").open("http://www.mohw.go.kr/react/jb/sjb0406vw.jsp?PAR_MENU_ID=03&MENU_ID=030406&SEARCHKEY=&SEARCHVALUE=&page=1&CONT_SEQ=%s&nowRowCnt=15"%list_all_bog[x][4])


    def getList(self, date):
        self.loop_bog(date)
        self.loop_sym(date)




# 쓸데없이 spacing 늘리는거 제거.
# TODO 매번 긁어오는게 아니라, 미리 긁어 온거에서 날짜 일치 수집하기(그렇지 페이지 하나 긁어와서 하는거니까)
# 과거 고시 모두 긁기



    def setUI(self):
        self.setupUi(self)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    app.exec_()
