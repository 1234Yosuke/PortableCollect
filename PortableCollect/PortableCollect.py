from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
from tkinter import messagebox

def open_file():
    file = filedialog.askopenfilename(initialdir = "/",
                                      title = "アプリを選択",
                                      filetypes = (("実行可能ファイル","*.exe"),("All files","*.*")))

def quit():
    window.quit()
    return 0

def developer():
    messagebox.showinfo("開発者", "ZIP")

window = Tk()
window.title("Portable Collect")

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="開く", command=open_file)
filemenu.add_command(label="閉じる", command=quit)

helpmenu = Menu(menubar, tearoff=1)
helpmenu.add_command(label="開発者", command=developer)

menubar.add_cascade(label="ファイル", menu=filemenu)
menubar.add_cascade(label="ヘルプ", menu=helpmenu)

window.config(menu=menubar)

window.mainloop()