from fileinput import filename
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from pytube import YouTube, Playlist
from pytube.exceptions import RegexMatchError
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QCursor
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("YT-Downloader")
        MainWindow.resize(641, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 321))
        self.label.setText("")
        backgroundImage = self.imagePath("assets\\zaytomd1c2e91.png")
        self.background = self.imagePath(backgroundImage)
        self.label.setPixmap(QtGui.QPixmap(self.background))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 641, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textUpDownload = QtWidgets.QLabel(self.frame)
        self.textUpDownload.setGeometry(QtCore.QRect(150, 20, 341, 21))
        self.textUpDownload.setStyleSheet("color: white; font-size: 16px;")
        self.textUpDownload.setAlignment(QtCore.Qt.AlignCenter)
        self.textUpDownload.setObjectName("textUpDownload")
        self.linkInput = QtWidgets.QLineEdit(self.frame)
        self.linkInput.setGeometry(QtCore.QRect(80, 50, 481, 31))
        self.linkInput.setStyleSheet("font-size: 15px;")
        self.linkInput.setObjectName("linkInput")
        self.downloadButton = QtWidgets.QPushButton(self.frame)
        self.downloadButton.setGeometry(QtCore.QRect(280, 200, 75, 23))
        self.downloadButton.setStyleSheet("color: black;")
        self.downloadButton.setObjectName("downloadButton")
        self.downloadButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.barraDeProgresso = QtWidgets.QProgressBar(self.frame)
        self.barraDeProgresso.setEnabled(True)
        self.barraDeProgresso.setGeometry(QtCore.QRect(80, 240, 515, 31))
        self.barraDeProgresso.setProperty("value", 0)
        self.barraDeProgresso.setObjectName("barraDeProgresso")
        self.barraDeProgresso.setStyleSheet("color: white;")
        self.musicName = QtWidgets.QLabel(self.frame)
        self.musicName.setGeometry(QtCore.QRect(80, 270, 481, 41))
        self.musicName.setStyleSheet("font-size: 20px; color: white;")
        self.musicName.setText("")
        self.musicName.setAlignment(QtCore.Qt.AlignCenter)
        self.musicName.setObjectName("musicName")
        self.minimizerButton = QtWidgets.QLabel(self.frame)
        self.minimizerButton.setGeometry(QtCore.QRect(572, 1, 30, 31))
        self.minimizerButton.setText("")
        minimizer = self.imagePath("assets\\minimize-button.png")
        self.minimizerButton.setPixmap(QtGui.QPixmap(minimizer))
        self.minimizerButton.setScaledContents(True)
        self.minimizerButton.setObjectName("minimizerButton")
        self.minimizerClickAction = QtWidgets.QPushButton(self.frame)
        self.minimizerClickAction.setGeometry(QtCore.QRect(572, 1, 30, 31))
        self.minimizerClickAction.setStyleSheet("background-color: transparent;")
        self.minimizerClickAction.setObjectName("minimizerClickAction")
        self.minimizerClickAction.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton = QtWidgets.QLabel(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(610, 0, 31, 31))
        self.closeButton.setText("")
        closeB = self.imagePath("assets\\closebutton.png")
        self.closeButton.setPixmap(QtGui.QPixmap(closeB))
        self.closeButton.setScaledContents(True)
        self.closeButton.setObjectName("closeButton")
        self.closeClickAction = QtWidgets.QPushButton(self.frame)
        self.closeClickAction.setGeometry(QtCore.QRect(610, 0, 31, 31))
        self.closeClickAction.setStyleSheet("background-color: transparent;")
        self.closeClickAction.setObjectName("closeClickAction")
        self.closeClickAction.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.saveText = QtWidgets.QLabel(self.frame)
        self.saveText.setGeometry(QtCore.QRect(0, 100, 641, 31))
        self.saveText.setStyleSheet("font-size: 16px; color: white;")
        self.saveText.setAlignment(QtCore.Qt.AlignCenter)
        self.saveText.setObjectName("saveText")
        self.diretorioInput = QtWidgets.QLineEdit(self.frame)
        self.diretorioInput.setGeometry(QtCore.QRect(140, 140, 331, 21))
        self.diretorioInput.setObjectName("diretorioInput")
        self.pastaButton = QtWidgets.QPushButton(self.frame)
        self.pastaButton.setGeometry(QtCore.QRect(475, 140, 61, 21))
        self.pastaButton.setObjectName("pastaButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("YT-Downloader", "YT-Downloader"))
        self.textUpDownload.setText(_translate("MainWindow", "Digite abaixo o link da musica"))
        self.downloadButton.setText(_translate("MainWindow", "Baixar"))
        self.saveText.setText(_translate("MainWindow", "Escolha onde deseja salvar"))
        self.pastaButton.setText(_translate("MainWindow", "Pasta"))  
    
    def imagePath(self, relative):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative)