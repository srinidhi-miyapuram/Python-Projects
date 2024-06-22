from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QFileDialog, QInputDialog
from PyQt6.QtGui import QAction, QTextCursor, QColor
from PyQt6.QtCore import Qt
import clipboard
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.currentFileName = None

        self.setWindowTitle("Notepad")
        self.setGeometry(300, 200, 600, 600)

        
        self.textLabel = QTextEdit()
        self.setCentralWidget(self.textLabel)
       
        menu = self.menuBar()
        menu.setFixedHeight(35)

        file = menu.addMenu("File")

        # Adding New to menu
        self.open = QAction("Open")
        file.addAction(self.open)
        self.open.triggered.connect(self.openFile)

        # Adding New to menu
        self.new = QAction("New")
        file.addAction(self.new)
        self.new.triggered.connect(self.newFile)

        # Adding Save to menu
        self.save = QAction("Save")
        file.addAction(self.save)
        self.save.triggered.connect(self.saveFile)

        # Adding Save As to menu
        self.saveAs = QAction("Save As")
        file.addAction(self.saveAs)
        self.saveAs.triggered.connect(self.saveFileAs)

        # Adding seperator
        file.addSeparator()

        # Adding Exit to menu
        self.exit = QAction("Exit")
        file.addAction(self.exit)
        self.exit.triggered.connect(self.exitFile)

        # Adding Edit menu
        edit = menu.addMenu("Edit")
        
        # Adding copy to menu
        self.copy = QAction("Copy")
        edit.addAction(self.copy)
        self.copy.triggered.connect(self.copyFile)

        # Adding paste to menu
        self.paste = QAction("Paste")
        edit.addAction(self.paste)
        self.paste.triggered.connect(self.pasteFile)

        # Adding cut to menu
        self.cut = QAction("Cut")
        edit.addAction(self.cut)
        self.cut.triggered.connect(self.cutFile)

        # Adding seperator
        edit.addSeparator()

        # Adding redo to menu
        self.redo = QAction("Redo")
        edit.addAction(self.redo)
        self.redo.triggered.connect(self.textLabel.redo)

        # Adding undo to menu
        self.undo = QAction("Undo")
        edit.addAction(self.undo)
        self.undo.triggered.connect(self.textLabel.undo)

        edit.addSeparator()

        # Adding find to menu
        self.findWord = QAction("Find")
        edit.addAction(self.findWord)
        self.findWord.triggered.connect(self.findWords)

        # Adding find to menu
        self.replaceWord = QAction("Replace")
        edit.addAction(self.replaceWord)
        self.replaceWord.triggered.connect(self.replaceWords)


    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File")
        with open(fileName[0], 'r') as f:
            self.textLabel.setText(f.read())
        self.currentFileName = fileName[0]
        name = self.currentFileName.split('/')[-1]
        self.setWindowTitle(name)

    def newFile(self):
        self.currentFileName = None
        self.textLabel.setText("")
        self.setWindowTitle("Notepad")

    def saveFileAs(self):
        fileName = QFileDialog.getSaveFileName(self,"Save File","","All Files (*);; Python.File (.py);; Test Files (*.txt)")
        if fileName[0]:
            with open(fileName[0], "w") as f:
                f.write(self.textLabel.toPlainText())
            self.currentFileName = fileName[0]
            name = self.currentFileName.split('/')[-1]
            self.setWindowTitle(name)

    
    def saveFile(self):
        if self.currentFileName:
            with open(self.currentFileName, "w") as f:
                f.write(self.textLabel.toPlainText())
        else:
            self.saveFileAs()


    def exitFile(self):
        self.saveFile()
        self.destroy()
    
    def copyFile(self):
        self.textLabel.copy()
        copied_text = clipboard.paste().strip()
        if len(copied_text) == 0:
            total_text = self.textLabel.toPlainText()
            clipboard.copy(total_text)
        self.textLabel.autoFormatting()
        
    
    def pasteFile(self):
        word = clipboard.paste()
        clipboard.copy(word)
        self.textLabel.paste()
    
    def cutFile(self):
        self.textLabel.cut()
    
    def findWords(self):
        word = QInputDialog.getText(self, "Find Text", "Search")
        print(word)
        if word[1]:
            words = []
            self.textLabel.moveCursor(QTextCursor.MoveOperation.Start)
            highlight_color = QColor(Qt.GlobalColor.yellow)
            while self.textLabel.find(word[0]):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)
                selection.cursor = self.textLabel.textCursor()
                words.append(selection)
            self.textLabel.setExtraSelections(words)
    
    def replaceWords(self):
        word = QInputDialog.getText(self, "Find Words", "Search")
        if word[1]:
            word2 = QInputDialog.getText(self, "Replace", "Serach")
            highlight_color = QColor(Qt.GlobalColor.yellow)
            words = []
            self.textLabel.moveCursor(QTextCursor.MoveOperation.Start)
            while self.textLabel.find(word[0]):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)
                selection.cursor = self.textLabel.textCursor()
                selection.cursor.removeSelectedText()
                selection.cursor.insertText(word2[0])
                words.append(selection)

            self.textLabel.setExtraSelections(words)
            


            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())