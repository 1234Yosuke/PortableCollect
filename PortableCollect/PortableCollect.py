import tkinter as tk
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfilename(initialdir = "/",
                                      title = "アプリを選択",
                                      filetypes = (("実行可能ファイル","*.exe"),("All files","*.*")))

def quit():
    window.quit()
    return 0

window = tk.Tk()
window.title("Portable Collect")

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="開く", command=open_file)
filemenu.add_command(label="閉じる", command=quit)

menubar.add_cascade(label="ファイル", menu=filemenu)

window.config(menu=menubar)

window.mainloop()