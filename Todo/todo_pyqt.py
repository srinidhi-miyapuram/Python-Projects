from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout, QTabWidget
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 800, 500)
        self.setWindowTitle("ToDo Application")

        # Creating window layout
        window_layout = QVBoxLayout()
        self.setLayout(window_layout)

        # Creating the tabs for todo application
        self.todo_tab = QTabWidget()
        self.todo_app_tab = QWidget()
        self.todo_tab.addTab(self.todo_app_tab, "Todo")

        self.todo_history_tab = QWidget()
        self.todo_tab.addTab(self.todo_history_tab, "History")
        window_layout.addWidget(self.todo_tab)

        # Creating the layout for todo application
        todo_layout = QVBoxLayout()
        self.todo_app_tab.setLayout(todo_layout)

        # Creating the layout for todo history
        self.history_layout = QVBoxLayout()
        self.todo_history_tab.setLayout(self.history_layout)
        self.history_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Creating Title Label for todo application
        title_label = QLabel()
        title_label.setText("ToDo List")
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        todo_layout.addWidget(title_label)
        title_label.setFixedHeight(30)

        # Setting layout for todo input
        todo_input_layout = QHBoxLayout()
        todo_layout.addLayout(todo_input_layout)
        todo_input_layout.setAlignment(self, Qt.AlignmentFlag.AlignTop)

        # Creating the input field for todo application
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Enter your task")
        todo_input_layout.addWidget(self.todo_input)
        self.todo_input.setMaxLength(100)

        # Creating the add and delete buttons to todo input layout
        todo_input_add = QPushButton()
        todo_input_add.setText("Add")
        todo_input_add.clicked.connect(self.__create_todo_task)

        todo_input_delete = QPushButton()
        todo_input_delete.setText("Cancel")
        todo_input_delete.clicked.connect(self.__cancel_task)
        todo_input_layout.addWidget(todo_input_add)
        todo_input_layout.addWidget(todo_input_delete)

        # Setting layout for todo list
        self.todo_list_group = QGroupBox()
        todo_layout.addWidget(self.todo_list_group)
        self.todo_list_layout = QVBoxLayout()
        self.todo_list_group.setLayout(self.todo_list_layout)
        self.todo_list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    def __create_todo_task(self):
        self.todo_list_elem_layout = QHBoxLayout()
        object_name = "horizon-" + str(self.count)
        self.todo_list_elem_layout.setObjectName(object_name)

        # Adding the task to the list of tasks
        self.todo_list_task = QLabel()
        self.todo_list_task.setText(self.todo_input.text())
        self.todo_list_task.setStyleSheet("""
                                            border: 1px solid black;
                                            padding: 0.5em;""")
        self.todo_list_task.setFixedWidth(550)
        self.todo_list_elem_layout.addWidget(self.todo_list_task)

        # Adding the completed and delete buttons to the list of tasks
        self.todo_task_complete = QPushButton()
        self.todo_task_complete.setText("Completed")
        self.todo_task_complete.clicked.connect(lambda: self.__complete_task(object_name))

        self.todo_task_delete = QPushButton()
        self.todo_task_delete.setText("Delete")
        self.todo_task_delete.clicked.connect(lambda: self.__delete_todo_task(object_name))

        self.todo_list_elem_layout.addWidget(self.todo_task_complete)
        self.todo_list_elem_layout.addWidget(self.todo_task_delete)
        self.todo_list_layout.addLayout(self.todo_list_elem_layout)

        self.count += 1
        self.todo_input.setText("")

    def __cancel_task(self):
        self.todo_input.setText("")

    def __delete_todo_task(self, name):
        for child in self.todo_list_layout.children():
            if child.objectName() == name:
                for i in range(child.count()):
                    item = child.itemAt(i)
                    item.widget().close()
                self.todo_list_layout.removeItem(child)
                break
        self.count -= 1

    def __complete_task(self, name):
        for child in self.todo_list_layout.children():
            if child.objectName() == name:
                label_text = child.itemAt(0).widget().text()
                history_label = QLabel()
                history_label.setText(label_text)
                history_label.setStyleSheet("""
                                            border: 2px solid black;
                                            padding: 0.5em;""")
                self.history_layout.addWidget(history_label)
        
        # Deleting the task from the list
        self.__delete_todo_task(name)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())