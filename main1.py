from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from tkinter import filedialog
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
from tkinter import Tk, Toplevel, Button, Label







class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.brush_size = 10
        self.brush_color = "red"
        self.color = "red"
        self.setUI()


    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)


    def set_color(self, new_color):
        self.color = new_color


    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def setUI(self):
        self.parent.title("Paint Lite")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white") #цвет фона листа

        self.canv.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)

        self.canv.bind("<B1-Motion>", self.draw)



        color_lab = Label(self, text="Цвет: ")

        color_lab.grid(row=0, column=0, padx=6)

        red_btn = Button(self, text="Красный", width=10, fg="red", command=lambda: self.set_color("red"))
        red_btn.grid(row=0, column=1)

        green_btn = Button(self, text="Зеленый", width=10, fg="green", command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Синий", width=10, fg="blue", command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Черный", width=10, fg="black", command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="Белый", width=10, fg="grey", command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)







        # twelfth_bth = Button(self, text="Круг", width=10, command=lambda:  self.set_brush_size(20))
        # twelfth_btn.grid(row=0, column=6)
        #
        #
        # create_rectangle(__x0: float, __y0: float, __x1: float, __y1: float)



        size_lab = Label(self, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="2x", width=10, command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="5x", width=10, command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="7x", width=10, command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="10x", width=10, command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="20x", width=10, command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="50x", width=10, command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)

        clear_btn = Button(self, text="Очистить", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)




def close_win():
    if askyesno("Выход", "Вы уверены?"):
        root.destroy()


def about():
    showinfo("Demo Paint", "Сделано на Python")




def save_file():
    types = [("Text files", "*.txt"),
             ("Png", "*.png"),
             ("Jpeg", "*.jpeg"),
             ("All files", "*.*")]
    file = filedialog.asksaveasfile(title = "Save File",
                                    initialdir = ".",
                                    defaultextension=".png",
                                    filetypes=types)
    if file:
        file.write("This is the content of the file.")
        file.close()




def main():
    global root
    root = Tk()
    root.geometry("800x600+300+300")
    app = Paint(root)
    m = Menu(root)
    root.config(menu=m)

    fm = Menu(m)
    m.add_cascade(label="Файл", menu=fm)
    fm.add_command(label="Выход", command=close_win)
    fm.add_command(label="Сохранить", command=save_file)

    hm = Menu(m)
    m.add_cascade(label="Справка", menu=hm)
    hm.add_command(label="О программе", command=about)
    root.mainloop()
    # save_button = tk.Button(root, text="Save File", command=save_file)
    # save_button.pack()


if __name__ == "__main__":
    main()