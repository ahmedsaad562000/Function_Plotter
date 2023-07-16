from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow_UI(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1216, 663)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1216, 663))
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
        self.frame.setGeometry(QRect(20, 110, 511, 241))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setStyleSheet(
            ".QFrame{border: 1px solid white; border-radius: 10px;}")
        self.functionTextBox = QLineEdit(self.frame)
        self.functionTextBox.setObjectName(u"functionTextBox")
        self.functionTextBox.setGeometry(QRect(80, 160, 401, 40))

        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.functionTextBox.sizePolicy().hasHeightForWidth())
        self.functionTextBox.setSizePolicy(sizePolicy1)
        self.functionTextBox.setSizeIncrement(QSize(6, 5))
        self.functionTextBox.setStyleSheet(
            "QLineEdit{border: 1px solid white; border-radius: 5px;}")
        font2 = QFont()
        font2.setFamily(u"Palatino Linotype")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.functionTextBox.setFont(font2)
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
        self.label_2.setStyleSheet(
            ".QLabel{color: rgb(255, 255, 255);}")
        font3 = QFont()
        font3.setFamily(u"Myanmar Text")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)
        self.label_2.setMouseTracking(False)
        self.horizontalFrame_2 = QFrame(self.frame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setGeometry(QRect(14, 30, 481, 83))
        self.horizontalFrame_2.setFrameShape(QFrame.Panel)
        self.horizontalFrame_2.setStyleSheet(
            ".QFrame{border: 1px solid white; border-radius: 10px;}")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.horizontalFrame_2)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(14)
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setStyleSheet(
            ".QLabel{color: rgb(255, 255, 255);}")
        self.verticalLayout.addWidget(self.label_4)

        self.startSpinBox = QDoubleSpinBox(self.horizontalFrame_2)
        self.startSpinBox.setObjectName(u"startSpinBox")
        BoxesFont = QFont()
        BoxesFont.setPointSize(10)
        BoxesFont.setBold(True)
        BoxesFont.setWeight(75)
        self.startSpinBox.setFont(BoxesFont)
        self.startSpinBox.setProperty("showGroupSeparator", False)
        self.startSpinBox.setMinimum(-999999.989999999990687)
        self.startSpinBox.setMaximum(999999.989999999990687)
        self.startSpinBox.setValue(-10.000000000000000)

        self.verticalLayout.addWidget(self.startSpinBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.line = QFrame(self.horizontalFrame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.horizontalFrame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setStyleSheet(
            ".QLabel{color: rgb(255, 255, 255);}")

        self.verticalLayout_2.addWidget(self.label_5)

        self.endSpinBox = QDoubleSpinBox(self.horizontalFrame_2)
        self.endSpinBox.setObjectName(u"endSpinBox")
        self.endSpinBox.setFont(BoxesFont)
        self.endSpinBox.setMinimum(-999999.989999999990687)
        self.endSpinBox.setMaximum(999999.989999999990687)
        self.endSpinBox.setValue(10.000000000000000)

        self.verticalLayout_2.addWidget(self.endSpinBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.horizontalFrame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.horizontalFrame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setStyleSheet(
            ".QLabel{color: rgb(255, 255, 255);}")

        self.verticalLayout_4.addWidget(self.label_7)

        self.pointSpinBox = QSpinBox(self.horizontalFrame_2)
        self.pointSpinBox.setObjectName(u"pointSpinBox")
        self.pointSpinBox.setFont(BoxesFont)
        self.pointSpinBox.setMinimum(2)
        self.pointSpinBox.setMaximum(99999)
        self.pointSpinBox.setValue(10)

        self.verticalLayout_4.addWidget(self.pointSpinBox)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setStyleSheet(
            ".QFrame{border: 12px solid white; border-radius: 10px;}")
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(540, 110, 651, 461))
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayoutWidget_2 = QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 631, 441))
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
        brush16 = QBrush(QColor(255, 0, 0, 128))
        brush16.setStyle(Qt.NoBrush)

        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)

        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        brush17 = QBrush(QColor(255, 0, 0, 128))
        brush17.setStyle(Qt.NoBrush)

        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)

        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        brush18 = QBrush(QColor(255, 0, 0, 128))
        brush18.setStyle(Qt.NoBrush)

        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)

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
        self.creationLabel.setGeometry(QRect(640, 580, 489, 31))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1216, 26))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionAbout_2)

        self.editUi(MainWindow)

        self.drawButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    def editUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Function Plotter", None))
        self.actionAbout_2.setText(QCoreApplication.translate(
            "MainWindow", u"Repository link", None))

        self.actionAbout_2.setShortcut(
            QCoreApplication.translate("MainWindow", u"Alt+R", None))

        self.drawButton.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Draw Enter", None))

        self.drawButton.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"drawButton", None))

        self.drawButton.setText(
            QCoreApplication.translate("MainWindow", u"Draw", None))

        self.drawButton.setShortcut(QCoreApplication.translate(
            "MainWindow", u"Return", None))

        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Function Plotter", None))

        self.functionTextBox.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"FunctionTextBox", None))

        self.functionTextBox.setText(
            QCoreApplication.translate("MainWindow", u"x^2", None))
        self.functionTextBox.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"y =", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Start", None))

        self.startSpinBox.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"startSpinBox", None))

        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"End", None))

        self.endSpinBox.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"endSpinBox", None))

        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"# of points", None))

        self.pointSpinBox.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"pointSpinBox", None))

        self.errorText.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"errorText", None))

        self.errorText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:'OCR A Extended'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

        self.creationLabel.setAccessibleName(
            QCoreApplication.translate("MainWindow", u"fuctionLabel", None))

        self.creationLabel.setText(QCoreApplication.translate(
            "MainWindow", u"Created By Ahmed Saad", None))
        self.menuMenu.setTitle(QCoreApplication.translate(
            "MainWindow", u"About", None))

    def setErrorText(self, Text):
        self.errorText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:'OCR A Extended'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />" + Text + "</p></body></html>", None))
