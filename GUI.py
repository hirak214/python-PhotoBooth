import random
import tkinter
import tkinter as tk
import tkinter.font as tkFont
import numpy as np
import cv2
from scipy.interpolate import UnivariateSpline
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from scipy import signal
from progressbar import ProgressBar

from playsound import playsound



class GUI:
    def __init__(self, root):

        self.clicked_button = 0
        self.frame = 0
        # setting title
        root.title("Photo Booth")

        screenwidth = int(root.winfo_screenwidth())
        screenheight = int(root.winfo_screenheight())
        print(screenwidth, screenheight)
        # setting window size
        root.geometry(f"{screenwidth}x{screenwidth}")

        button_x_pos = int(screenwidth - 500)
        # alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # root.geometry(alignstr)
        # root.resizable(width=False, height=False)

        font = tkFont.Font(family='Arial', size=16)
        width_var = 200
        height_var = 50

        v1 = tk.IntVar()

        f1 = tk.Button(root)
        f1["bg"] = "#efefef"
        f1["font"] = font
        f1["fg"] = "#000000"
        f1["justify"] = "center"
        f1["text"] = "Invert"
        f1.place(x=button_x_pos, y=100, width=width_var, height=height_var)
        f1["command"] = self.f1_command

        f2 = tk.Button(root)
        f2["bg"] = "#efefef"
        f2["font"] = font
        f2["fg"] = "#000000"
        f2["justify"] = "center"
        f2["text"] = "Blurring"
        f2.place(x=button_x_pos, y=200, width=width_var, height=height_var)
        f2["command"] = self.f2_command

        f3 = tk.Button(root)
        f3["bg"] = "#efefef"
        f3["font"] = font
        f3["fg"] = "#000000"
        f3["justify"] = "center"
        f3["text"] = "Thresholding"
        f3.place(x=button_x_pos, y=300, width=width_var, height=height_var)
        f3["command"] = self.f3_command

        f4 = tk.Button(root)
        f4["bg"] = "#efefef"
        f4["font"] = font
        f4["fg"] = "#000000"
        f4["justify"] = "center"
        f4["text"] = "Sketch"
        f4.place(x=button_x_pos, y=400, width=width_var, height=height_var)
        f4["command"] = self.f4_command

        f5 = tk.Button(root)
        f5["bg"] = "#efefef"
        f5["font"] = font
        f5["fg"] = "#000000"
        f5["justify"] = "center"
        f5["text"] = "Sharpening"
        f5.place(x=button_x_pos, y=500, width=width_var, height=height_var)
        f5["command"] = self.f5_command

        f6 = tk.Button(root)
        f6["bg"] = "#efefef"
        f6["font"] = font
        f6["fg"] = "#000000"
        f6["justify"] = "center"
        f6["text"] = "Revert"
        f6.place(x=button_x_pos, y=600, width=width_var, height=height_var)
        f6["command"] = self.f6_command

        click_bt = tk.Button(root)
        click_bt["bg"] = "#efefef"
        ft = font
        click_bt["font"] = ft
        click_bt["fg"] = "#000000"
        click_bt["justify"] = "center"
        click_bt["text"] = "Click"
        click_bt.place(x=545, y=900, width=150, height=60)
        click_bt["command"] = self.click_bt_command

        self.panel_image = tk.Label(root)  # ,image=img)
        self.panel_image.place(x=10, y=10, width=1080, height=720)

        s1 = tk.Scale(root, variable=v1, from_=1, to=100, orient=tk.HORIZONTAL)

        l3 = tk.Label(root, text="Threshold Scaler")

        s1.place(x=button_x_pos, y=700)
        l3.place(x=button_x_pos, y=720)

    def f1_command(self):
        self.clicked_button = 1
        self.frame = cv2.bitwise_not(self.frame)

    def f2_command(self):
        self.clicked_button = 2
        mask = np.ones([10, 10], dtype=int)
        mask = mask / 100
        self.frame = signal.convolve2d(self.frame, mask)

    def f3_command(self):
        #  thresholding
        self.clicked_button = 3
        r, c = self.frame.shape
        T = 128
        for i in range(r):
            for j in range(c):
                if self.frame[i, j] > T:
                    self.frame[i, j] = self.frame.max()
                else:
                    self.frame[i, j] = 0

    def f4_command(self):
        # edge detection
        self.clicked_button = 4
        mask_horizontal = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        horizontal = cv2.filter2D(self.frame, -1, mask_horizontal)

        mask_vertical = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        vertical = cv2.filter2D(self.frame, -1, mask_vertical)

        mask_forwarddiagonal = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])
        forwarddiagonal= cv2.filter2D(self.frame, -1, mask_forwarddiagonal)

        mask_backworddiagonal = np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]])
        backwarddiagonal = cv2.filter2D(self.frame, -1, mask_backworddiagonal)

        self.frame = horizontal + vertical + forwarddiagonal + backwarddiagonal




    def f5_command(self):
        self.clicked_button = 5
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        self.frame = cv2.filter2D(self.frame, -1, kernel)

    def f6_command(self):
        self.clicked_button = 6
        self.frame = self.frame

    def click_bt_command(self):
        cv2.imwrite(f"images/Image{random.randint(1, 100)}.png", self.frame)
        playsound('click.wav')


    def show1(self):
        sel = "Horizontal Scale Value = " + str(v1.get())
        l1.config(text=sel, font=("Courier", 14))

    def call_function(self):
        if self.clicked_button == 1: self.f1_command()
        if self.clicked_button == 2: self.f2_command()
        if self.clicked_button == 3: self.f3_command()
        if self.clicked_button == 4: self.f4_command()
        if self.clicked_button == 5: self.f5_command()
        if self.clicked_button == 6: self.f6_command()
        if self.clicked_button == 0: pass
