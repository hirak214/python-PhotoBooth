import cv2
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from skimage import data, io, filters
import skimage
import numpy as np


from GUI import *


def add_filter(image):
    pass
if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)

    cap = cv2.VideoCapture(1)
    while cap.isOpened():
        ret, frame = cap.read()

        # cv2.imshow('Photo Booth', frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # frame = add_filter(frame)
        frame_np = np.array(frame)

        # filter function implier goes here
        gui.frame = frame_np
        gui.call_function()
        frame = gui.frame
        # gui.f1_command(frame)


        img_update = ImageTk.PhotoImage(Image.fromarray(frame))
        gui.panel_image.configure(image=img_update)
        gui.panel_image.image = img_update
        gui.panel_image.update()

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


    root.mainloop()