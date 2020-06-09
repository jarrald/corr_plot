import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
from random import randrange
import pandas as pd
import scipy.stats

class Cor2:

    """Deals with correlation of 2 observations or groups thereof"""
    def __init__(self, vx, vy):
        self.vx = pd.Series(vx)
        self.vy = pd.Series(vy)

    def draw(self, color="red"):
        self.window = tk.Tk()
        self.window.title = "Correlation graph"
        
        self.container = ttk.Frame(self.window)
        self.container.pack(side="top", fill="both", expand = True)
        
        self.menuframe = ttk.Frame(self.container)
        self.menuframe.pack(side="left", fill="both", expand = True)
        
        self.plotframe = ttk.Frame(self.container)
        self.plotframe.pack(side="right", fill="both", expand = True)

        self.leftlabel = ttk.Label(self.menuframe, text="something1")
        self.leftlabel.pack(padx=10,pady=10)


        self.f = Figure(figsize=(5,5), dpi=100)
        a = self.f.add_subplot()
        a.scatter(self.vx, self.vy, alpha=.5, label="label")
        self.regre = scipy.stats.linregress(self.vx, self.vy)

        b = self.f.add_subplot()
        b.plot(self.vx, self.regre.intercept + self.regre.slope * self.vx, color='green')
        self.canvas = FigureCanvasTkAgg(self.f, self.container)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.window.mainloop()
    def getCorr(self):
        return (self.vx.corr(self.vy))*100
c = Cor2([4,5,7,9,11,13,15,18],[5,7,9,10,12,14,15,20])
print(c.getCorr())
c.draw()