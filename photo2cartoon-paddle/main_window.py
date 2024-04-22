import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import utility
from PIL import Image,ImageTk
import cv2
from threading import Thread
from tkinter.filedialog import askopenfilename
from load_model import *
utility.enable_high_dpi_awareness()


def model_load():
    global model
    model = load_model()
    moudel_load_label.pack_forget()
    a.pack_forget()
thread1 = Thread(target=model_load)
thread1.start()

def select():
    global photo
    global img
    path = askopenfilename()
    print(path)
    if not path:
        return
    else:
        img = Image.open(path)
        img = img.resize((800, 600))
        photo = ImageTk.PhotoImage(img)
        photo_Label.config(image=photo)




def change_img():
    global cartoon
    cartoon = predict_img(model=model,input_img=img)
    cartoon = cartoon.resize((800, 600))
    cartoon = ImageTk.PhotoImage(cartoon)
    cartoon_Label.config(image=cartoon)


root = tk.Tk()
style = ttk.Style()

frame1 = ttk.Frame(root, padding=10)
frame1.pack(fill=tk.X)
title = ttk.Label(master=frame1,text='PHOTO2CARTOON',bootstyle=ttk.INFO)
title.pack(side=tk.TOP, padx=3, pady=10)
moudel_load_label = ttk.Label(frame1, text='模型导入中',bootstyle=ttk.PRIMARY)
moudel_load_label.pack(side=tk.LEFT,padx=3,pady=10)
a = ttk.Progressbar(frame1, bootstyle=ttk.SUCCESS, orient=tk.HORIZONTAL)
a.pack(side=tk.LEFT)
a.start()

video_frame = ttk.Frame(master=root,bootstyle=ttk.LIGHT,width=1600,height=600)
video_frame.pack(side=tk.TOP,ipadx=50,ipady=20)
mask = Image.new('RGB',(800,600),color='black')
photo = ImageTk.PhotoImage(mask)
photo_Label = tk.Label(video_frame,image=photo)#把图片整合到标签类中
photo_Label.pack(side=tk.LEFT)
cartoon_Label = tk.Label(video_frame,image=photo)#把图片整合到标签类中
cartoon_Label.pack(side=tk.RIGHT)

cartoom = None

frame2 = ttk.Frame(master=root)
frame2.pack(side=tk.BOTTOM,fill=tk.X)
select_button = ttk.Button(master=frame2,text='选择图片',bootstyle=ttk.INFO, width=12,padding=10,command=select)
select_button.pack(side=tk.LEFT,pady=10,padx=400)
change_button = ttk.Button(master=frame2,text='开始转换',bootstyle=ttk.INFO, width=12,padding=10,command=change_img)
change_button.pack(side=tk.RIGHT,pady=10,padx=400)

root.mainloop()