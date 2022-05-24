from tkinter import *

#grid 4x4
# 7 8 9 +
# 4 5 6 -
# 1 2 3 *
# 0 C = /

#por enquanto, simples, 1 e 2, + e -  

expression = ""

def som():
    global expression
    expression = expression + "+"
    total["text"] = expression

def dim():
    global expression
    expression = expression + "-"
    total["text"] = expression

def um():
    global expression
    expression = expression + "1"
    total["text"] = expression

def dois():
    global expression
    expression = expression + "2"
    total["text"] = expression

def tres():
    global expression
    expression = expression + "3"
    total["text"] = expression

def quatro():
    global expression
    expression = expression + "4"
    total["text"] = expression

def cinco():
    global expression
    expression = expression + "5"
    total["text"] = expression

def seis():
    global expression
    expression = expression + "6"
    total["text"] = expression

def sete():
    global expression
    expression = expression + "7"
    total["text"] = expression

def oito():
    global expression
    expression = expression + "8"
    total["text"] = expression

def nove():
    global expression
    expression = expression + "9"
    total["text"] = expression

def zero():
    global expression
    expression = expression + "0"
    total["text"] = expression

def clear():
    global expression
    expression = ""
    total["text"] = expression

janela = Tk()
janela.geometry("300x500")
janela.resizable(False, False)
janela.title("Calculadora")

total = Label(janela, text="")
total.grid(column=1, row= 0)

somar = Button(janela, text="+", command=som, height=1, width=7)
somar.grid(column=0, row=1)

diminuir = Button(janela, text="-", command=dim, height=1, width=7)
diminuir.grid(column=0, row=2)

limpa = Button(janela, text="C", command=clear, height=1, width=7)
limpa.grid(column=0, row=3)

#enter = Button(janela, text="=", command=ent)

#multiplicar = Button(janela, text="*", command=mul)
#divisão = Button(janela, text="/", command=div)

numero1 = Button(janela, text="1", command=um, height=1, width=7)
numero1.grid(column=1, row=1)
numero2 = Button(janela, text="2", command=dois, height=1, width=7)
numero2.grid(column=1, row=2)
numero3 = Button(janela, text="3", command=tres, height=1, width=7)
numero3.grid(column=1, row=3)
numero4 = Button(janela, text="4", command=quatro, height=1, width=7)
numero4.grid(column=2, row=1)
numero5 = Button(janela, text="5", command=cinco, height=1, width=7)
numero5.grid(column=2, row=2)
numero6 = Button(janela, text="6", command=seis, height=1, width=7)
numero6.grid(column=2, row=3)
numero7 = Button(janela, text="7", command=sete, height=1, width=7)
numero7.grid(column=3, row=1)
numero8 = Button(janela, text="8", command=oito, height=1, width=7)
numero8.grid(column=3, row=2)
numero9 = Button(janela, text="9", command=nove, height=1, width=7)
numero9.grid(column=3, row=3)
numero0 = Button(janela, text="0", command=zero, height=1, width=7)
numero0.grid(column=3, row=4)

janela.mainloop()