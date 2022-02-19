import PIL
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
from tkinter import *
global k
k=0
root=Tk()
root.title("Kappa")
my_img0=PIL.ImageTk.PhotoImage(PIL.Image.open(r'C:\Users\\rodri\Pictures\20190124_121447.jpg'))
my_img1=PIL.ImageTk.PhotoImage(PIL.Image.open(r'C:\Users\\rodri\Pictures\20190124_121521.jpg'))
my_img2=PIL.ImageTk.PhotoImage(PIL.Image.open(r'C:\Users\\rodri\Pictures\20190124_121518.jpg'))
pictures_list=[my_img0,my_img1,my_img2]
global my_label
my_label=Label(image=pictures_list[k])
my_label.grid(row=0,column=0,columnspan=3)

def show(image_showed,t):
    global k
    if t==0:
        k=k-1
    if t==1:
        k=k+1
    global my_label
    my_label.grid_forget()
    my_label=Label(image=pictures_list[k])

    if k==0:
        button_back=Button(root,text="<<",state=DISABLED)
    else:
        button_back=Button(root,text="<<",command=lambda:show(k-1,t=0))
    button_exit=Button(root,text='Exit',command=root.quit)
    if k==2:
        button_forward=Button(root,text=">>",state=DISABLED)
    else:
        button_forward=Button(root,text=">>",command=lambda:show(k+1,t=1))
        t=1

    button_back.grid(row=1,column=0)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)
    my_label.grid(row=0,column=0,columnspan=3)




if k==0:
    button_back=Button(root,text="<<",state=DISABLED)
else:
    button_back=Button(root,text="<<",command=lambda:show(k-1,t=0))
    t=0
button_exit=Button(root,text='Exit',command=root.quit)
if k==2:
    button_forward=Button(root,text=">>",state=DISABLED)
else:
    button_forward=Button(root,text=">>",command=lambda:show(k+1,t=1))
    t=1

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
root.mainloop()