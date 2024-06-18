from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QHBoxLayout, QComboBox, QSlider, QFormLayout
from PyQt6.QtTextToSpeech import QTextToSpeech
from PyQt6.QtCore import Qt 
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text to Speech Translator")
        self.setGeometry(300, 200, 500, 500)

        layout = QFormLayout()
        horizontal1 = QHBoxLayout()
        horizontal2 = QHBoxLayout()
        self.setLayout(layout)

        layout.addRow(horizontal1)
        self.textLabel = QLineEdit(self)
        self.button = QPushButton()
        self.button.setText("Submit")
        self.button.clicked.connect(self.text_to_speech)

        horizontal1.addWidget(self.textLabel)
        horizontal1.addWidget(self.button)

        # Engine
        layout.addRow(horizontal2)
        self.engines = QTextToSpeech.availableEngines()
        if len(self.engines) > 0:
            self.engine = QTextToSpeech(self.engines[0])
        
        # Voices
        self.voices = []
        self.dropdown = QComboBox()
        for voice in self.engine.availableVoices():
            self.voices.append(voice)
            self.dropdown.addItem(voice.name())
        
        # If user changes voice in dropdown
        self.dropdown.currentIndexChanged.connect(self.text_to_speech)

        # Creating horizontal slider for volume control
        self.volumeControl = QSlider(Qt.Orientation.Horizontal, self)
        self.volumeControl.setMinimum(50)
        self.volumeControl.setMaximum(200)
        self.volumeControl.setValue(10)
        self.volumeControl.valueChanged.connect(self.text_to_speech)

        horizontal2.addWidget(self.dropdown)
        horizontal2.addWidget(self.volumeControl)
    
    # Speech
    def text_to_speech(self):
        self.text = self.textLabel.text()
        self.volume_change()
        self.engine.say(self.text)
    
    # Volume and voice setter
    def volume_change(self):
        volume_value = self.volumeControl.value()
        self.engine.setVolume(float(volume_value / 100))
        self.engine.setVoice(self.voices[self.dropdown.currentIndex()])

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
