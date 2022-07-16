from encodings.punycode import selective_find
from tkinter import *
from RouletteArray import RA


class MyFirstGUI:
    entryTally = []
    optionsNumber = ('[0]',
                     '[1, "R"]', '[2, "B"]', '[3, "R"]', '[4, "B"]', '[5, "R"]', '[6, "B"]', '[7, "R"]', '[8, "B"]', '[9, "R"]',
                     '[10, "B"]', '[11, "B"]', '[12, "R"]', '[13, "B"]', '[14, "R"]', '[15, "B"]', '[16, "R"]', '[17, "B"]', '[18, "R"]',
                     '[19, "R"]', '[20, "B"]', '[21, "R"]', '[22, "B"]', '[23, "R"]', '[24, "B"]', '[25, "R"]', '[26, "B"]', '[27, "R"]',
                     '[28, "B"]', '[29, "B"]', '[30, "R"]', '[31, "B"]', '[32, "R"]', '[33, "B"]', '[34, "R"]', '[35, "B"]', '[36, "R"]')




    def __init__(self, master):
        self.master = master
        self.clickedNum = StringVar()
        self.clickedNum.set('please select a draw')
        self.clickedColor = StringVar()
        self.clickedColor.set(0)
        master.title("Roulette Probability GUI")
        master.geometry("400x350")
        self.label = Label(master, text="please input roulette draw")
        self.label.pack()

        self.drop_number = OptionMenu(master, self.clickedNum, *MyFirstGUI.optionsNumber)
        self.drop_number.pack()


        self.drop_button = Button(master, text="enter draw", command=self.showNum)
        self.drop_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def showNum(self):
        self.label.config(text=self.clickedNum.get())
        entry = (self.clickedNum.get())
        with open("tally.txt", 'a') as writeFile:
            writeFile.write(entry+'\n')
        writeFile.close()



    def greet(self):
        print("Greetings!")

    def tally(entry):
        print("tally in class RA has been activated: tally the entry")
        # self.entryTally = self.entryTally + entry

    def getTally(self):
        print(RA.entryTally)

