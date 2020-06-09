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
    """
    Helper to show a plot with choosen values, it's regression & their placements
    Deals with correlation of 2 observations or groups thereof
    """
    def __init__(self, vx, vy):
        """initializes the correlation class
                Args:
            vx (iterable): values on x-axis
            vy (iterable): values on y-axis
        >>> c = Cor2([4,5,7,9,11,13,15,18],[5,7,9,10,12,14,15,20])

        """        
        self.vx = pd.Series(vx)
        self.vy = pd.Series(vy)

    def draw(self, color="red"):
        """Creates a window gui for the user to see the data
                Args:
            color (string, optional): color of the dots shown. Defaults to "red".
        >>> c = Cor2([4,5,7,9,11,13,15,18],[5,7,9,10,12,14,15,20])
        >>> c.draw()
        ...
        """        
        self.window = tk.Tk()
        self.window.title = "Correlation graph"
        
        self.container = ttk.Frame(self.window)
        self.container.pack(side="top", fill="both", expand = True)
        
        self.menuframe = ttk.Frame(self.container)
        self.menuframe.pack(side="left", fill="both", expand = True)
        
        self.plotframe = ttk.Frame(self.container)
        self.plotframe.pack(side="right", fill="both", expand = True)

        self.leftlabel = ttk.Label(self.menuframe, text="Settings")
        self.leftlabel.pack(side="top", padx=10,pady=10)


        self.f = Figure(figsize=(5,5), dpi=100)
        a = self.f.add_subplot()
        a.scatter(self.vx, self.vy, alpha=.5, label="label")
        self.regre = scipy.stats.linregress(self.vx, self.vy)

        self.regressionButton = ttk.Button(self.menuframe, text="Show regression", command = lambda :self.showRegression())
        self.regressionButton.pack()

        self.canvas = FigureCanvasTkAgg(self.f, self.container)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.window.mainloop()
    def getCorr(self):
        """Calculates the correlation by using pandas
            Returns:
                float: from 0 to 1 where 1 means they're most likely correlated
        >>> c = Cor2([4,5,7,9,11,13,15,18],[5,7,9,10,12,14,15,20])
        >>> c.getCorr()
        0.9896952582371691
        """        
        return (self.vx.corr(self.vy))
    def showRegression(self):
        b = self.f.add_subplot()
        b.plot(self.vx, self.regre.intercept + self.regre.slope * self.vx, color='green')
        self.canvas.draw()

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)