from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QStatusBar, QToolBar, QColorDialog, QMenuBar, QFileDialog
from PyQt6.QtGui import QColor, QMouseEvent, QPainter, QPen, QPixmap, QIcon, QAction
from PyQt6.QtCore import QPoint, Qt, QSize, QRect
import sys

class Canvas(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.starting_position = [[(0,0), (600, 600)]]
        self.initUI()


    def initUI(self):
        self.pixmap = QPixmap(600, 600)
        self.pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)
        self.drawing = False
        self.pen_width = 1
        self.eraser = False
        self.pen_color = Qt.GlobalColor.black
        self.point = QPoint()


    def mouseMoveEvent(self, event):
        self.mouse_position = event.pos()
        if event.buttons() and Qt.MouseButton.LeftButton and self.drawing:
            self.draw(self.mouse_position)
            self.parent.statusbar.showMessage(f"Mouse position is at {self.mouse_position.x()} and {self.mouse_position.y()} coordinates")
    
    def mousePressEvent(self, event):
        if event.button() ==  Qt.MouseButton.LeftButton:
            self.point = event.pos()
            self.drawing = True
            self.starting_position.append([self.point])
        
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_end_point = event.pos()
            self.drawing = False
            self.starting_position[-1].append(self.mouse_end_point)
    
    def draw(self, start_point):
        
        painter = QPainter(self.pixmap)
        if self.eraser == False:
            painter.begin(self)
            pen = QPen(self.pen_color, self.pen_width)
            painter.setPen(pen)
            painter.drawLine(self.point, start_point)
            self.point = start_point
        elif self.eraser == True:
            eraser = QRect(start_point.x(), start_point.y(), 15, 15)
            painter.eraseRect(eraser)
        self.update()
        
    
    def paintEvent(self, event):
        painter = QPainter(self)
        target = event.rect()
        painter.drawPixmap(target, self.pixmap, target)
        painter.end()
    
    def selected_tool(self, tool):
        match tool:
            case "pencil":
                self.pen_width = 3
                self.eraser = False
            case "brush":
                self.pen_width = 5
                self.eraser = False
            case "eraser":
                self.eraser = True
            case "color_bucket":
                self.eraser = False
                self.pen_color = QColorDialog.getColor()
            case _:
                self.pen_width = 1
                self.pen_color = Qt.GlobalColor.black
                self.eraser = False
    
    def new_file(self):
        self.pixmap.fill(Qt.GlobalColor.white)
        self.update()
    
    def save_file(self):
        fileName = QFileDialog.getSaveFileName(self, "Save As", "", "PNG File (*.png)")
        if fileName:
            self.pixmap.save(fileName[0], "png")
        file = fileName[0].split('/')[-1]
        self.setWindowTitle(file)
    

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Painting Application")
        self.setGeometry(200, 200, 600,600)
        canvas = Canvas(self)
        self.setCentralWidget(canvas)
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        toolbar = QToolBar()
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(24, 24))


        pencil = QAction(QIcon("./Images/pencil.png"), "Pencil", toolbar)
        pencil.triggered.connect(lambda: canvas.selected_tool("pencil"))

        brush = QAction(QIcon("./Images/brush.png"), "Brush", toolbar)
        brush.triggered.connect(lambda: canvas.selected_tool("brush"))

        eraser = QAction(QIcon("./Images/eraser.png"), "Eraser", toolbar)
        eraser.triggered.connect(lambda: canvas.selected_tool("eraser"))

        color_bucket = QAction(QIcon("./Images/color_bucket.png"), "Colors", toolbar)
        color_bucket.triggered.connect(lambda: canvas.selected_tool("color_bucket"))

        
        toolbar.addAction(pencil)
        toolbar.addAction(brush)
        toolbar.addAction(eraser)
        toolbar.addAction(color_bucket)

        self.new = QAction("New")
        self.new.triggered.connect(canvas.new_file)
        self.save = QAction("Save")
        self.save.triggered.connect(canvas.save_file)
        self.exit = QAction("Exit")
        self.exit.triggered.connect(self.close)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new)
        file_menu.addAction(self.save)
        file_menu.addSeparator()
        file_menu.addAction(self.exit)









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
