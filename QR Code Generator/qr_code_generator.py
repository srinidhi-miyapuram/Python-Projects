import pyqrcode

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(200, 200, 600, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title_label = QLabel("QR Code Generator")
        self.layout.addWidget(title_label)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Enter the url name here ")
        self.layout.addWidget(self.input_name)

        self.input_url = QLineEdit()
        self.input_url.setPlaceholderText("Enter the URL here")
        self.layout.addWidget(self.input_url)

        generator_button = QPushButton()
        generator_button.setText("Generate QR Code")
        self.layout.addWidget(generator_button)
        generator_button.clicked.connect(self.generate_qr_code)
    
    def generate_qr_code(self):
        url = self.input_url.text()
        name = self.input_name.text() + ".png"
        qr_code = pyqrcode.create(url)
        qr_code.png(name, scale=4)
        qr_code_label = QLabel()
        pixmap = QPixmap(name)
        qr_code_label.setPixmap(pixmap)
        qr_code_label.setFixedWidth(500)
        qr_code_label.setFixedHeight(400)
        qr_code_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(qr_code_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())