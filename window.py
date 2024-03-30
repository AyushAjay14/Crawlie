from tkinter import *
import sys
import clustter
import main
def btn_clicked():
    depth = str(0)
    ss = str(0)
    depth = entry0.get()
    ss = entry1.get()
    url = entry2.get()
    # print(cluster , ss , depth)
    main.main_func(url , depth , ss , 0)
    sys.exit()


window = Tk()
window.geometry("848x516")
def new_window():
    def cluster_submit():
        query = entry3.get()
        count = entry4.get()
        clustter.fetch_image_urls(query , count)
        sys.exit()
    root = Toplevel(window)
    root.geometry("458x263")
    root.configure(bg = "#ffffff")
    canvas = Canvas(
        root,
        bg = "#ffffff",
        height = 263,
        width = 458,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./Tkinter/Tkinter2/background1.png")
    background = canvas.create_image(
        229.0, 131.5,
        image=background_img)

    entry3_img = PhotoImage(file = f"./Tkinter/Tkinter2/img_textBox3.png")
    entry3_bg = canvas.create_image(
        101.5, 80.5,
        image = entry3_img)

    entry3 = Entry(
        root,
        bd = 0,
        bg = "#fdfdfd",
        highlightthickness = 0)
    entry3.place(
        x = 28.0, y = 56,
        width = 147.0,
        height = 47)

    entry4_img = PhotoImage(file = f"./Tkinter/Tkinter2/img_textBox4.png")
    entry4_bg = canvas.create_image(
        339.0, 80.5,
        image = entry4_img)

    entry4 = Entry(
        root,
        bd = 0,
        bg = "#fdfdfd",
        highlightthickness = 0)

    entry4.place(
        x = 269.0, y = 56,
        width = 140.0,
        height = 47)

    img1 = PhotoImage(file = f"./Tkinter/Tkinter2/img1.png")
    b1 = Button(
        root,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = cluster_submit,
        relief = "flat")

    b1.place(
        x = 153, y = 155,
        width = 152,
        height = 53)

    root.resizable(False, False)
    root.mainloop()

   

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

background_img = PhotoImage(file = f"./Tkinter/background.png")
background = canvas.create_image(
    424.0, 259.5,
    image=background_img)

entry0_img = PhotoImage(file = f"./Tkinter/img_textBox0.png")
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

entry1_img = PhotoImage(file = f"./Tkinter/img_textBox1.png")
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

img0 = PhotoImage(file = f"./Tkinter/img0.png")
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

entry2_img = PhotoImage(file = f"./Tkinter/img_textBox2.png")
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
var1 = IntVar()
c1 = Checkbutton(window, text="cluster", variable=var1 , bg="white" , onvalue = 1, offvalue = 0,
command=new_window)
c1.place(x=705 , y = 322)
window.resizable(False, False)
window.mainloop()
