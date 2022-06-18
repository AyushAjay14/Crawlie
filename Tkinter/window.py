from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("848x516")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 516,
    width = 848,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    424.0, 259.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    542.5, 291.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#bebebe",
    highlightthickness = 0)

entry0.place(
    x = 500.0, y = 271,
    width = 85.0,
    height = 38)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    752.5, 291.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#bebebe",
    highlightthickness = 0)

entry1.place(
    x = 712.0, y = 271,
    width = 81.0,
    height = 38)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 585, y = 358,
    width = 121,
    height = 49)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    650.5, 176.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#bebebe",
    highlightthickness = 0)

entry2.place(
    x = 490.0, y = 154,
    width = 321.0,
    height = 42)

window.resizable(False, False)
window.mainloop()
