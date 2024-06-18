from tkinter import *
from tkinter import messagebox
import json

class Window(object):
    def __init__(self, master):
        self.ind = 0
        self.score = 0
        self.master = master
        self.buttons = []
        
        # Loading the json file
        file = open('text.json')
        json_file_load = json.load(file)
        self.title_list = json_file_load['quizzes']
        self.frames = []
        self.__get_home_page()
    
    # Home page for quiz
    def __get_home_page(self):
        if len(self.buttons) != 0:
            self.label.destroy()
            for f in self.buttons:
                f.destroy()
        self.label = Label(master=self.master, text="Select a Quiz", font=("bold", 30))
        self.label.pack()
        titles = self.__get_json_file()

        for title in titles:
            self.frame = Frame(master=self.master, pady=10)
            self.frame.pack()
            button = Button(master=self.frame, text=title, relief= "groove", font=("bold", 20), command=lambda word = title: self.__get_quiz_options(word) )
            button.pack()
            self.frames.append(self.frame)

    # Quiz page
    def __get_quiz_options(self, title):
        self.label.destroy()
        for f in self.frames:
            f.destroy()
        self.questions_list = self.__get_json_file(title)
        # for question in questions_list:
        self.label = Label(master=self.master, text= self.questions_list[self.ind]["question"], font=("bold", 26))
        self.label.pack()
        choice_list = self.questions_list[self.ind]["choices"]
        self.button_frames = []
        for choice in choice_list.keys():
            self.frame = Frame(master=self.master, pady=10)
            self.frame.pack()
            button = Button(master=self.frame, text= choice, command=lambda ch_ls=choice_list, ch=choice, word=title: self.__get_answer(ch_ls, ch, word), font=("bold", 20))
            button.pack()
            self.buttons.append(self.frame)
            self.button_frames.append(button)
    
    # Getting details from the json file
    def __get_json_file(self,title = None):
        if title is None:
            titles_list = []

            for title_ in self.title_list:
                titles_list.append(title_["quizTitle"])
            return titles_list
        else:
            for title_ in self.title_list:
                if title_["quizTitle"] == title:
                    return title_["questions"]
    
    # Checking if the user selected answer is correct
    def __get_answer(self, choice_list, choice, title):
        # If the questions are completed successfully
        if self.ind >= len(self.questions_list)-1:
            self.__get_message()
        else:
            # If the user selected answer is correct
            if choice_list[choice] == True:
                self.label.destroy()
                for f in self.buttons:
                    f.destroy()
                self.ind += 1
                self.score += 1
                self.__get_quiz_options(title)
            # If the user selected incorrect answer
            else:
                for f in self.button_frames:
                    f.config(state=DISABLED)
                self.__get_message()
        
    # Getting dialog message
    def __get_message(self):
        message = f"Your Score is {self.score}\n Do you want to continue?"
        self.score = 0
        msg = messagebox.askquestion(message=message)
        if msg == "yes":
            self.ind = 0
            self.__get_home_page()
        else:
            self.master.destroy()


if __name__ == "__main__":
    window = Tk()
    app = Window(window)
    window.title("Quiz Application")
    window.geometry("600x600")
    window.mainloop()