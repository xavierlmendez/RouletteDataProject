from encodings.punycode import selective_find
from tkinter import *
from RouletteArray import RA


class MyFirstGUI:
    entryTally = []
    optionsNumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                     "10", "11", "12", "13", "14", "15", "16", "17", "18",
                     "19", "20", "21", "22", "23", "24", "25", "26", "27",
                     "28", "29", "30", "31", "32", "33", "34", "35", "36"]

    optionsLetter = [" ", 'B', 'R']
    myGame = RA

    def __init__(self, master):
        self.master = master
        self.clickedNum = StringVar()
        self.clickedNum.set(0)
        master.title("Roulette Probability GUI")
        master.geometry("400x350")
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.drop = OptionMenu(master, self.clickedNum.get(), *MyFirstGUI.optionsNumber)
        self.drop.pack()

        self.drop_button = Button(master, text="calculate probabilities", command=self.show)
        self.drop_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def show(self):
        self.label.config(text=self.clickedNum.get())

    def greet(self):
        print("Greetings!")

    def tally(entry):
        print("tally in class RA has been activated: tally the entry")
        # self.entryTally = self.entryTally + entry

    def getTally(self):
        print(RA.entryTally)

