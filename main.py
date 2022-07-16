from array import array

import txt as txt

from RouletteArray import RA
from tkinter import Tk, Label, Button
from GUI import MyFirstGUI

if __name__ == '__main__':
    print("main initiated")

    test = RA
    test.getTally(test)
    fileName = 'tally.txt'
    list = []
    with open("tally.txt") as tally:
        for line in tally:
            list.append(line.replace("\n",""))
    print(list)


    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
