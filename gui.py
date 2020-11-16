import tkinter as tk 
from tkinter import ttk 
   
class tkinterApp(tk.Tk): 

    def __init__(self, *args, **kwargs):  

        tk.Tk.__init__(self, *args, **kwargs) 

        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 

        self.frames = {}   

        for F in (Menu, fertilidadeRelativa, idk): 
   
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

        button2 = ttk.Button(self, text ="idk", 
        command = lambda : controller.show_frame(idk)) 
 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 

class fertilidadeRelativa(tk.Frame): 
      
    def __init__(self, parent, controller): 
          
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Fertilidade\nRelativa") 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        button1 = ttk.Button(self, text ="Menu", 
                            command = lambda : controller.show_frame(Menu)) 
 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
 
        button2 = ttk.Button(self, text ="idk", 
                            command = lambda : controller.show_frame(idk)) 

        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
class idk(tk.Frame):  
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="idk") 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        button1 = ttk.Button(self, text ="Fertilidade\nRelativa", 
                            command = lambda : controller.show_frame(fertilidadeRelativa)) 

        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 

        button2 = ttk.Button(self, text ="Menu", 
                            command = lambda : controller.show_frame(Menu)) 

        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 

app = tkinterApp() 
app.mainloop() 