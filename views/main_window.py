# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListBookForm(object):
    def setupUi(self, ListBookForm):
        if not ListBookForm.objectName():
            ListBookForm.setObjectName(u"ListBookForm")
        ListBookForm.resize(961, 560)
        ListBookForm.setMouseTracking(False)
        self.buttonsFrame = QFrame(ListBookForm)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(10, 10, 941, 91))
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.openBookButton = QPushButton(self.buttonsFrame)
        self.openBookButton.setObjectName(u"openBookButton")
        self.openBookButton.setGeometry(QRect(20, 10, 71, 51))
        self.openBookButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.openBookButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style:solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/icons/open-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openBookButton.setIcon(icon)
        self.openBookButton.setIconSize(QSize(50, 50))
        self.openBookButton.setFlat(True)
        self.label = QLabel(self.buttonsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 91, 21))
        self.openBookButton_2 = QPushButton(self.buttonsFrame)
        self.openBookButton_2.setObjectName(u"openBookButton_2")
        self.openBookButton_2.setGeometry(QRect(110, 10, 71, 51))
        self.openBookButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.openBookButton_2.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style:solid;\n"
"	background-color:#bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#0069c0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/add-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openBookButton_2.setIcon(icon1)
        self.openBookButton_2.setIconSize(QSize(50, 50))
        self.openBookButton_2.setFlat(True)
        self.label_2 = QLabel(self.buttonsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 60, 91, 21))
        self.openEditButton = QPushButton(self.buttonsFrame)
        self.openEditButton.setObjectName(u"openEditButton")
        self.openEditButton.setGeometry(QRect(200, 10, 71, 51))
        self.openEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.openEditButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style:solid;\n"
"	background-color:#bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#0069c0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/edit-book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openEditButton.setIcon(icon2)
        self.openEditButton.setIconSize(QSize(50, 50))
        self.openEditButton.setFlat(True)
        self.label_3 = QLabel(self.buttonsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 60, 91, 21))
        self.label_4 = QLabel(self.buttonsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 60, 91, 21))
        self.deleteBookButton = QPushButton(self.buttonsFrame)
        self.deleteBookButton.setObjectName(u"deleteBookButton")
        self.deleteBookButton.setGeometry(QRect(290, 10, 71, 51))
        self.deleteBookButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteBookButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style:solid;\n"
"	background-color:#bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#0069c0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/delete-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteBookButton.setIcon(icon3)
        self.deleteBookButton.setIconSize(QSize(50, 50))
        self.deleteBookButton.setFlat(True)
        self.frame = QFrame(ListBookForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 941, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 71, 20))
        self.searchByComboBox = QComboBox(self.frame)
        self.searchByComboBox.setObjectName(u"searchByComboBox")
        self.searchByComboBox.setGeometry(QRect(90, 10, 161, 22))
        self.parameterLineEdit = QLineEdit(self.frame)
        self.parameterLineEdit.setObjectName(u"parameterLineEdit")
        self.parameterLineEdit.setGeometry(QRect(260, 10, 411, 20))
        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(680, 10, 120, 25))
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.refreshButton = QPushButton(self.frame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(810, 10, 120, 25))
        self.refreshButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon5)
        self.listBooksTable = QTableWidget(ListBookForm)
        self.listBooksTable.setObjectName(u"listBooksTable")
        self.listBooksTable.setGeometry(QRect(10, 160, 941, 341))
        self.qtyLabel = QLabel(ListBookForm)
        self.qtyLabel.setObjectName(u"qtyLabel")
        self.qtyLabel.setGeometry(QRect(10, 520, 87, 20))
        self.booksQtyLabel = QLabel(ListBookForm)
        self.booksQtyLabel.setObjectName(u"booksQtyLabel")
        self.booksQtyLabel.setGeometry(QRect(100, 520, 100, 20))

        self.retranslateUi(ListBookForm)

        QMetaObject.connectSlotsByName(ListBookForm)
    # setupUi

    def retranslateUi(self, ListBookForm):
        ListBookForm.setWindowTitle(QCoreApplication.translate("ListBookForm", u"Book List", None))
        self.openBookButton.setText("")
        self.label.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\">Open Book</p></body></html>", None))
        self.openBookButton_2.setText("")
        self.label_2.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\">New Book</p></body></html>", None))
        self.openEditButton.setText("")
        self.label_3.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\">Edit Book</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\">Delete Book</p></body></html>", None))
        self.deleteBookButton.setText("")
        self.label_5.setText(QCoreApplication.translate("ListBookForm", u"Search by:", None))
        self.searchButton.setText(QCoreApplication.translate("ListBookForm", u"Search", None))
        self.refreshButton.setText(QCoreApplication.translate("ListBookForm", u"Refresh", None))
        self.qtyLabel.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Books Qty: </span></p></body></html>", None))
        self.booksQtyLabel.setText(QCoreApplication.translate("ListBookForm", u"#", None))
    # retranslateUi

