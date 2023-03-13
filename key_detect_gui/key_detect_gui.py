from tkinter import *
from PIL import Image, ImageTk
import keyboard, win32api
win = Tk()
size = (700,400)
win.geometry(f"{size[0]}x{size[1]}+50+50")
win.wm_attributes("-topmost", True)
def cvs_create():
    cvs = Canvas(win)
    cvs.config(width=size[0],height=size[1],bd=0,highlightthickness=0)
    cvs.pack()
    return cvs

cvs = cvs_create()

def image_read(name):
    img = Image.open(f"{name}.png")
    return img

img_dict = {"w":[image_read("w0"), image_read("w1")],
            "a":[image_read("a0"), image_read("a1")],
            "s":[image_read("s0"), image_read("s1")],
            "d":[image_read("d0"), image_read("d1")],
            "left":[image_read("left0"), image_read("left1")],
            "right":[image_read("right0"), image_read("right1")],
            "low":[image_read("low0")]}


class myImg:
    def __init__(self, name):
        self.name = name
        self.img = img_dict[self.name][0]
        if len(self.name) == 1: # self.name이 w,a,s,d인 경우
            if keyboard.is_pressed(self.name):
                self.img = img_dict[self.name][1]
        elif self.name == "left":
            if win32api.GetKeyState(0x01) < 0 : 
                self.img = img_dict[self.name][1]
        elif self.name == "right":
            if win32api.GetKeyState(0x02) < 0 : 
                self.img = img_dict[self.name][1]
        self.img_resize = 0.35
        self.img_size = (round(self.img.width*self.img_resize),
                        round(self.img.height*self.img_resize))
        self.img_pos = (round(self.img_size[0]/2), round(self.img_size[1]/2))
        self.img = self.img.resize(self.img_size, Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img, master = win)
    def show(self):
        cvs.create_image(self.img_pos, image = self.img)
        
name_list = ["w","a","s","d","left","right","low"]
win.update()

while True:
    cvs.destroy()
    cvs = cvs_create()
    img_list = []
    for name in name_list:
        img_list.append(myImg(name))
        img_list[-1].show()
    win.update()



