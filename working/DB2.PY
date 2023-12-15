# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newestySJScQ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys,re
import functools
from PyQt5.QtGui import QIntValidator
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QIntValidator,QValidator,
    QValidator,QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
# from PyQt6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
#     QHBoxLayout, QHeaderView, QLabel, QLineEdit,QDialog,QDialogButtonBox,
#     QMainWindow, QPushButton, QSizePolicy, QSlider,QFormLayout,
#     QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
#     QToolBox, QVBoxLayout, QWidget)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,QDialog,QDialogButtonBox,
    QMainWindow, QPushButton, QSizePolicy, QSlider,QFormLayout,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
# import game1 
import sqlite3
# from game1 import run_game
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        super().__init__()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1248, 656)
        MainWindow.setStyleSheet(u"\n"
"QTabBar:tab:selected{\n"
"background-color:rgb(250, 113, 108);\n"
"color:white;\n"
"color:rgb(172, 0, 0);\n"
"text-aligen:center;\n"
"\n"
"}\n"
"QTabBar:tab:hover{\n"
"background-color:rgb(250, 113, 108);\n"
"color:white;\n"
"text-aligen:center;\n"
"}\n"
"\n"
"QTabBar:tab{\n"
"height: 40px;\n"
"color:red;\n"
"border:none;\n"
"margin-left:13px;\n"
"font-size:20px;\n"
"width:153px;\n"
"margin-bottom:40px;\n"
"margin-top:10px;\n"
"}\n"
"\n"
"Widget_4{\n"
"background-color:rgb(255, 192, 193);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(180, 0))
        self.widget.setMaximumSize(QSize(200, 16777212))
        self.widget.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(210, 71))
        self.widget_3.setMaximumSize(QSize(235, 110))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 10, 191, 71))
        font = QFont()
        self.label.setFont(font)
        self.label.setStyleSheet(u"  color:rgb(203, 0, 0);\n"
"font-size:60px;")

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet(u"background-color:rgb(255, 192, 193);")

        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 20))
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none;")

        self.verticalLayout_2.addWidget(self.widget_5)

        self.Game = QTabWidget(self.widget_2)
        self.Game.setObjectName(u"Game")
        self.Game.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"")
        self.Patient = QTabWidget()
        
        self.Patient.setObjectName(u" Patient")
        self.Patient.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.Patient)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_8 = QWidget(self.Patient)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 300))
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(500, 0))
        self.widget_10.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_10)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(150, 50))
        self.widget_9.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.Search_label = QLabel(self.widget_9)
        self.Search_label.setObjectName(u"Search_label")
        self.Search_label.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_15.addWidget(self.Search_label)

        self.comboBox = QComboBox(self.widget_9)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(30, 0))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height:30px;")

        self.horizontalLayout_15.addWidget(self.comboBox)


        self.horizontalLayout_2.addWidget(self.widget_9)

        self.Search_lineEdit = QLineEdit(self.widget_10)
        self.Search_lineEdit.setObjectName(u"Search_lineEdit")
        self.Search_lineEdit.setMinimumSize(QSize(350, 0))
        self.Search_lineEdit.setMaximumSize(QSize(550, 50))
        self.Search_lineEdit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"\n"
"color:red;\n"
"margin-right:20px;\n"
"\n"
"\n"
"height:30px;\n"
"border-radius:20px;")

        self.horizontalLayout_2.addWidget(self.Search_lineEdit)

        self.search_btn = QPushButton(self.widget_10)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.clicked.connect(self.search_users)
        self.search_btn.setMinimumSize(QSize(40, 0))
        self.search_btn.setMaximumSize(QSize(90, 16777215))
        self.search_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height:25px;\n"
"margin-right:7px;\n"
"margin-left:7px;\n"
"")

        self.horizontalLayout_2.addWidget(self.search_btn)

        self.refresh_btn = QPushButton(self.widget_10)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.clicked.connect(self.load_users)
        self.refresh_btn.setMinimumSize(QSize(40, 0))
        self.refresh_btn.setMaximumSize(QSize(90, 16777215))
        self.refresh_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height:25px;\n"
"margin-right:7px;")

        self.horizontalLayout_2.addWidget(self.refresh_btn)

        self.demo_btn = QPushButton(self.widget_10)
        self.demo_btn.setObjectName(u"demo_btn")
        
        self.demo_btn.setMinimumSize(QSize(50, 30))
        self.demo_btn.setMaximumSize(QSize(90, 50))
        self.demo_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin-right:7px;\n"
"border-radius:15px;\n"
"color:red;")

        self.horizontalLayout_2.addWidget(self.demo_btn)

        self.AddUser_btn = QPushButton(self.widget_10)
        self.AddUser_btn.setObjectName(u"AddUser_btn")
        self.AddUser_btn.setMinimumSize(QSize(30, 15))
        self.AddUser_btn.setMaximumSize(QSize(60, 50))
        self.AddUser_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.AddUser_btn.clicked.connect(self.add_user) 
        self.horizontalLayout_2.addWidget(self.AddUser_btn)
########################
        self.selected_user_label = QLabel("Selected User: N/A")
        self.verticalLayout_3.addWidget(self.selected_user_label)
  ##########################      
        self.verticalLayout_4.addWidget(self.widget_10)
        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.Patient)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout = QGridLayout(self.widget_7)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(1020, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.table = QTableWidget(self.frame_2)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.table.rowCount() < 4):
            self.table.setRowCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, __qtablewidgetitem9)
        self.table.setObjectName(u"table")
        # self.table.setHorizontalHeaderLabels(['ID','Name', 'Address', 'Details', 'Phone Number'])

        self.gridLayout_2.addWidget(self.table, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.Game.addTab(self.Patient, "")
        self.Exercise = QWidget()
        self.Exercise.setObjectName(u"Exercise")
        self.Exercise.setStyleSheet(u"background-color:rgb(255, 192, 193);")
        self.gridLayout_3 = QGridLayout(self.Exercise)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_6 = QWidget(self.Exercise)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_13 = QWidget(self.widget_6)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 25))
        ###########
        
        self.Category_label = QLabel("Your Category: N/A Your Game: N/A", self.widget_13)
        self.gridLayout_4.addWidget(self.Category_label)
        self.gridLayout_4.addWidget(self.widget_13)
        ###########
        
        self.gridLayout_4.addWidget(self.widget_13, 0, 0, 1, 1)
        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(180, 0))

        self.gridLayout_4.addWidget(self.widget_11, 0, 1, 3, 1)

        self.toolBox = QToolBox(self.widget_6)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:20px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_4 = QHBoxLayout(self.page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_12 = QWidget(self.page)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.widget_12)
        # self.pushButton_5.clicked.connect(lambda: self.updateLabel("Neck", "Snake Game"))
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(16777215, 369))
        self.pushButton_5.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.widget_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(16777215, 369))
        self.pushButton_4.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.widget_12)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 369))
        self.pushButton_3.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addWidget(self.widget_12)

        self.toolBox.addItem(self.page, u"Neck")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_6 = QHBoxLayout(self.page_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_15 = QWidget(self.page_3)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_6 = QPushButton(self.widget_15)
        self.pushButton_6.clicked.connect(lambda: self.updateLabel("Neck", "Snake Game")) 
        self.pushButton_6.setMaximumSize(QSize(16777215, 369))
        #  stylesheet 
        self.pushButton_6.setStyleSheet(f"QPushButton {{ background-image: url(cutsnake.jpg) ; background-position: center; background-repeat: no-repeat; background-size: cover;}}")
        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_15)
        self.pushButton_7.clicked.connect(lambda: self.updateLabel("Neck", "Flappy Bird")) 
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(16777215, 369))
        self.pushButton_7.setStyleSheet(f"QPushButton {{ background-image: url(flappyBird.jpg) ; background-position: center; background-repeat: no-repeat; background-size: cover;}};background-color:rgb(255, 192, 193);"
"border-radius:10px;")

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.widget_15)
        self.pushButton_8.clicked.connect(lambda: self.updateLabel("Neck", "Angry Bird")) 
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(16777215, 369))
        self.pushButton_8.setStyleSheet(f"QPushButton {{ background-image: url(AngryBird.png) ; background-position: center; background-repeat: no-repeat; background-size: cover;}};background-color:rgb(255, 192, 193);"
"border-radius:10px;")

        self.horizontalLayout_5.addWidget(self.pushButton_8)


        self.horizontalLayout_6.addWidget(self.widget_15)

        self.toolBox.addItem(self.page_3, u"Knee")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_8 = QHBoxLayout(self.page_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_16 = QWidget(self.page_4)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_9 = QPushButton(self.widget_16)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(16777215, 369))
        self.pushButton_9.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_16)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(16777215, 369))
        self.pushButton_10.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_7.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget_16)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(16777215, 369))
        self.pushButton_11.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_7.addWidget(self.pushButton_11)


        self.horizontalLayout_8.addWidget(self.widget_16)

        self.toolBox.addItem(self.page_4, u"Spine")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_10 = QHBoxLayout(self.page_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_17 = QWidget(self.page_5)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_12 = QPushButton(self.widget_17)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(16777215, 369))
        self.pushButton_12.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_9.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.widget_17)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(16777215, 369))
        self.pushButton_13.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_9.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_17)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(16777215, 369))
        self.pushButton_14.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_9.addWidget(self.pushButton_14)


        self.horizontalLayout_10.addWidget(self.widget_17)

        self.toolBox.addItem(self.page_5, u"Waist")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_12 = QHBoxLayout(self.page_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_18 = QWidget(self.page_2)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_15 = QPushButton(self.widget_18)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMaximumSize(QSize(16777215, 369))
        self.pushButton_15.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_11.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.widget_18)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMaximumSize(QSize(16777215, 369))
        self.pushButton_16.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_11.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.widget_18)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMaximumSize(QSize(16777215, 369))
        self.pushButton_17.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_11.addWidget(self.pushButton_17)


        self.horizontalLayout_12.addWidget(self.widget_18)

        self.toolBox.addItem(self.page_2, u"Hip")

        self.gridLayout_4.addWidget(self.toolBox, 1, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_6)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.widget_14, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_6, 1, 0, 1, 1)

        self.Game.addTab(self.Exercise, "")
        self.Game_2 = QWidget()
        self.Game_2.setObjectName(u"Game_2")
        self.Game_2.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"\n"
"")
        self.gridLayout_5 = QGridLayout(self.Game_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_19 = QWidget(self.Game_2)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setStyleSheet(u"margin-top:30px;\n"
"margin-right:60px;\n"
"margin-bottom:15px;")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.widget_19)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMaximumSize(QSize(16777215, 369))
        self.pushButton_18.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_13.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.widget_19)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMaximumSize(QSize(16777215, 404))
        self.pushButton_19.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_13.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.widget_19)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMaximumSize(QSize(16777215, 369))
        self.pushButton_20.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_13.addWidget(self.pushButton_20)


        self.gridLayout_5.addWidget(self.widget_19, 0, 0, 1, 1)

        self.widget_20 = QWidget(self.Game_2)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setStyleSheet(u"margin-top:15px;\n"
"margin-right:60px;\n"
"margin-bottom:30px;")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_21 = QPushButton(self.widget_20)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMaximumSize(QSize(16777215, 369))
        self.pushButton_21.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_14.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.widget_20)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMaximumSize(QSize(16777215, 369))
        self.pushButton_22.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_14.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.widget_20)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMaximumSize(QSize(16777215, 369))
        self.pushButton_23.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_14.addWidget(self.pushButton_23)


        self.gridLayout_5.addWidget(self.widget_20, 1, 0, 1, 1)

        self.Game.addTab(self.Game_2, "")
        self.Goal = QWidget()
        self.Goal.setObjectName(u"Goal")
        self.Goal.setStyleSheet(u"background-color:rgb(255, 192, 193);")
        self.gridLayout_6 = QGridLayout(self.Goal)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSlider_4 = QSlider(self.Goal)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setMinimumSize(QSize(0, 20))
        self.horizontalSlider_4.setMaximumSize(QSize(350, 60))
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_4, 1, 2, 1, 1)

        self.horizontalSlider_2 = QSlider(self.Goal)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMinimumSize(QSize(0, 20))
        self.horizontalSlider_2.setMaximumSize(QSize(350, 60))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_2, 0, 2, 1, 1)

        self.horizontalSlider = QSlider(self.Goal)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(0, 20))
        self.horizontalSlider.setMaximumSize(QSize(350, 60))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider, 0, 1, 1, 1)

        self.horizontalSlider_3 = QSlider(self.Goal)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setMinimumSize(QSize(0, 20))
        self.horizontalSlider_3.setMaximumSize(QSize(350, 60))
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_3, 1, 1, 1, 1)

        self.Game.addTab(self.Goal, "")
        self.Setup = QWidget()
        self.Setup.setObjectName(u"Setup")
        self.Setup.setStyleSheet(u"background-color:rgb(255, 192, 193);")
        self.gridLayout_7 = QGridLayout(self.Setup)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, -1, 0, 0)
        self.widget_21 = QWidget(self.Setup)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_7 = QVBoxLayout(self.widget_21)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_39 = QWidget(self.widget_21)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_41 = QWidget(self.widget_39)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setStyleSheet(u"margin-top:15px;\n"
"margin-right:60px;\n"
"margin-bottom:30px;")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.pushButton_50 = QPushButton(self.widget_41)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMaximumSize(QSize(16777215, 369))
        self.pushButton_50.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_29.addWidget(self.pushButton_50)

        self.pushButton_51 = QPushButton(self.widget_41)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMaximumSize(QSize(16777215, 369))
        self.pushButton_51.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_29.addWidget(self.pushButton_51)

        self.pushButton_52 = QPushButton(self.widget_41)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setMaximumSize(QSize(16777215, 369))
        self.pushButton_52.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_29.addWidget(self.pushButton_52)


        self.horizontalLayout_31.addWidget(self.widget_41)


        self.verticalLayout_7.addWidget(self.widget_39)

        self.widget_38 = QWidget(self.widget_21)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_40 = QWidget(self.widget_38)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setStyleSheet(u"margin-top:15px;\n"
"margin-right:60px;\n"
"margin-bottom:30px;")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.pushButton_47 = QPushButton(self.widget_40)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMaximumSize(QSize(16777215, 369))
        self.pushButton_47.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_28.addWidget(self.pushButton_47)

        self.pushButton_48 = QPushButton(self.widget_40)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMaximumSize(QSize(16777215, 369))
        self.pushButton_48.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_28.addWidget(self.pushButton_48)

        self.pushButton_49 = QPushButton(self.widget_40)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMaximumSize(QSize(16777215, 369))
        self.pushButton_49.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_28.addWidget(self.pushButton_49)


        self.horizontalLayout_32.addWidget(self.widget_40)


        self.verticalLayout_7.addWidget(self.widget_38)


        self.gridLayout_7.addWidget(self.widget_21, 0, 0, 1, 1)

        self.Game.addTab(self.Setup, "")
        self.Play = QWidget()
        self.Play.setObjectName(u"Play")
        self.Play.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"")
        self.gridLayout_15 = QGridLayout(self.Play)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.widget_42 = QWidget(self.Play)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_8 = QVBoxLayout(self.widget_42)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_43 = QWidget(self.widget_42)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.pushButton_58 = QPushButton(self.widget_43)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setMaximumSize(QSize(16777215, 369))
        self.pushButton_58.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_33.addWidget(self.pushButton_58)

        self.pushButton_56 = QPushButton(self.widget_43)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setMaximumSize(QSize(16777215, 369))
        self.pushButton_56.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_33.addWidget(self.pushButton_56)

        self.pushButton_57 = QPushButton(self.widget_43)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setMaximumSize(QSize(16777215, 369))
        self.pushButton_57.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_33.addWidget(self.pushButton_57)


        self.verticalLayout_8.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.widget_42)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.pushButton_60 = QPushButton(self.widget_44)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setMaximumSize(QSize(16777215, 369))
        self.pushButton_60.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_34.addWidget(self.pushButton_60)

        self.pushButton_59 = QPushButton(self.widget_44)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setMaximumSize(QSize(16777215, 369))
        self.pushButton_59.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_34.addWidget(self.pushButton_59)

        self.pushButton_61 = QPushButton(self.widget_44)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setMaximumSize(QSize(16777215, 369))
        self.pushButton_61.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;")

        self.horizontalLayout_34.addWidget(self.pushButton_61)


        self.verticalLayout_8.addWidget(self.widget_44)


        self.gridLayout_15.addWidget(self.widget_42, 0, 0, 1, 1)

        self.Game.addTab(self.Play, "")
        self.Assignment = QWidget()
        self.Assignment.setObjectName(u"Assignment")
        sizePolicy1.setHeightForWidth(self.Assignment.sizePolicy().hasHeightForWidth())
        self.Assignment.setSizePolicy(sizePolicy1)
        self.Assignment.setStyleSheet(u"background-color:rgb(255, 192, 193);")
        self.gridLayout_16 = QGridLayout(self.Assignment)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.widget_45 = QWidget(self.Assignment)
        self.widget_45.setObjectName(u"widget_45")
        self.gridLayout_17 = QGridLayout(self.widget_45)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.widget_46 = QWidget(self.widget_45)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMinimumSize(QSize(0, 25))

        self.gridLayout_17.addWidget(self.widget_46, 0, 0, 1, 1)

        self.toolBox_3 = QToolBox(self.widget_45)
        self.toolBox_3.setObjectName(u"toolBox_3")
        self.toolBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:20px;")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.page_11.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_35 = QHBoxLayout(self.page_11)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.widget_49 = QWidget(self.page_11)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pushButton_62 = QPushButton(self.widget_49)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setMaximumSize(QSize(16777215, 369))
        self.pushButton_62.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_36.addWidget(self.pushButton_62)

        self.pushButton_63 = QPushButton(self.widget_49)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setMaximumSize(QSize(16777215, 369))
        self.pushButton_63.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_36.addWidget(self.pushButton_63)

        self.pushButton_64 = QPushButton(self.widget_49)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setMaximumSize(QSize(16777215, 369))
        self.pushButton_64.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_36.addWidget(self.pushButton_64)


        self.horizontalLayout_35.addWidget(self.widget_49)

        self.toolBox_3.addItem(self.page_11, u"9-9-23")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.page_12.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_37 = QHBoxLayout(self.page_12)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.widget_50 = QWidget(self.page_12)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pushButton_65 = QPushButton(self.widget_50)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setMaximumSize(QSize(16777215, 369))
        self.pushButton_65.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_38.addWidget(self.pushButton_65)

        self.pushButton_66 = QPushButton(self.widget_50)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setMaximumSize(QSize(16777215, 369))
        self.pushButton_66.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_38.addWidget(self.pushButton_66)

        self.pushButton_67 = QPushButton(self.widget_50)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMaximumSize(QSize(16777215, 369))
        self.pushButton_67.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_38.addWidget(self.pushButton_67)


        self.horizontalLayout_37.addWidget(self.widget_50)

        self.toolBox_3.addItem(self.page_12, u"10-9-23")
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.page_13.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_39 = QHBoxLayout(self.page_13)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.widget_51 = QWidget(self.page_13)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.pushButton_68 = QPushButton(self.widget_51)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setMaximumSize(QSize(16777215, 369))
        self.pushButton_68.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_40.addWidget(self.pushButton_68)

        self.pushButton_69 = QPushButton(self.widget_51)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setMaximumSize(QSize(16777215, 369))
        self.pushButton_69.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_40.addWidget(self.pushButton_69)

        self.pushButton_70 = QPushButton(self.widget_51)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setMaximumSize(QSize(16777215, 369))
        self.pushButton_70.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_40.addWidget(self.pushButton_70)


        self.horizontalLayout_39.addWidget(self.widget_51)

        self.toolBox_3.addItem(self.page_13, u"11-9-23")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.page_14.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_41 = QHBoxLayout(self.page_14)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.widget_52 = QWidget(self.page_14)
        self.widget_52.setObjectName(u"widget_52")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.pushButton_71 = QPushButton(self.widget_52)
        self.pushButton_71.setObjectName(u"pushButton_71")
        self.pushButton_71.setMaximumSize(QSize(16777215, 369))
        self.pushButton_71.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_42.addWidget(self.pushButton_71)

        self.pushButton_72 = QPushButton(self.widget_52)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setMaximumSize(QSize(16777215, 369))
        self.pushButton_72.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_42.addWidget(self.pushButton_72)

        self.pushButton_73 = QPushButton(self.widget_52)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setMaximumSize(QSize(16777215, 369))
        self.pushButton_73.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_42.addWidget(self.pushButton_73)


        self.horizontalLayout_41.addWidget(self.widget_52)

        self.toolBox_3.addItem(self.page_14, u"13-9-23")
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.page_15.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_43 = QHBoxLayout(self.page_15)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.widget_53 = QWidget(self.page_15)
        self.widget_53.setObjectName(u"widget_53")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.pushButton_74 = QPushButton(self.widget_53)
        self.pushButton_74.setObjectName(u"pushButton_74")
        self.pushButton_74.setMaximumSize(QSize(16777215, 369))
        self.pushButton_74.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_44.addWidget(self.pushButton_74)

        self.pushButton_75 = QPushButton(self.widget_53)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setMaximumSize(QSize(16777215, 369))
        self.pushButton_75.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_44.addWidget(self.pushButton_75)

        self.pushButton_76 = QPushButton(self.widget_53)
        self.pushButton_76.setObjectName(u"pushButton_76")
        self.pushButton_76.setMaximumSize(QSize(16777215, 369))
        self.pushButton_76.setStyleSheet(u"background-color:rgb(255, 192, 193);\n"
"border-radius:10px;")

        self.horizontalLayout_44.addWidget(self.pushButton_76)


        self.horizontalLayout_43.addWidget(self.widget_53)

        self.toolBox_3.addItem(self.page_15, u"13-9-23")

        self.gridLayout_17.addWidget(self.toolBox_3, 1, 0, 1, 1)

        self.widget_48 = QWidget(self.widget_45)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(180, 0))

        self.gridLayout_17.addWidget(self.widget_48, 1, 1, 1, 1)

        self.widget_47 = QWidget(self.widget_45)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setMinimumSize(QSize(0, 40))

        self.gridLayout_17.addWidget(self.widget_47, 2, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_45, 0, 0, 1, 1)

        self.Game.addTab(self.Assignment, "")

        self.verticalLayout_2.addWidget(self.Game)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Game.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.toolBox_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" Better.", None))
        self.Search_label.setText(QCoreApplication.translate("MainWindow", u"Search..", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Phone no", None))

        self.Search_lineEdit.setText("")
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.demo_btn.setText(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.AddUser_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Details", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Phone no", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.Game.setTabText(self.Game.indexOf(self.Patient), QCoreApplication.translate("MainWindow", u"Patient", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Neck", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Snake Game", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Flappy Bird", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Angry Bird", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Knee", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Spine", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Waist", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Hip", None))
        self.Game.setTabText(self.Game.indexOf(self.Exercise), QCoreApplication.translate("MainWindow", u"Exercise", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Game.setTabText(self.Game.indexOf(self.Game_2), QCoreApplication.translate("MainWindow", u"Game", None))
        self.Game.setTabText(self.Game.indexOf(self.Goal), QCoreApplication.translate("MainWindow", u"Goal ", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Game.setTabText(self.Game.indexOf(self.Setup), QCoreApplication.translate("MainWindow", u"Setup", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Game.setTabText(self.Game.indexOf(self.Play), QCoreApplication.translate("MainWindow", u"Play", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_63.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_11), QCoreApplication.translate("MainWindow", u"9-9-23", None))
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_67.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_12), QCoreApplication.translate("MainWindow", u"10-9-23", None))
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_69.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_13), QCoreApplication.translate("MainWindow", u"11-9-23", None))
        self.pushButton_71.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_72.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_73.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_14), QCoreApplication.translate("MainWindow", u"13-9-23", None))
        self.pushButton_74.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_75.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_76.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_15), QCoreApplication.translate("MainWindow", u"13-9-23", None))
        self.Game.setTabText(self.Game.indexOf(self.Assignment), QCoreApplication.translate("MainWindow", u"Assignment", None))
        
        self.conn = sqlite3.connect('user09.db')
        self.create_table()
        self.load_users() 
    # retranslateUi
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                address TEXT,
                details TEXT,
                phone_number INT
            )
        ''')
        self.conn.commit()

    def load_users(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Patients')
        data = cursor.fetchall()

        self.table.setRowCount(0)
        for row,user in enumerate(data):
            user_name = user[1]
            self.table.insertRow(row)
            for col, value in enumerate(user):
                

                
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, col, item)

            
        
            edit_button = QPushButton("Edit")           
            delete_button = QPushButton("Delete")
            edit_button.clicked.connect(functools.partial(self.edit_user, row))
            delete_button.clicked.connect(functools.partial(self.delete_user, row))
        
            select_button = QPushButton("Select")
            select_button.clicked.connect(functools.partial(self.onSelectButtonClicked, user_name))
             


            button_layout = QHBoxLayout()
            button_layout.addWidget(edit_button)
            button_layout.addWidget(delete_button)
            button_layout.addWidget(select_button)
            button_widget = QWidget()
            button_widget.setLayout(button_layout)
            self.table.setCellWidget(row, 5, button_widget)
            
    def onSelectButtonClicked(self, user_name):
        self.updateTabName(user_name)  

    def updateTabName(self, new_tab_name):
        current_index = self.Game.currentIndex()
        self.Game.setTabText(current_index, "Patient:"+str(new_tab_name))
        selected_tab_stylesheet = (
            "QTabBar::tab:selected {"
            
            "    font-size:15px"
            "}"
        )
        
        self.Game.setStyleSheet(selected_tab_stylesheet)
        self.selected_user_label.setText(f"Selected User: {new_tab_name} >>") 
#         self.selected_user_name(new_tab_name)
#     def selected_user_name(self,new_tab_name2): 
#         self.Patient.setTabText(new_tab_name2)        
    
    
    def search_users(self):
        cursor = self.conn.cursor()

        # Determine the search option from the combo box
        search_option = self.comboBox.currentText()
        search_text = self.Search_lineEdit.text()

        if search_option == "Name":
            cursor.execute('SELECT * FROM Patients WHERE name LIKE ?', ('%' + search_text + '%',))
        elif search_option == "Phone no":
            cursor.execute('SELECT * FROM Patients WHERE phone_number LIKE ?', ('%' + search_text + '%',))

        data = cursor.fetchall()
        # user_name = self.table.item(row, 1).text()

        self.table.setRowCount(0)
        for row, user in enumerate(data):
            self.table.insertRow(row)
            for col, value in enumerate(user):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, col, item)
            user_name = self.table.item(row, 1).text()
            # Add buttons for actions (Edit and Delete)
            edit_button = QPushButton("Edit")
            delete_button = QPushButton("Delete")
            Select_button = QPushButton("Select")
            edit_button.clicked.connect(lambda _ , r=row: self.edit_user(r))  # Lambda for Edit
            delete_button.clicked.connect(lambda _ , r=row: self.delete_user(r))# Lambda for Delete
            Select_button.clicked.connect(lambda state,user_name=user_name:self.onSelectButtonClicked(user_name))
            button_layout = QHBoxLayout()  # Horizontal layout for buttons
            button_layout.addWidget(edit_button)
            button_layout.addWidget(delete_button)
            button_layout.addWidget(Select_button)
            button_widget = QWidget()
            button_widget.setLayout(button_layout)
            self.table.setCellWidget(row, 5, button_widget)  # Add button layout to Actions column (column 5)
    def add_user(self):
        add_dialog = UserDialog()
        if add_dialog.exec_():
            name = add_dialog.name_input.text()
            address = add_dialog.address_input.text()
            details = add_dialog.details_input.text()
            phone_number = add_dialog.phone_number_input.text()

            if name and address and phone_number:
                cursor = self.conn.cursor()
                cursor.execute('''
                    INSERT INTO Patients (name, address, details, phone_number)
                    VALUES (?, ?, ?, ?)
                ''', (name, address, details, phone_number))
                self.conn.commit()
                self.load_users()
                print("User added successfully.")
            else:
                print("Please fill in all required fields.")

    def edit_user(self, row):
        edit_dialog = UserDialog()
        edit_dialog.setWindowTitle("Edit User")
        edit_dialog.name_input.setText(self.table.item(row, 1).text())
        edit_dialog.address_input.setText(self.table.item(row, 2).text())
        edit_dialog.details_input.setText(self.table.item(row, 3).text())
        edit_dialog.phone_number_input.setText(self.table.item(row, 4).text())

        if edit_dialog.exec_():
            name = edit_dialog.name_input.text()
            address = edit_dialog.address_input.text()
            details = edit_dialog.details_input.text()
            phone_number = edit_dialog.phone_number_input.text()

            user_id = self.table.item(row, 0).text()

            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE Patients
                SET name=?, address=?, details=?, phone_number=?
                WHERE id=?
            ''', (name, address, details, phone_number, user_id))
            self.conn.commit()
            self.load_users()
            print("User edited successfully.")

    def delete_user(self, row):
        user_id = self.table.item(row, 0).text()

        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM Patients WHERE id=?', (user_id,))
        self.conn.commit()
        self.load_users()
        print("User deleted successfully.")
        
    def updateLabel(self, category, button_name):
            # Update the label text when a button is clicked
        self.Category_label.setText(f"Selected Category: {category} >>Selected Game: {button_name}")

    
class UserDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add User")
        self.setGeometry(200, 200, 400, 200)

        layout = QFormLayout()

        self.name_input = QLineEdit()
        self.address_input = QLineEdit()
        self.details_input = QLineEdit()
        
        
        self.phone_number_input = QLineEdit()
        # self.user_tab = user_tab

        layout.addRow("Name:", self.name_input)
        layout.addRow("Address:", self.address_input)
        layout.addRow("Details:", self.details_input)
        layout.addRow("Phone Number (10 digit only +91):", self.phone_number_input)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout.addRow(self.buttons)

        self.setLayout(layout)
        self.phone_number_input.textChanged.connect(self.validate_phone_number)
    def validate_phone_number(self):
        phone_number = self.phone_number_input.text()
        valid = re.match(r'^\d{10}$', phone_number) is not None

        if valid:
            self.phone_number_input.setStyleSheet("color: black; border: 1px solid black;")
            self.buttons.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.phone_number_input.setStyleSheet("color: red; border: 1px solid red;")
            self.buttons.button(QDialogButtonBox.Ok).setEnabled(False)
            
#     def updateTabName(self, new_tab_name):
#         current_index = self.Patient.currentIndex()
#         self.Patient.setTabText(1, new_tab_name)
#         self.selected_user_label.setText(f"Selected User: {new_tab_name}") 

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())