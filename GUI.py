import random
import tkinter
import tkinter as tk
import tkinter.font as tkFont
import numpy as np
import cv2
from scipy.interpolate import UnivariateSpline
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


class GUI:
    def __init__(self, root):

        self.clicked_button = 0
        self.frame = 0
        # setting title
        root.title("Photo Booth")
        # setting window size
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        print(screenwidth, screenheight)

        button_x_pos = int(screenwidth - 400)
        # alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # root.geometry(alignstr)
        # root.resizable(width=False, height=False)

        font = tkFont.Font(family='Arial', size=16)

        f1 = tk.Button(root)
        f1["bg"] = "#efefef"
        f1["font"] = font
        f1["fg"] = "#000000"
        f1["justify"] = "center"
        f1["text"] = "Invert"
        f1.place(x=button_x_pos, y=100, width=150, height=60)
        f1["command"] = self.f1_command

        f2 = tk.Button(root)
        f2["bg"] = "#efefef"
        f2["font"] = font
        f2["fg"] = "#000000"
        f2["justify"] = "center"
        f2["text"] = "Blurring"
        f2.place(x=button_x_pos, y=200, width=150, height=60)
        f2["command"] = self.f2_command

        f3 = tk.Button(root)
        f3["bg"] = "#efefef"
        f3["font"] = font
        f3["fg"] = "#000000"
        f3["justify"] = "center"
        f3["text"] = "Thresholding"
        f3.place(x=button_x_pos, y=300, width=150, height=60)
        f3["command"] = self.f3_command

        f4 = tk.Button(root)
        f4["bg"] = "#efefef"
        f4["font"] = font
        f4["fg"] = "#000000"
        f4["justify"] = "center"
        f4["text"] = "Grey"
        f4.place(x=button_x_pos, y=400, width=150, height=60)
        f4["command"] = self.f4_command

        f5 = tk.Button(root)
        f5["bg"] = "#efefef"
        f5["font"] = font
        f5["fg"] = "#000000"
        f5["justify"] = "center"
        f5["text"] = "Image Segmentation"
        f5.place(x=button_x_pos, y=500, width=150, height=60)
        f5["command"] = self.f5_command

        f6 = tk.Button(root)
        f6["bg"] = "#efefef"
        f6["font"] = font
        f6["fg"] = "#000000"
        f6["justify"] = "center"
        f6["text"] = "Sharpening"
        f6.place(x=button_x_pos, y=600, width=150, height=60)
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

    def f1_command(self):
        self.clicked_button = 1

        # #sepia
        # img_sepia = np.array(self.frame, dtype=np.float64)  # converting to float to prevent loss
        # img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
        #                                                 [0.349, 0.686, 0.168],
        #                                                 [0.393, 0.769,
        #                                                  0.189]]))  # multipying image with special sepia matrix
        # img_sepia[np.where(img_sepia > 255)] = 255  # normalizing values greater than 255 to 255
        # self.frame = np.array(img_sepia, dtype=np.uint8)

        # # sketch
        # sk_gray, self.frame = cv2.pencilSketch(self.frame, sigma_s=60, sigma_r=0.07, shade_factor=0.1)

        # #HDR
        # self.frame = cv2.detailEnhance(self.frame, sigma_s=12, sigma_r=0.15)

        #invert
        self.frame = cv2.bitwise_not(self.frame)

        # def LookupTable(x, y):
        #     spline = UnivariateSpline(x, y)
        #     return spline(range(256))
        # #summer
        # increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        # decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        # blue_channel, green_channel, red_channel = cv2.split(self.frame)
        # red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
        # blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
        # self.frame = cv2.merge((blue_channel, green_channel, red_channel))

    def f2_command(self):
        self.clicked_button = 2
        self.frame = cv2.blur(self.frame, (20, 20))


    def f3_command(self):
        self.clicked_button = 3
        ret, self.frame = cv2.threshold(self.frame, 127, 255, cv2.THRESH_BINARY)

    def f4_command(self):
        self.clicked_button = 4
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)


    def f5_command(self):
        self.clicked_button = 5
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        # apply thresholding
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # get a kernel
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        # extract the background from image
        sure_bg = cv2.dilate(opening, kernel, iterations=3)

        dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

        sure_fg = np.uint8(sure_fg)
        self.frame = sure_bg


    def f6_command(self):
        self.clicked_button = 6
        kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
        self.frame = cv2.filter2D(self.frame, -1, kernel)


    def click_bt_command(self):
        cv2.imwrite(f"images/Image{random.randint(1, 100)}.png", self.frame)

    def call_function(self):
        if self.clicked_button == 1: self.f1_command()
        if self.clicked_button == 2: self.f2_command()
        if self.clicked_button == 3: self.f3_command()
        if self.clicked_button == 4: self.f4_command()
        if self.clicked_button == 5: self.f5_command()
        if self.clicked_button == 6: self.f6_command()
        if self.clicked_button == 0: pass