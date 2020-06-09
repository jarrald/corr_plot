import tkinter as tk
from random import Random, random, randrange
from tkinter import ttk
import random

import matplotlib
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

matplotlib.use("TkAgg")



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
        container.pack(side="left", fill="both", expand = True)
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
        label.pack(pady=10,padx=10, side=tk.LEFT)
        self.figframe = tk.Frame(self)
        self.figframe.pack()

        self.values = []

        button1 = ttk.Button(self, text="Add random obs", command=lambda: self.addObservations(random.choice(["sugar", "bean", "peanuts", "dew", "apple"]),[randrange(1,23,1) for i in range(8)],[randrange(1,23,1) for i in range(8)],color=random.choice(['green', 'red', 'blue', 'yellow', 'black', 'orange', 'grey'])))
        button1.pack()

        self.addObservations("coffee",[randrange(1,23,1) for i in range(8)],[randrange(1,23,1) for i in range(8)],color=random.choice(['green', 'red', 'blue', 'yellow', 'black', 'orange', 'grey']))
        

    def addvaluesandlabel(self, label, x , y):
        self.values.append((label, x, y))

    def addObservations(self, name, x, y, color="red", alpha=0.5):
        self.figframe.pack_forget()
        self.figframe.destroy()
        self.figframe = tk.Frame(self)
        self.figframe.pack()

        self.f = Figure(figsize=(5,5), dpi=100)
        self.values.append((name, x, y, color, alpha))
        for row in self.values:
            a = self.f.add_subplot(1,1,1)
            rowname, x, y, color, alpha = row
            a.scatter(x, y, alpha=alpha, color=color, edgecolors='none', s=30, label=rowname)
            self.f.legend(rowname)
        canvas = FigureCanvasTkAgg(self.f, self.figframe)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self.figframe)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        print(self.values)

        

app = CorrPlot()
app.mainloop()
