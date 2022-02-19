import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Tkinter import *

domain_min = 1
domain_max = 10
order_min = 0
order_max = 3
fig = Figure(figsize=(10,5), dpi=50)

def module(x):
    global domain, order, output_message, fig, a, x_vals, y_vals

    domain = float(domain_slide.get())
    order = int(order_slide.get())

    output_message = 'f(1) = %i\nf(2) = %i\nf(3) = %i\nf(4) = %i\nf(5) = %i\nf(6) = %i\n\
f(7) = %i\nf(8) = %i\nf(9) = %i\nf(10)= %i'%(1**order,2**order,3**order,4**order,5**order,\
                                             6**order,7**order,8**order,9**order,10**order)

    output_message_text.set(output_message)

    x_vals = np.linspace(0,domain,100)
    y_vals = x_vals**order

    a = fig.add_subplot(111)
    a.clear()
    a.plot(x_vals,y_vals,color='blue')

#GUI
root = Tk()

domain_slide = DoubleVar()
order_slide = DoubleVar()
output_message_text = StringVar()

ds = Scale(root, variable = domain_slide, from_ = domain_min, to = domain_max, command = module)
ds.grid(column = 0, row = 0)

o_s = Scale(root, variable = order_slide, from_ = order_min, to = order_max, command = module)
o_s.grid(column = 1, row = 0)

out_message = Message(root, textvariable = output_message_text, width = 300, bg = 'white').grid(column = 0, row = 1, rowspan = 3)


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().grid(column=3,row=1)
canvas.show()

label = Label(root)
label.grid()

root.mainloop()