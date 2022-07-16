from encodings.punycode import selective_find
from tkinter import *
from RouletteArray import RA


class MyFirstGUI:
    entryTally = []
    optionsNumber = ('0',
                     '1R', '2B', '3R', '4B', '5R', '6B', '7R', '8B', '9R',
                     '10B', '11B', '12R', '13B', '14R', '15B', '16R', '17B', '18R',
                     '19R', '20B', '21R', '22B', '23R', '24B', '25R', '26B', '27R',
                     '28B', '29B', '30R', '31B', '32R', '33B', '34R', '35B', '36R')




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
        #back up to tally.txt
        with open("tally.txt", 'a') as writeFile:
            writeFile.write(entry+'\n')
        writeFile.close()
        #get the numerical representation of the draw by using its location
        location = self.optionsNumber.index(entry)
        print(location)



    def greet(self):
        print("Greetings!")

    def tally(entry):
        print("tally in class RA has been activated: tally the entry")
        # self.entryTally = self.entryTally + entry

    def getTally(self):
        print(RA.entryTally)

