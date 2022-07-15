from RouletteArray import RA
from tkinter import Tk, Label, Button
from GUI import MyFirstGUI

if __name__ == '__main__':
    print("main initiated")
    myGame = RA
    myGame.returnProb(7)
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
