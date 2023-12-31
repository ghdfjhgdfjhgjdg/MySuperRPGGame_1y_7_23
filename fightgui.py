# Form implementation generated from reading ui file 'fightgui.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_fight(object):
    def setupUi(self, Dialog_fight):
        Dialog_fight.setObjectName("Dialog_fight")
        Dialog_fight.resize(400, 389)
        Dialog_fight.setMinimumSize(QtCore.QSize(400, 389))
        Dialog_fight.setMaximumSize(QtCore.QSize(400, 389))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        Dialog_fight.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/fight.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_fight.setWindowIcon(icon)
        Dialog_fight.setStyleSheet("background-color:rgb(0, 0,0)")
        self.btn_fightOK = QtWidgets.QPushButton(parent=Dialog_fight)
        self.btn_fightOK.setEnabled(False)
        self.btn_fightOK.setGeometry(QtCore.QRect(150, 340, 101, 41))
        self.btn_fightOK.setAutoFillBackground(False)
        self.btn_fightOK.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.btn_fightOK.setObjectName("btn_fightOK")
        self.label_welcome1 = QtWidgets.QLabel(parent=Dialog_fight)
        self.label_welcome1.setGeometry(QtCore.QRect(20, 10, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_welcome1.setFont(font)
        self.label_welcome1.setAutoFillBackground(False)
        self.label_welcome1.setStyleSheet("color: white;")
        self.label_welcome1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_welcome1.setObjectName("label_welcome1")
        self.label_info_battle1 = QtWidgets.QLabel(parent=Dialog_fight)
        self.label_info_battle1.setGeometry(QtCore.QRect(20, 220, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_info_battle1.setFont(font)
        self.label_info_battle1.setAutoFillBackground(False)
        self.label_info_battle1.setStyleSheet("color: white;")
        self.label_info_battle1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_battle1.setObjectName("label_info_battle1")
        self.btn_fight = QtWidgets.QPushButton(parent=Dialog_fight)
        self.btn_fight.setGeometry(QtCore.QRect(30, 60, 120, 120))
        self.btn_fight.setText("")
        self.btn_fight.setIcon(icon)
        self.btn_fight.setIconSize(QtCore.QSize(120, 120))
        self.btn_fight.setCheckable(False)
        self.btn_fight.setChecked(False)
        self.btn_fight.setAutoRepeat(False)
        self.btn_fight.setObjectName("btn_fight")
        self.btn_run = QtWidgets.QPushButton(parent=Dialog_fight)
        self.btn_run.setGeometry(QtCore.QRect(260, 60, 120, 120))
        self.btn_run.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/run.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_run.setIcon(icon1)
        self.btn_run.setIconSize(QtCore.QSize(120, 120))
        self.btn_run.setCheckable(False)
        self.btn_run.setChecked(False)
        self.btn_run.setAutoRepeat(False)
        self.btn_run.setObjectName("btn_run")
        self.label1 = QtWidgets.QLabel(parent=Dialog_fight)
        self.label1.setGeometry(QtCore.QRect(260, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(False)
        self.label1.setStyleSheet("color: white;")
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(parent=Dialog_fight)
        self.label2.setGeometry(QtCore.QRect(30, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setAutoFillBackground(False)
        self.label2.setStyleSheet("color: white;")
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.label_info_battle2 = QtWidgets.QLabel(parent=Dialog_fight)
        self.label_info_battle2.setGeometry(QtCore.QRect(20, 260, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_info_battle2.setFont(font)
        self.label_info_battle2.setAutoFillBackground(False)
        self.label_info_battle2.setStyleSheet("color: white;")
        self.label_info_battle2.setText("")
        self.label_info_battle2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_battle2.setObjectName("label_info_battle2")
        self.label_info_battle3 = QtWidgets.QLabel(parent=Dialog_fight)
        self.label_info_battle3.setGeometry(QtCore.QRect(20, 300, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_info_battle3.setFont(font)
        self.label_info_battle3.setAutoFillBackground(False)
        self.label_info_battle3.setStyleSheet("color: white;")
        self.label_info_battle3.setText("")
        self.label_info_battle3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info_battle3.setObjectName("label_info_battle3")

        self.retranslateUi(Dialog_fight)
        QtCore.QMetaObject.connectSlotsByName(Dialog_fight)

    def retranslateUi(self, Dialog_fight):
        _translate = QtCore.QCoreApplication.translate
        Dialog_fight.setWindowTitle(_translate("Dialog_fight", "Битва"))
        self.btn_fightOK.setText(_translate("Dialog_fight", "OK"))
        self.label_welcome1.setText(_translate("Dialog_fight", "Ви зустріли ворога"))
        self.label_info_battle1.setText(_translate("Dialog_fight", "Ініціалізація"))
        self.label1.setText(_translate("Dialog_fight", "Втекти"))
        self.label2.setText(_translate("Dialog_fight", "Битися"))
