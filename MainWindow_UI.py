from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1062, 704)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1062, 620))
        MainWindow.setMaximumSize(QSize(5000, 5000))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(40, 40, 134, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(60, 60, 201, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(50, 50, 167, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(27, 27, 89, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush6 = QBrush(QColor(29, 29, 97, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush4)
        brush7 = QBrush(QColor(240, 240, 240, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush4)
        brush8 = QBrush(QColor(147, 147, 194, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush4)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.SolidPattern)

        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)

        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush11 = QBrush(QColor(64, 64, 216, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        brush12 = QBrush(QColor(20, 20, 67, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush4)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.SolidPattern)

        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)

        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush4)
        brush14 = QBrush(QColor(0, 120, 215, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush4)

        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)

        MainWindow.setPalette(palette)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionAbout_2 = QAction(MainWindow)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        icon = QIcon()
        icon.addFile(u":/i18n/pro1_en_GB.qm", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_2.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drawButton = QPushButton(self.centralwidget)
        self.drawButton.setObjectName(u"drawButton")
        self.drawButton.setGeometry(QRect(220, 380, 121, 51))
        font = QFont()
        font.setFamily(u"Myanmar Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.drawButton.setFont(font)
        self.drawButton.setLayoutDirection(Qt.LeftToRight)
        self.drawButton.setCheckable(False)
        self.drawButton.setAutoExclusive(False)
        self.drawButton.setAutoDefault(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 801, 81))
        font1 = QFont()
        font1.setFamily(u"Myanmar Text")
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 110, 491, 241))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 471, 121))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setObjectName(
            u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 451, 83))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Myanmar Text")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setMouseTracking(False)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.startSpinBox = QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.startSpinBox.setObjectName(u"startSpinBox")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.startSpinBox.setFont(font4)
        self.startSpinBox.setProperty("showGroupSeparator", False)
        self.startSpinBox.setMinimum(-999999.989999999990687)
        self.startSpinBox.setMaximum(999999.989999999990687)
        self.startSpinBox.setValue(-10.000000000000000)

        self.verticalLayout.addWidget(self.startSpinBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.label_8 = QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font2)
        self.label_8.setMouseTracking(False)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.endSpinBox = QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.endSpinBox.setObjectName(u"endSpinBox")
        self.endSpinBox.setFont(font4)
        self.endSpinBox.setValue(10.000000000000000)

        self.verticalLayout_2.addWidget(self.endSpinBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.label_9 = QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font2)
        self.label_9.setMouseTracking(False)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.pointSpinBox = QSpinBox(self.horizontalLayoutWidget_2)
        self.pointSpinBox.setObjectName(u"pointSpinBox")
        self.pointSpinBox.setFont(font4)
        self.pointSpinBox.setMaximum(999999999)
        self.pointSpinBox.setValue(10)

        self.verticalLayout_4.addWidget(self.pointSpinBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.functionTextBox = QLineEdit(self.frame)
        self.functionTextBox.setObjectName(u"functionTextBox")
        self.functionTextBox.setGeometry(QRect(80, 160, 381, 31))
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.functionTextBox.sizePolicy().hasHeightForWidth())
        self.functionTextBox.setSizePolicy(sizePolicy2)
        self.functionTextBox.setSizeIncrement(QSize(6, 5))
        font5 = QFont()
        font5.setFamily(u"Palatino Linotype")
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.functionTextBox.setFont(font5)
        self.functionTextBox.setCursor(QCursor(Qt.IBeamCursor))
        self.functionTextBox.setContextMenuPolicy(Qt.NoContextMenu)
        self.functionTextBox.setAutoFillBackground(False)
        self.functionTextBox.setFrame(True)
        self.functionTextBox.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.functionTextBox.setClearButtonEnabled(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(20, 140, 48, 78))
        self.label_2.setFont(font2)
        self.label_2.setMouseTracking(False)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(550, 110, 489, 461))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayoutWidget_2 = QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 471, 441))
        self.GraphLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.GraphLayout.setObjectName(u"GraphLayout")
        self.GraphLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.GraphLayout.setContentsMargins(0, 0, 0, 0)
        self.errorText = QTextBrowser(self.centralwidget)
        self.errorText.setObjectName(u"errorText")
        self.errorText.setGeometry(QRect(40, 440, 491, 171))
        palette1 = QPalette()
        brush15 = QBrush(QColor(255, 0, 0, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.errorText.setPalette(palette1)
        font6 = QFont()
        font6.setFamily(u"OCR A Extended")
        font6.setPointSize(22)
        font6.setBold(False)
        font6.setWeight(50)
        self.errorText.setFont(font6)
        self.errorText.setFrameShape(QFrame.NoFrame)
        self.creationLabel = QLabel(self.centralwidget)
        self.creationLabel.setObjectName(u"creationLabel")
        self.creationLabel.setGeometry(QRect(230, 620, 489, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        self.creationLabel.setPalette(palette2)
        font7 = QFont()
        font7.setFamily(u"MV Boli")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setUnderline(False)
        font7.setWeight(50)
        self.creationLabel.setFont(font7)
        self.creationLabel.setFrameShape(QFrame.NoFrame)
        self.creationLabel.setFrameShadow(QFrame.Plain)
        self.creationLabel.setAlignment(Qt.AlignCenter)
        self.functionDisplay = QTextBrowser(self.centralwidget)
        self.functionDisplay.setObjectName(u"functionDisplay")
        self.functionDisplay.setGeometry(QRect(550, 580, 489, 41))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.functionDisplay.setPalette(palette3)
        font8 = QFont()
        font8.setPointSize(16)
        font8.setBold(True)
        font8.setWeight(75)
        self.functionDisplay.setFont(font8)
        self.functionDisplay.setLayoutDirection(Qt.LeftToRight)
        self.functionDisplay.setFrameShape(QFrame.WinPanel)
        self.functionDisplay.setFrameShadow(QFrame.Plain)
        self.functionDisplay.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1062, 26))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionAbout_2)

        self.changeUI(MainWindow)

        self.drawButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    def editUI(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Function Plotter", None))
        self.actionAbout_2.setText(QCoreApplication.translate(
            "MainWindow", u"Repository link", None))

        self.actionAbout_2.setShortcut(
            QCoreApplication.translate("MainWindow", u"Alt+R", None))

        self.drawButton.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"drawButton", None))

        self.drawButton.setText(
            QCoreApplication.translate("MainWindow", u"Draw", None))

        self.drawButton.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+S", None))

        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Function Plotter", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"x :", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Start", None))

        self.startSpinBox.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"startSpinBox", None))

        self.label_8.setText(
            QCoreApplication.translate("MainWindow", u":", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"End", None))

        self.endSpinBox.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"endSpinBox", None))

        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u":", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"# of points", None))

        self.pointSpinBox.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"pointSpinBox", None))

        self.functionTextBox.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"FunctionTextBox", None))

        self.functionTextBox.setText(
            QCoreApplication.translate("MainWindow", u"x", None))
        self.functionTextBox.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"y =", None))

        self.errorText.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"errorText", None))

        self.errorText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:'OCR A Extended'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

        self.creationLabel.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"fuctionLabel", None))

        self.creationLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Created By Ahmed Saad", None))

        self.functionDisplay.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"functionDisplay", None))

        self.functionDisplay.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                "p, li { white-space: pre-wrap; }\n"
                                                                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Y= x</p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate(
            "MainWindow", u"About", None))
