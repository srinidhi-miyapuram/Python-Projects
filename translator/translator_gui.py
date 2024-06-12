
# Importing the required modules
from translator import textTranslator, ExcelFile
from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QComboBox, QWidget, QLabel, QFormLayout, QHBoxLayout
import sys

# Creating a class for the window
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translator")
        self.setGeometry(200,100,500,500)

        # Getting the country languages and their codes in a dictionary
        self.countryLanguages = ExcelFile().get_country_names()

        # Creating the layout for the window
        layout = QFormLayout()
        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout3 = QHBoxLayout()
        horizontal_layout4 = QHBoxLayout()

        self.setLayout(layout)

        # Label 1 for the input field
        layout.addRow(horizontal_layout1)
        lable1 = QLabel("Text")
        self.text1 = QLineEdit(self)
        self.text1.setText("")
        
        # adding the label and line edit to the layout
        horizontal_layout1.addWidget(lable1)
        horizontal_layout1.addWidget(self.text1)

        # Label 2 for the dropdown field to select destination language
        layout.addRow(horizontal_layout2)
        lable2 = QLabel("Destination Language")
        self.dropdown = QComboBox()

        self.countryNames = list(self.countryLanguages.values())
        self.countryShortNames = list(self.countryLanguages.keys())

        # Adding the country names to the dropdown field
        for key, value in self.countryLanguages.items():
            self.dropdown.addItem(value.title())

        horizontal_layout2.addWidget(lable2)
        horizontal_layout2.addWidget(self.dropdown)

        # Label 3 for the translated text
        layout.addRow(horizontal_layout3)
        self.textLable = QLabel(self)
        self.textLable.setText("Translated Text")
        horizontal_layout3.addWidget(self.textLable)

        # Adding the submit and cancel buttons to the layout
        layout.addRow(horizontal_layout4)
        button1 = QPushButton("Submit")
        button2 = QPushButton("Cancel")
        horizontal_layout4.addWidget(button1)
        horizontal_layout4.addWidget(button2)

        # Getting the selected language from dropdown
        index_country = self.countryNames.index(self.dropdown.currentText().lower())
        self.language = self.countryShortNames[index_country]

        # Connecting the submit and cancel buttons to the functions
        button1.clicked.connect(self.translate_text)
        button2.clicked.connect(self.close_Event)


    # Function to close the program
    def close_Event(self):
        sys.exit(app.exec())
    
    # Function to translate the text
    def translate_text(self):
        # Checking if input field is modified or not
        input_state = self.text1.isModified()
        if input_state:
            self.text = self.text1.text()
        else:
            self.text1.setPlaceholderText("Enter valid input")
        
        # Getting the selected language from dropdown
        if self.dropdown.currentTextChanged:
            self.language = self.countryShortNames[self.countryNames.index(self.dropdown.currentText().lower())]
        
        # Checking if the input field is empty
        if len(self.text.strip()) == 0:
            self.text = "Enter valid input text"
        
        # Translating the text
        self.translated_text = textTranslator(self.text, self.language).get_text()

        # Updating the translated text
        self.textLable.setText(self.translated_text)
        self.textLable.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())