from pdf_compressor.ilovepdf import Compress
from pdf_ilovPDF_api import api_key

from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
import sys

stylesheet = """
    title_label_style {
        font-size: 80px;
        padding: 5px;
        font-weight: bold;
    }
    button_label{
        border: 2px solid black;
        padding: 5px;
        font-size: 30px;
    }
    button_label:hover{
                    background-color:#d3d3d3;
                    }

"""

class CompressionFile:
    def __init__(self, filePath):
        self.filePath = filePath
        self.fileName = filePath.split('/')[-1]
        

    def compress(self):
        try:
            file_path_name = '/'.join(self.filePath.split('/')[:-1]) + "/compressed_files/"

            compressor = Compress(api_key, "low")
            compressor.add_file(self.filePath)
            compressor.process()
            compressor.download(file_path_name)
            return True, file_path_name
        except Exception as e:
            return False, None

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("File Compression")
        self.setGeometry(300, 200, 500, 300)

        self.file_path = ""

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Creating the title label
        title_label = QLabel()
        title_label.setObjectName("title_label_style")
        title_label.setText("File Compression")
        title_label.font().setBold(True)
        title_label.font().setPixelSize(80)
        self.layout.addWidget(title_label)

        # Creating the output file label
        input_file_label = QPushButton()
        input_file_label.setText("Select File")
        input_file_label.setFixedWidth(100)
        input_file_label.setFixedHeight(40)
        input_file_label.setObjectName("button_label")
        input_file_label.clicked.connect(self.open_file)
        self.layout.addWidget(input_file_label)
    
    def open_file(self):
        # Creating the input file dialog
        input_file_dialog = QFileDialog()
        self.file_path = input_file_dialog.getOpenFileName()[0]
        compression_obj = CompressionFile(self.file_path)
        compressed_data, filePath = compression_obj.compress()

        dialog_box = QMessageBox(self)
        dialog_box.setWindowTitle("Compressed")
        self.layout.addWidget(dialog_box)
        dialog_box.setGeometry(200, 200, 500, 500)
        if compressed_data:
            dialog_box.setText(f"File compressed successfully \nFile is saved at {filePath}")
        else:
            dialog_box.setText("Failed to compress the file.")
        dialog_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = Window()
    window.show()
    sys.exit(app.exec())