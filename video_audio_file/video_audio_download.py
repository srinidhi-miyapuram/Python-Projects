from pytube import YouTube
import shutil
from moviepy.editor import *

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Video Downloader")
        self.setGeometry(300, 200, 600, 600)

        window_layout = QVBoxLayout()
        self.setLayout(window_layout)
        window_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Title layout

        vertical_layout = QVBoxLayout()
        window_layout.addLayout(vertical_layout)

        title_label = QLabel()
        title_label.setText("Video Downloader")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vertical_layout.addWidget(title_label)

        # Input URL field
        url_input = QLineEdit()
        url_input.setPlaceholderText("Enter video URL")
        url_input.setFixedHeight(40)
        vertical_layout.addWidget(url_input)

        # Destination Path
        filePath = "Downloads"

        self.download_status = QLabel()
        self.download_status.setText("")
        vertical_layout.addWidget(self.download_status)

        # Download Button
        button_layout = QHBoxLayout()
        window_layout.addLayout(button_layout)
        
        download_button = QPushButton()
        download_button.setText("Download MP4")
        download_button.clicked.connect(lambda: self.__download_video(url_input.text(), filePath))
        download_button.setFixedHeight(35)
        button_layout.addWidget(download_button)

        # Audio Download
        audio_download_button = QPushButton()
        audio_download_button.setText("Download MP3")
        audio_download_button.clicked.connect(lambda: self.__download_audio(url_input.text(), filePath))
        audio_download_button.setFixedHeight(35)
        button_layout.addWidget(audio_download_button)

    
    def __download_audio(self, url_input, filePath):
        try:
            self.download_status.setText("Downloading audio .........")
            yt = YouTube(url_input)
            audio = yt.streams.filter(only_audio=True)
            print(audio)
            audio.download(filePath + '/audio/')
            self.download_status.setText("Audio downloaded successfully!")
        except Exception as e:
            self.download_status.setText(f"Error downloading audio: {str(e)}")
    
    def __download_video(self, url_input, filePath):
        try:
            self.download_status.setText("Downloading video...........")
            yt = YouTube(url_input)
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video.download(filePath + "/video/")
            self.download_status.setText("Video downloaded successfully!")
        except Exception as e:
            self.download_status.setText(f"Error downloading video: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())