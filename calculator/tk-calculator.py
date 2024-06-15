from tkinter import *

class Window:
    def __init__(self, master):

        self.equation = ""
        self.insert_index = 0

        # Creating the Title of the app
        self.label = Label(master=master, text="Calcultor", font="bold")
        self.label.pack()

        # Creating the entry box to enter the equation
        self.entry = Entry(master=master, textvariable=self.equation, width=50)
        self.entry.pack()

        #  Creating frame for buttons
        self.frame = Frame(master=master, pady=10)
        self.frame.pack()
        num_list = ['7', '8', '9', '/','**', '4', '5', '6', '*', '(', '1', '2', '3', '-', ')', '0', '.', '=', '+', '%']
        index_num = 0
        for i in range(4):
            for j in range(5):
                count = num_list[index_num]
                # Creating buttons for calculator
                button = Button(master=self.frame, relief="raised", fg= "black",bg= "gray", activebackground="white", text=f'{count}', command=lambda text = count: self.__action_command(text), width=8, pady= 5, font= ("bold", 10))

                # Placing the buttons on the grid
                button.grid(row=i, column=j, padx= 10, pady= 10)
                index_num += 1

        button = Button(master=self.frame, relief="raised", text="C",activebackground="white", command=self.__clear_text, width= 20, fg= "black", bg= "gray", pady= 5, font= ("bold", 10))
        button.grid(row= 4, column= 0, columnspan=2)

    
    # Button action
    def __action_command(self, num):
        if num == "=":
            result = self.__action_line()
            self.insert_index = 0
            self.__clear_text()
            self.entry.insert(self.insert_index, result)
            
        else:
            self.entry.insert(self.insert_index, num)
            self.equation += str(num)
            if num.isdigit():
                self.insert_index += 1
            else:
                self.insert_index += len(num) 
    
    # Evaluate the current equation and return the result
    def __action_line(self):
        return eval(self.equation)
    
    # Clear the current equation
    def __clear_text(self):
        self.entry.delete(0, END)
        self.equation = ""


if __name__ == '__main__':
    window = Tk()
    window.title("Calculator")
    window.geometry("500x500")
    app = Window(window)
    window.mainloop()