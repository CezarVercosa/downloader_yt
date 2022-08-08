from fileinput import filename
from tkinter import filedialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QPoint
from pytube import YouTube, Playlist
from pytube.exceptions import RegexMatchError
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow
from interface import Ui_MainWindow
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.downloadButton.clicked.connect(self.clickBtn)
        self.closeClickAction.clicked.connect(self.closeApp)
        self.minimizerClickAction.clicked.connect(self.minimizerApp)
        self.pastaButton.clicked.connect(self.browserFolder)

    def closeApp(self):
        self.close()
    
    def minimizerApp(self):
        self.showMinimized()
    
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        if event.modifiers() & Qt.ControlModifier:
            x = self.horizontalScrollBar().value()
            self.horizontalScrollBar().setValue(x - delta)

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()
        except AttributeError:
            pass

    def clickBtn(self):
        self.downloadButton.setDisabled(True)
        self.worker = threadWorker(linkYT=self.linkInput.text())
        self.linkInput.setText("")
        self.worker.start()
        self.worker.updateProgress.connect(self.conectionThreads)
        self.worker.updateName.connect(self.conectionMusicName)
        self.worker.finished.connect(self.handleFinished)
    
    def browserFolder(self):
        global folder
        folder = filedialog.askdirectory()
        self.diretorioInput.setText(folder)
        


    
    def conectionThreads(self, val):
        self.barraDeProgresso.setValue(val)
    
    def conectionMusicName(self, val):
        self.musicName.setText(val)
    
    def handleFinished(self):
        self.downloadButton.setDisabled(False)




class threadWorker(QThread):
    finished = pyqtSignal()
    updateProgress = pyqtSignal(int)
    updateName = pyqtSignal(str)
    
    def __init__(self, linkYT):
        QThread.__init__(self)
        self.link = linkYT
    
    def run(self):
        

        output = folder
        try:
            if Playlist(self.link):
                playlists = Playlist(self.link)
                for video in playlists.video_urls:
                    yt = YouTube(video, on_progress_callback=self.on_progress)
                    video = yt.streams.filter(only_audio=True).first()
                    self.updateName.emit(video.title)
                    out_file = video.download(output_path=output)
                    base, ext = os.path.splitext(out_file)
                    try:
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)
                        
                    except FileExistsError:
                        self.updateName.emit("Musica ja existente na pasta")
                        arquivoPlaylist = Path(new_file)
                        if arquivoPlaylist.is_file():
                            os.remove(out_file)
                        pass
                    except RegexMatchError:
                        self.updateName.emit("Link Invalido")
                        pass
                    
                        
                    
                    
        except:
            try:
                yt = YouTube(self.link, on_progress_callback=self.on_progress)
                video = yt.streams.filter(only_audio=True).first()
                self.updateName.emit(video.title)
                out_file = video.download(output_path=output)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print("out_file ", out_file)
                print("new_file ", new_file)
                print("output ", output)
            except FileExistsError:
                self.updateName.emit("Musica ja existente na pasta")
                arquivoVideo = Path(new_file)
                if arquivoVideo.is_file():
                    os.remove(out_file)
                pass
            except RegexMatchError:
                self.updateName.emit("Link Invalido")
                pass   
        self.finished.emit()
        
    def on_progress(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        progress = int(((size - bytes_remaining) / size) * 100)
        self.updateProgress.emit(progress)
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
