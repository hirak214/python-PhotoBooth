import tkinter
import tkinter as tk
import tkinter.font as tkFont


class GUI:
    def __init__(self, root):
        # setting title
        root.title("Photo Booth")
        # setting window size
        width = 3000
        height = 2000
        # screenwidth = root.winfo_screenwidth()
        # screenheight = root.winfo_screenheight()
        # alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # root.geometry(alignstr)
        root.resizable(width=False, height=False)

        font = tkFont.Font(family='Arial', size=16)

        f1 = tk.Button(root)
        f1["bg"] = "#efefef"
        f1["font"] = font
        f1["fg"] = "#000000"
        f1["justify"] = "center"
        f1["text"] = "Filter 1"
        f1.place(x=440, y=50, width=70, height=25)
        f1["command"] = self.f1_command

        f2 = tk.Button(root)
        f2["bg"] = "#efefef"
        f2["font"] = font
        f2["fg"] = "#000000"
        f2["justify"] = "center"
        f2["text"] = "Filter 2"
        f2.place(x=440, y=100, width=70, height=25)
        f2["command"] = self.f2_command

        f3 = tk.Button(root)
        f3["bg"] = "#efefef"
        f3["font"] = font
        f3["fg"] = "#000000"
        f3["justify"] = "center"
        f3["text"] = "Filter 3"
        f3.place(x=440, y=150, width=70, height=25)
        f3["command"] = self.f3_command

        f4 = tk.Button(root)
        f4["bg"] = "#efefef"
        f4["font"] = font
        f4["fg"] = "#000000"
        f4["justify"] = "center"
        f4["text"] = "Filter 4"
        f4.place(x=440, y=200, width=70, height=25)
        f4["command"] = self.f4_command

        f5 = tk.Button(root)
        f5["bg"] = "#efefef"
        f5["font"] = font
        f5["fg"] = "#000000"
        f5["justify"] = "center"
        f5["text"] = "Filter 5"
        f5.place(x=440, y=250, width=70, height=25)
        f5["command"] = self.f5_command

        f6 = tk.Button(root)
        f6["bg"] = "#efefef"
        f6["font"] = font
        f6["fg"] = "#000000"
        f6["justify"] = "center"
        f6["text"] = "Filter 6"
        f6.place(x=440, y=300, width=70, height=25)
        f6["command"] = self.f6_command

        click_bt = tk.Button(root)
        click_bt["bg"] = "#efefef"
        ft = font
        click_bt["font"] = ft
        click_bt["fg"] = "#000000"
        click_bt["justify"] = "center"
        click_bt["text"] = "Click"
        click_bt.place(x=190, y=420, width=70, height=25)
        click_bt["command"] = self.click_bt_command

        self.panel_image = tk.Label(root)  # ,image=img)
        self.panel_image.place(x=0, y=0, width=1080, height=720)

    def f1_command(self):
        return 1

    def f2_command(self):
        print("command")

    def f3_command(self):
        print("command")

    def f4_command(self):
        print("command")

    def f5_command(self):
        print("command")

    def f6_command(self):
        print("command")

    def click_bt_command(self):
        print("command")

