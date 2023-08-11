# Form implementation generated from reading ui file 'superRPGGame_Main.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 312)
        Dialog.setMinimumSize(QtCore.QSize(517, 312))
        Dialog.setMaximumSize(QtCore.QSize(517, 312))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/fight.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:rgb(0, 0,0)")
        self.hearts1 = QtWidgets.QLabel(parent=Dialog)
        self.hearts1.setGeometry(QtCore.QRect(10, 10, 36, 36))
        self.hearts1.setText("")
        self.hearts1.setPixmap(QtGui.QPixmap("../assets/life.png"))
        self.hearts1.setScaledContents(True)
        self.hearts1.setObjectName("hearts1")
        self.hearts2 = QtWidgets.QLabel(parent=Dialog)
        self.hearts2.setGeometry(QtCore.QRect(50, 10, 36, 36))
        self.hearts2.setText("")
        self.hearts2.setPixmap(QtGui.QPixmap("../assets/life.png"))
        self.hearts2.setScaledContents(True)
        self.hearts2.setObjectName("hearts2")
        self.hearts3 = QtWidgets.QLabel(parent=Dialog)
        self.hearts3.setGeometry(QtCore.QRect(90, 10, 36, 36))
        self.hearts3.setText("")
        self.hearts3.setPixmap(QtGui.QPixmap("../assets/life.png"))
        self.hearts3.setScaledContents(True)
        self.hearts3.setObjectName("hearts3")
        self.hearts4 = QtWidgets.QLabel(parent=Dialog)
        self.hearts4.setGeometry(QtCore.QRect(130, 10, 36, 36))
        self.hearts4.setText("")
        self.hearts4.setPixmap(QtGui.QPixmap("../assets/life.png"))
        self.hearts4.setScaledContents(True)
        self.hearts4.setObjectName("hearts4")
        self.hearts5 = QtWidgets.QLabel(parent=Dialog)
        self.hearts5.setGeometry(QtCore.QRect(170, 10, 36, 36))
        self.hearts5.setText("")
        self.hearts5.setPixmap(QtGui.QPixmap("../assets/life.png"))
        self.hearts5.setScaledContents(True)
        self.hearts5.setObjectName("hearts5")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(403, 20, 101, 23))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.btn_start = QtWidgets.QPushButton(parent=Dialog)
        self.btn_start.setGeometry(QtCore.QRect(220, 20, 75, 23))
        self.btn_start.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.btn_start.setObjectName("btn_start")
        self.btn_pause = QtWidgets.QPushButton(parent=Dialog)
        self.btn_pause.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.btn_pause.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.btn_pause.setObjectName("btn_pause")
        self.label_info = QtWidgets.QLabel(parent=Dialog)
        self.label_info.setGeometry(QtCore.QRect(10, 60, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_info.setFont(font)
        self.label_info.setStyleSheet("color: white;")
        self.label_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.btn_hero1 = QtWidgets.QPushButton(parent=Dialog)
        self.btn_hero1.setGeometry(QtCore.QRect(20, 130, 120, 120))
        self.btn_hero1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/hero1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_hero1.setIcon(icon1)
        self.btn_hero1.setIconSize(QtCore.QSize(120, 120))
        self.btn_hero1.setCheckable(False)
        self.btn_hero1.setChecked(False)
        self.btn_hero1.setAutoRepeat(False)
        self.btn_hero1.setObjectName("btn_hero1")
        self.btn_hero2 = QtWidgets.QPushButton(parent=Dialog)
        self.btn_hero2.setEnabled(False)
        self.btn_hero2.setGeometry(QtCore.QRect(140, 130, 120, 120))
        self.btn_hero2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../assets/hero2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_hero2.setIcon(icon2)
        self.btn_hero2.setIconSize(QtCore.QSize(120, 120))
        self.btn_hero2.setCheckable(False)
        self.btn_hero2.setChecked(False)
        self.btn_hero2.setAutoRepeat(False)
        self.btn_hero2.setObjectName("btn_hero2")
        self.btn_hero3 = QtWidgets.QPushButton(parent=Dialog)
        self.btn_hero3.setEnabled(False)
        self.btn_hero3.setGeometry(QtCore.QRect(260, 130, 120, 120))
        self.btn_hero3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../assets/hero3.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_hero3.setIcon(icon3)
        self.btn_hero3.setIconSize(QtCore.QSize(120, 120))
        self.btn_hero3.setCheckable(False)
        self.btn_hero3.setChecked(False)
        self.btn_hero3.setAutoRepeat(False)
        self.btn_hero3.setObjectName("btn_hero3")
        self.btn_hero4 = QtWidgets.QPushButton(parent=Dialog)
        self.btn_hero4.setEnabled(False)
        self.btn_hero4.setGeometry(QtCore.QRect(390, 130, 120, 120))
        self.btn_hero4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../assets/hero4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_hero4.setIcon(icon4)
        self.btn_hero4.setIconSize(QtCore.QSize(120, 120))
        self.btn_hero4.setCheckable(False)
        self.btn_hero4.setChecked(False)
        self.btn_hero4.setAutoRepeat(False)
        self.btn_hero4.setObjectName("btn_hero4")
        self.label_heroInfo = QtWidgets.QLabel(parent=Dialog)
        self.label_heroInfo.setGeometry(QtCore.QRect(10, 260, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_heroInfo.setFont(font)
        self.label_heroInfo.setStyleSheet("color: white;")
        self.label_heroInfo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_heroInfo.setObjectName("label_heroInfo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Super RPG Game"))
        self.btn_start.setText(_translate("Dialog", "Старт"))
        self.btn_pause.setText(_translate("Dialog", "Пауза"))
        self.label_info.setText(_translate("Dialog", "Ініціалізація гри"))
        self.label_heroInfo.setText(_translate("Dialog", "Ваш клас: Воїн. Атака фізична - 30 Магічна - 0"))
