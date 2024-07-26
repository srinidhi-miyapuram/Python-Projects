import sys
import requests
import googletrans
from googletrans import Translator

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QTextEdit, QPushButton, QComboBox, QVBoxLayout,QHBoxLayout, QFormLayout
from PyQt6.QtCore import Qt

class Quotation:
    def __init__(self):
        self.getQuotation()
    
    def getQuotation(self):
        quote = self.__getQuote()
        return quote
    
    def __getQuote(self):
        api_url = 'https://api.api-ninjas.com/v1/quotes'
        api_key = "KcO7E7mOTo7YKsjjNBW8UuAmzpRToWwr1yxUN3tY"
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        if response.status_code == requests.codes.ok:
            response = response.json()
            print(response)
            return response[0]["quote"]
        else:
            print("Error:", response.status_code, response.text)
            return "No Quote"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.getQuote = Quotation()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Learn Languages")
        self.setGeometry(200, 100, 800, 500)

        # layout
        formLayout = QFormLayout()
        verticallayout = QVBoxLayout()
        verticallayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(formLayout)
        formLayout.addRow(verticallayout)

        # Quote label
        self.quoteLabel = QLabel()
        self.quote = self.getQuote.getQuotation()
        self.quoteLabel.setText(self.quote)
        self.quoteLabel.setWordWrap(True)
        self.quoteLabel.adjustSize()
        self.quoteLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        verticallayout.addWidget(self.quoteLabel)

        # Refresh button
        refreshButton = QPushButton("Refresh")
        refreshButton.clicked.connect(self.__getNewQuote)
        verticallayout.addWidget(refreshButton)

        # Practice language and language selection
        horizontalLayout = QHBoxLayout()
        formLayout.addRow(horizontalLayout)

        userTextField = QTextEdit()
        userTextField.setMaximumWidth(600)
        userTextField.setMaximumHeight(100)
        userTextField.setPlaceholderText("Enter your text here ...")
        horizontalLayout.addWidget(userTextField)

        self.languagedropdown = QComboBox()
        self.__getLanguages()
        self.languagedropdown.setFixedHeight(30)
        horizontalLayout.addWidget(self.languagedropdown)

        # Get Translated text
        translateButton = QPushButton("Translate")
        translateButton.clicked.connect(self.__translate)
        formLayout.addWidget(translateButton)

        # Translated Text label
        self.translatedText = QLabel()
        self.translatedText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.translatedText.setWordWrap(True)
        formLayout.addWidget(self.translatedText)


    def __getNewQuote(self):
        self.quote = self.getQuote.getQuotation()
        self.quoteLabel.setText(self.quote)

    def __getLanguages(self):
        languages = googletrans.LANGUAGES
        languages = list(languages.values())
        for language in languages:
            self.languagedropdown.addItem(language)
    
    def __translate(self):
        translator = Translator()
        languages = googletrans.LANGCODES
        language = self.languagedropdown.currentText()
        language = languages[language]
        translatedText = translator.translate(self.quote, language).text
        self.translatedText.setText(translatedText)
        self.translatedText.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())