import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
from random import randrange


FONT_TITLE = ("Verdana", 12)


class CorrPlot(tk.Tk):
    """Handles observations & their correlation, maps them on a graph

    Args:
        tk (tkinter): tkinter window containing the app
    """
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        
        tk.Tk.wm_title(self, "Correlation Plot")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = PageThree(container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Correlation tool", font=FONT_TITLE)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Add random obs", command=lambda: self.addObservations("sugar", [randrange(1,23,1) for i in range(8)],[randrange(1,23,1) for i in range(8)]))
        button1.pack()

        self.f = Figure(figsize=(5,5), dpi=100)
        
        self.addObservations("coffe", [4,5,7,9,11,13,15,18], [5,7,9,10,12,14,15,20], color="blue")

        

        canvas = FigureCanvasTkAgg(self.f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def addObservations(self, name, x, y, color="red", alpha=0.5):
        a = self.f.add_subplot(1,1,1)
        a.scatter(x,y, alpha=0.5, c=color, edgecolors='none', s=30, label=name)
        canvas = FigureCanvasTkAgg(self.f, self)
        

        

app = CorrPlot()
app.mainloop()