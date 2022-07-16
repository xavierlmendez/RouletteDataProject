from encodings.punycode import selective_find
from tkinter import *
from RouletteArray import RA


class MyFirstGUI:
    entryTally = []
    optionsNumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                     "10", "11", "12", "13", "14", "15", "16", "17", "18",
                     "19", "20", "21", "22", "23", "24", "25", "26", "27",
                     "28", "29", "30", "31", "32", "33", "34", "35", "36"]

    optionsColors = [" ", 'B', 'R']
    myGame = RA

    def __init__(self, master):
        self.master = master
        self.clickedNum = StringVar()
        self.clickedNum.set(0)
        self.clickedColor = StringVar()
        self.clickedColor.set(0)
        master.title("Roulette Probability GUI")
        master.geometry("400x350")
        self.label = Label(master, text="please input roulette draw")
        self.label.pack()

        self.drop_number = OptionMenu(master, self.clickedNum, *MyFirstGUI.optionsNumber)
        self.drop_number.pack()

        self.drop_color = OptionMenu(master, self.clickedColor, *MyFirstGUI.optionsColors)
        self.drop_color.pack()

        self.drop_button = Button(master, text="calculate probabilities", command=self.showNum)
        self.drop_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def showNum(self):
        self.label.config(text=self.clickedNum.get())

    def showcolor(self):
        self.label.config(text=self.clickedColor.get())

    def greet(self):
        print("Greetings!")

    def tally(entry):
        print("tally in class RA has been activated: tally the entry")
        # self.entryTally = self.entryTally + entry

    def getTally(self):
        print(RA.entryTally)

