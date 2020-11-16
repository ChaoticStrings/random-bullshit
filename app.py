from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import *

window = tk.Tk()

frameMenu = Frame(window, bg = 'blue')
frameFertilidade = Frame(window)

window.geometry('900x700')
frameFertilidade.columnconfigure([0, 1], weight = 1, minsize = 100)
frameFertilidade.rowconfigure([0, 1, 2], weight = 1, minsize = 100)

textFertilidadeVar = tk.StringVar()
textFertilidadeVar.set('''
                        Tanto a fertilidade feminina como a masculina são afetadas\n
                        pela idade. Como a mulher nasce com todos os seus ovócitos\n 
                        e não serão produzidos mais ao longo da sua vida, com a idade\n
                        o número de folículos primordiais disponíveis nos ovários\n
                        diminuiu para um nível em que a conceção se torna mais\n
                        improvável. Quando a mulher atinge a menopausa perde a sua\n
                        capacidade de conceber, pois, nessa altura, os ovários já\n
                        não contêm folículos capazes de se desenvolver e amadurecer.\n
                        Em relação aos homens, a grande maioria passa por uma redução\n
                        gradual da produção de testosterona e de espermatozoides à\n
                        medida que vai envelhecendo e verifica-se uma menor capacidade\n
                        de manter ereção para permitir a relação sexual. Também após\n
                        os 50 anos idade, existe um risco crescente de se gerarem\n
                        deficiências cromossómicas.
                        ''')

def raise_frame(frame):
    frame.tkraise() 

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
    canvas.draw()

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
    canvas.draw()

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
    canvas.draw()

fig = Figure(figsize = (5, 5), dpi = 80)
plotf = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master = frameFertilidade)
canvas.draw()
canvas.get_tk_widget().grid(row = 0, column = 0)

textFertilidade = Label(frameFertilidade, textvariable = textFertilidadeVar, justify = CENTER, wraplength = 0)

btnFertilidadeMulher = tk.Button(master = frameFertilidade, text = 'Mulher', height = 5, width = 30, command = grafFertilidadeMulher)
btnFertilidadeAmbos = tk.Button(frameFertilidade, text = 'Ambos', height = 5, width = 30, command = grafFertilidadeAmbos)
btnFertilidadeHomem = tk.Button(frameFertilidade, text = 'Homem', height = 5, width = 30, command = grafFertilidadeHomem)
btnCloseFertilidade = tk.Button(frameFertilidade, text = 'Voltar', height = 5, width = 30, command = raise_frame(frameMenu))
btnFertilidade = tk.Button(frameMenu, text = 'Fertilidade\nRelativa', heigh = 5, width = 30, command = raise_frame(frameFertilidade))

textFertilidade.grid(row = 0, column = 1)

btnFertilidadeMulher.grid(row = 1, column = 0)
btnFertilidadeAmbos.grid(row = 2, column = 0)
btnFertilidadeHomem.grid(row = 1, column = 1)
btnCloseFertilidade.grid(row = 2, column = 1)
btnFertilidade.grid(row = 1, column = 1)

frameFertilidade.grid()
frameMenu.grid()

window.title('Menu')
window.mainloop()
