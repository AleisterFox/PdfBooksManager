# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_book_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NewBookForm(object):
    def setupUi(self, newBookWindow):
        if not newBookWindow.objectName():
            newBookWindow.setObjectName(u"newBookWindow")
        newBookWindow.resize(405, 472)
        newBookWindow.setStyleSheet(u"QPushButton:hover \n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdef0;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        self.label = QLabel(newBookWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(newBookWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 100, 20))
        self.titleLineEdit = QLineEdit(newBookWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(newBookWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 100, 20))
        self.categoryLineEdit = QLineEdit(newBookWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.label_4 = QLabel(newBookWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 100, 20))
        self.pageQtySpinBox = QSpinBox(newBookWindow)
        self.pageQtySpinBox.setMaximum(2000)
        self.pageQtySpinBox.setObjectName(u"pageQtySpinBox")
        self.pageQtySpinBox.setGeometry(QRect(30, 180, 101, 22))
        self.label_5 = QLabel(newBookWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 210, 121, 20))
        self.filePathLineEdit = QLineEdit(newBookWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setEnabled(True)
        self.filePathLineEdit.setGeometry(QRect(30, 230, 191, 20))
        self.selectFileButton = QPushButton(newBookWindow)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(230, 228, 26, 26))
        self.selectFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"./assets/icons/select-file.icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectFileButton.setIcon(icon)
        self.selectFileButton.setIconSize(QSize(25, 25))
        self.selectFileButton.setFlat(True)
        self.label_6 = QLabel(newBookWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 260, 150, 20))
        self.descriptionTextEdit = QTextEdit(newBookWindow)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setGeometry(QRect(30, 280, 351, 111))
        self.addButton = QPushButton(newBookWindow)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(67, 410, 100, 31))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	height:2em;\n"
"	border-style:solid;\n"
"	border-width: 2px;\n"
"	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #0069c0;\n"
"	color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/add-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setFlat(True)
        self.cancelButton = QPushButton(newBookWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(243, 410, 101, 31))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	height:2em;\n"
"	border-style:solid;\n"
"	border-width: 2px;\n"
"	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: grey;\n"
"	color: white;\n"
"}\n"
"")
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setFlat(True)

        self.retranslateUi(newBookWindow)

        QMetaObject.connectSlotsByName(newBookWindow)
    # setupUi

    def retranslateUi(self, newBookWindow):
        newBookWindow.setWindowTitle(QCoreApplication.translate("newBookWindow", u"New Book", None))
        self.label.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NEW BOOK</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Book Title</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Category</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Pages Qty</span></p><p><br/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Select File</span></p></body></html>", None))
        self.selectFileButton.setText("")
        self.label_6.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Book Description</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("newBookWindow", u"ADD", None))
        self.cancelButton.setText(QCoreApplication.translate("newBookWindow", u"CANCEL", None))
    # retranslateUi

