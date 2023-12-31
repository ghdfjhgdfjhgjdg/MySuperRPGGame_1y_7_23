# Form implementation generated from reading ui file 'shopgui.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_shop(object):
    def setupUi(self, Dialog_shop):
        Dialog_shop.setObjectName("Dialog_shop")
        Dialog_shop.resize(400, 300)
        Dialog_shop.setMinimumSize(QtCore.QSize(400, 300))
        Dialog_shop.setMaximumSize(QtCore.QSize(400, 300))
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
        Dialog_shop.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/fight.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog_shop.setWindowIcon(icon)
        Dialog_shop.setStyleSheet("background-color:rgb(0, 0,0)")
        self.btn_shopOK = QtWidgets.QPushButton(parent=Dialog_shop)
        self.btn_shopOK.setGeometry(QtCore.QRect(150, 250, 101, 41))
        self.btn_shopOK.setAutoFillBackground(False)
        self.btn_shopOK.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.btn_shopOK.setObjectName("btn_shopOK")
        self.label_welcome = QtWidgets.QLabel(parent=Dialog_shop)
        self.label_welcome.setGeometry(QtCore.QRect(20, 0, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_welcome.setFont(font)
        self.label_welcome.setAutoFillBackground(False)
        self.label_welcome.setStyleSheet("color: white;")
        self.label_welcome.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_welcome.setObjectName("label_welcome")
        self.btn_shopAtack = QtWidgets.QPushButton(parent=Dialog_shop)
        self.btn_shopAtack.setGeometry(QtCore.QRect(20, 70, 130, 130))
        self.btn_shopAtack.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/shop2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_shopAtack.setIcon(icon1)
        self.btn_shopAtack.setIconSize(QtCore.QSize(120, 120))
        self.btn_shopAtack.setCheckable(False)
        self.btn_shopAtack.setChecked(False)
        self.btn_shopAtack.setAutoRepeat(False)
        self.btn_shopAtack.setObjectName("btn_shopAtack")
        self.label_atackPrice = QtWidgets.QLabel(parent=Dialog_shop)
        self.label_atackPrice.setGeometry(QtCore.QRect(20, 210, 130, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_atackPrice.setFont(font)
        self.label_atackPrice.setAutoFillBackground(False)
        self.label_atackPrice.setStyleSheet("color: white;")
        self.label_atackPrice.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_atackPrice.setObjectName("label_atackPrice")
        self.btn_shopLife = QtWidgets.QPushButton(parent=Dialog_shop)
        self.btn_shopLife.setGeometry(QtCore.QRect(260, 70, 130, 130))
        self.btn_shopLife.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../assets/shop1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_shopLife.setIcon(icon2)
        self.btn_shopLife.setIconSize(QtCore.QSize(120, 120))
        self.btn_shopLife.setCheckable(False)
        self.btn_shopLife.setChecked(False)
        self.btn_shopLife.setAutoRepeat(False)
        self.btn_shopLife.setObjectName("btn_shopLife")
        self.label_lifePrice = QtWidgets.QLabel(parent=Dialog_shop)
        self.label_lifePrice.setGeometry(QtCore.QRect(260, 210, 130, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_lifePrice.setFont(font)
        self.label_lifePrice.setAutoFillBackground(False)
        self.label_lifePrice.setStyleSheet("color: white;")
        self.label_lifePrice.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_lifePrice.setObjectName("label_lifePrice")

        self.retranslateUi(Dialog_shop)
        QtCore.QMetaObject.connectSlotsByName(Dialog_shop)

    def retranslateUi(self, Dialog_shop):
        _translate = QtCore.QCoreApplication.translate
        Dialog_shop.setWindowTitle(_translate("Dialog_shop", "Магазин"))
        self.btn_shopOK.setText(_translate("Dialog_shop", "OK"))
        self.label_welcome.setText(_translate("Dialog_shop", "Ви потрапили у магазин"))
        self.label_atackPrice.setText(_translate("Dialog_shop", "2000"))
        self.label_lifePrice.setText(_translate("Dialog_shop", "1000"))
