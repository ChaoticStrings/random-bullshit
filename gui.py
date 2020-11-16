from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk 
from tkinter import ttk 

fig = Figure(figsize = (5, 5), dpi = 80)
plotf = fig.add_subplot(111)

def grafFertilidadeMulher():
    fig.clear()
    plotf = fig.add_subplot(111)

    idadeM = [18,22,27,32,37,42,47,67,87,99]
    fertilidadeRelativaM = [0.84,1,0.96,0.9,0.8,0.48,0.1,0.08,0.05,0.01]

    plotf.plot(idadeM, fertilidadeRelativaM, linewidth='4', color='pink', marker='o', markerfacecolor='purple', markersize='8')
    plotf.set_ylim(0,1.2)
    plotf.set_xlim(17,100)
    plotf.set_xlabel('idade')
    plotf.set_ylabel('fertilidade relativa')
    plotf.set_title('Perda de fertilidade com a idade')
    
    canvas = FigureCanvasTkAgg(master = container)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0)

def grafFertilidadeHomem():
    fig.clear()
    plotf = fig.add_subplot(111)

    idadeH = [19,20,30,40,50,60,70,80,90,99]
    fertilidadeRelativaH = [0.92,1,1,1,0.95,0.81,0.6,0.4,0.4,0.4]

    plotf.plot(idadeH, fertilidadeRelativaH, linewidth = '4', color = 'cyan', marker = 'o', markerfacecolor = 'blue', markersize = '8')
    plotf.set_ylim(0,1.2)
    plotf.set_xlim(17,100)
    plotf.set_xlabel('idade')
    plotf.set_ylabel('fertilidade relativa')
    plotf.set_title('Perda de fertilidade com a idade')
    
    canvas = FigureCanvasTkAgg(fig, master = container)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0)

def grafFertilidadeAmbos():
    fig.clear()
    plotf = fig.add_subplot(111)

    idadeM = [18,22,27,32,37,42,47,67,87,99]
    fertilidadeRelativaM = [0.84,1,0.96,0.9,0.8,0.48,0.1,0.08,0.05,0.01]
    idadeH = [19,20,30,40,50,60,70,80,90,99]
    fertilidadeRelativaH = [0.92,1,1,1,0.95,0.81,0.6,0.4,0.4,0.4]

    plotf.plot(idadeM, fertilidadeRelativaM, linewidth='4', color='pink', marker='o', markerfacecolor = 'purple', markersize='8')
    plotf.plot(idadeH, fertilidadeRelativaH, linewidth = '4', color = 'cyan', marker = 'o', markerfacecolor = 'blue', markersize = '8')
    plotf.set_ylim(0,1.2)
    plotf.set_xlim(17,100)
    plotf.set_xlabel('idade')
    plotf.set_ylabel('fertilidade relativa')
    plotf.set_title('Perda de fertilidade com a idade')
   
    canvas = FigureCanvasTkAgg(fig, master = container)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0)


class tkinterApp(tk.Tk): 

    def __init__(self, *args, **kwargs):  

        tk.Tk.__init__(self, *args, **kwargs) 

        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
        self.geometry("800x800")
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 

        self.frames = {}   

        for F in (Menu, fertilidadeRelativa): 
   
            frame = F(container, self) 

            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(Menu) 

    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 

class Menu(tk.Frame): 

    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 

        label = ttk.Label(self, text ="Menu") 

        label.grid(row = 0, column = 4, padx = 10, pady = 10)  
   
        button1 = ttk.Button(self, text ="Fertilidade\nRelativa", 
        command = lambda : controller.show_frame(fertilidadeRelativa)) 

        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 

class fertilidadeRelativa(tk.Frame): 
      
    def __init__(self, parent, controller): 
          
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Fertilidade\nRelativa") 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        button1 = ttk.Button(self, text ="Mulher", 
                            command = lambda : grafFertilidadeMulher) 
 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Homem", 
                            command = lambda : grafFertilidadeHomem) 

        button2.grid(row = 1, column = 2, padx = 10, pady = 10) 
 
        button3 = ttk.Button(self, text ="Ambos", 
                            command = lambda : grafFertilidadeAmbos) 

        button3.grid(row = 2, column = 1, padx = 10, pady = 10) 

        button4 = ttk.Button(self, text ="Voltar", 
                            command = lambda : controller.show_frame(Menu)) 

        button4.grid(row = 2, column = 2, padx = 10, pady = 10) 

app = tkinterApp() 
app.mainloop() 