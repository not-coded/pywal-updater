from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import sys
import pywal_updater

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initGUI()
    
    def initGUI(self):

        self.setWindowTitle("Pywal Updater")
        self.setFixedSize(300, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Pywal Updater", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label, 0, Qt.AlignmentFlag.AlignTop)

        self.wallpaperLabel = QLabel(self)

        self.updatePixmap()

        layout.addWidget(self.wallpaperLabel, 0, Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Update", self)
        button.clicked.connect(self.updateWallpaper)
        layout.addWidget(button, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.show()
    
    def updateWallpaper(self):
        pywal_updater.updateWallpaper()
        self.updatePixmap()

    
    def updatePixmap(self):
        self.wallpaperPixmap = QPixmap(pywal_updater.get_current_wallpaper())
        self.wallpaperPixmap = self.wallpaperPixmap.scaled(250, 550, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        self.wallpaperLabel.setPixmap(self.wallpaperPixmap)
        self.wallpaperLabel.resize(self.wallpaperPixmap.size())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()