from RouletteArray import RA
from tkinter import Tk, Label, Button
from GUI import MyFirstGUI

if __name__ == '__main__':
    print("main initiated")

    test = RA
    test.getTally(test)

    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
