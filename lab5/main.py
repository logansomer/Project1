import tkinter
from gui import *


def main() -> object:
    window = Tk()
    window.geometry('275x325')
    window.configure(background='green')
    window.resizable(False, False)
    window.title('Data saver')
    GUI(window)
    window.mainloop()
if __name__ == '__main__':
    main()
