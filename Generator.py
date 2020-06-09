import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from datetime import datetime
from PyQt5.QtCore import QDate
import random

sellerID = "YOUR_SELLER_ID"  # Here you input your seller ID (the same as your login)
crcKey = "YOUR_CRC_KEY"      # Here you input your CRC key 

SelectedDate = None

BuyerData = [None, None, None, None, None, ""]  # Name, Surname, Hour, Date, Money, Email, Email prepared


def SetDate(value):
    # print(value)
    BuyerData[3] = str(value.day()) + str(value.month()) + str(value.year())
    # print(BuyerData)


def GenerateString():
    # print(BuyerData)
    BuyerData[0] = str(ui.Name.text())
    BuyerData[1] = str(ui.Surname.text())
    if ":" in ui.TimeHHMM.text():
        BuyerData[2] = str(str(ui.TimeHHMM.text().split(":")[0]) + str(ui.TimeHHMM.text().split(":")[1]))
    elif ";" in ui.TimeHHMM.text():
        BuyerData[2] = str(str(ui.TimeHHMM.text().split(";")[0]) + str(ui.TimeHHMM.text().split(";")[1]))
    else:
        BuyerData[2] = str(ui.TimeHHMM.text())
    BuyerData[4] = str(int(float(ui.AmountOMoney.text())*100))
    if "@" in ui.lineEdit.text():
        BuyerData[5] = str(ui.lineEdit.text().replace('@', '%40'))
    else:
        BuyerData[5] = str(ui.lineEdit.text())
    # print(BuyerData)

    random.seed(int(BuyerData[2]) + int(BuyerData[3]) + 250)
    nameOfTransaction = "zabieg%20nr" + str(random.randint(0, 10000)) + BuyerData[0][0] + BuyerData[1][0]
    FinalLink = "https://sklep.przelewy24.pl/zakup.php?" + "z24_id_sprzedawcy=" + str(sellerID) + "&z24_nazwa=" + \
                nameOfTransaction + "&z24_crc=" + str(crcKey) + "&z24_kwota=" + str(BuyerData[4]) + "&k24_email=" + \
                str(BuyerData[5]) + "&z24_return_url=www.dentalcity.com.pl" + \ 
                "&k24_nazwa=" + str(BuyerData[0]) + "%20" + str(BuyerData[1])  # This is the link splicing
    # print(FinalLink)
    ui.LinkExport.setText(FinalLink)
    pyperclip.copy(FinalLink)  # This copies the link into your clipboard for ease of use
    spam = pyperclip.paste()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.DateSelector = QtWidgets.QCalendarWidget(self.centralwidget)
        self.DateSelector.setObjectName("DateSelector")
        self.DateSelector.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        self.DateSelector.clicked.connect(SetDate)
        self.gridLayout.addWidget(self.DateSelector, 9, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Surname = QtWidgets.QLineEdit(self.centralwidget)
        self.Surname.setObjectName("Surname")
        self.gridLayout.addWidget(self.Surname, 1, 1, 1, 1)
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setReadOnly(False)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.GenerateButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateButton.setObjectName("GenerateButton")
        self.GenerateButton.clicked.connect(GenerateString)
        self.gridLayout.addWidget(self.GenerateButton, 10, 0, 1, 2)
        self.AmountOMoney = QtWidgets.QLineEdit(self.centralwidget)
        self.AmountOMoney.setObjectName("AmountOMoney")
        self.gridLayout.addWidget(self.AmountOMoney, 5, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.TimeHHMM = QtWidgets.QLineEdit(self.centralwidget)
        self.TimeHHMM.setObjectName("TimeHHMM")
        self.gridLayout.addWidget(self.TimeHHMM, 7, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setScaledContents(False)
        self.label_4.setIndent(-2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 2)
        self.LinkExport = QtWidgets.QLineEdit(self.centralwidget)
        self.LinkExport.setText("")
        self.LinkExport.setReadOnly(True)
        self.LinkExport.setObjectName("LinkExport")
        self.gridLayout.addWidget(self.LinkExport, 11, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 21))
        self.menubar.setObjectName("menubar")
        self.menuGenerator = QtWidgets.QMenu(self.menubar)
        self.menuGenerator.setObjectName("menuGenerator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGenerator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generator Linków Płatności"))
        self.label_2.setText(_translate("MainWindow", "Nazwisko"))
        self.label.setText(_translate("MainWindow", "Imie"))
        #  self.Surname.setText(_translate("MainWindow", "Nazwisko pacjenta"))
        #  self.Name.setText(_translate("MainWindow", "Imie pacjenta"))
        self.label_3.setText(_translate("MainWindow", "Kwota"))
        self.GenerateButton.setText(_translate("MainWindow", "Wygeneruj"))
        #  self.AmountOMoney.setText(_translate("MainWindow", "Kwota przedpłaty"))
        self.label_5.setText(_translate("MainWindow", "Godzina (GG:MM)"))
        #  self.TimeHHMM.setText(_translate("MainWindow", "Godzina rozpoczęcia wizyty"))
        self.label_4.setText(_translate("MainWindow", "Data"))
        #  self.lineEdit.setText(_translate("MainWindow", "Nazwa płatności"))
        self.label_6.setText(_translate("MainWindow", "Email klienta"))
        self.menuGenerator.setTitle(_translate("MainWindow", "Generator Linków"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
