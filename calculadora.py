from tkinter import *
#variaveis globais
num1 = int()
num2 = int()
res = 0
operation = ""
expression = ""
#funçoes de operadores
def som():
    global num1, expression, operation
    if expression == "": #se a expressão for vazia os operadores não funcionam
        pass
    else:
        num1 = int(expression)
        print(num1) #todos os prints são pra feedback no terminal apenas
        expression = "" #limpa a expressão após a operação
        operation = "add"
        total["text"] = expression

def dim():
    global num1, expression, operation
    if expression == "": #see line 12
        pass
    else:
        num1 = int(expression)
        print(num1)
        expression = ""
        operation = "sub"
        total["text"] = expression

def mul():
    global num1, expression, operation
    if expression == "": #see line 12
        pass
    else:
        num1 = int(expression)
        print(num1)
        expression = ""
        operation = "mul"
        total["text"] = expression

def div():
    global num1, expression, operation
    if expression == "": #see line 12
        pass
    else:
        num1 = int(expression)
        print(num1)
        expression = ""
        operation = "div"
        total["text"] = expression

def clear(): 
    global num1, num2, expression
    num1 = 0
    num2 = 0
    expression = ""
    total["text"] = expression

def equals():
    global num1, num2, res, expression, operation
    if num1 != 0: #o igual só funciona se o num1 já existir (ou seja, se uma operação já estiver sido selecionada...)
        if expression != "": #...e pra evitar o "['340 + ='] -> erro", ele checa a expressão
            num2 = int(expression)
            print(num2)
            if operation == "add":
                res = int(num1) + int(num2)
                print(res) #feedback no terminal
                expression = "" #reseta a expressão (visualmente) pra proxima operação
                num1 = res #atualiza o valor do numero1 para a proxima operação
                total["text"] = res 
            if operation == "sub":
                res = int(num1) - int(num2)
                print(res)
                expression = ""
                num1 = res
                total["text"] = res
            if operation == "mul":
                res = int(num1) * int(num2)
                print(res)
                expression = ""
                num1 = res
                total["text"] = res
            if operation == "div":
                res = int(num1) / int(num2)
                print(res)
                expression = ""
                num1 = res
                total["text"] = res
        else:
            pass
    else:
        pass
#funções de números
def um():
    global expression
    expression += "1"
    total["text"] = expression

def dois():
    global expression
    expression += "2"
    total["text"] = expression

def tres():
    global expression
    expression += "3"
    total["text"] = expression

def quatro():
    global expression
    expression += "4"
    total["text"] = expression

def cinco():
    global expression
    expression += "5"
    total["text"] = expression

def seis():
    global expression
    expression += "6"
    total["text"] = expression

def sete():
    global expression
    expression += "7"
    total["text"] = expression

def oito():
    global expression
    expression += "8"
    total["text"] = expression

def nove():
    global expression
    expression += "9"
    total["text"] = expression

def zero():
    global expression
    expression += "0"
    total["text"] = expression

while True: #isso aqui é uma aberração (o uso do while loop)
    janela = Tk()
    janela.geometry("300x500")
    janela.resizable(False, False)
    janela.title("Calculadora")

    total = Label(janela, text="", height=1, width=24)
    total.grid(columnspan=4, row=0)
#operadores
    somar = Button(janela, text="+", command=som, height=1, width=7)
    somar.grid(column=3, row=1)

    diminuir = Button(janela, text="-", command=dim, height=1, width=7)
    diminuir.grid(column=3, row=2)

    multiplicar = Button(janela, text="*", command=mul, height=1, width=7)
    multiplicar.grid(column=3, row=3)

    divisão = Button(janela, text="/", command=div, height=1, width=7)
    divisão.grid(column=3, row=4)

    limpa = Button(janela, text="C", command=clear, height=1, width=7)
    limpa.grid(column=2, row=4)

    igual = Button(janela, text="=", command=equals, height=1, width=7)
    igual.grid(column=3, row=5)
#numeros
    numero1 = Button(janela, text="1", command=um, height=1, width=7)
    numero1.grid(column=0, row=3)
    numero2 = Button(janela, text="2", command=dois, height=1, width=7)
    numero2.grid(column=1, row=3)
    numero3 = Button(janela, text="3", command=tres, height=1, width=7)
    numero3.grid(column=2, row=3)
    numero4 = Button(janela, text="4", command=quatro, height=1, width=7)
    numero4.grid(column=0, row=2)
    numero5 = Button(janela, text="5", command=cinco, height=1, width=7)
    numero5.grid(column=1, row=2)
    numero6 = Button(janela, text="6", command=seis, height=1, width=7)
    numero6.grid(column=2, row=2)
    numero7 = Button(janela, text="7", command=sete, height=1, width=7)
    numero7.grid(column=0, row=1)
    numero8 = Button(janela, text="8", command=oito, height=1, width=7)
    numero8.grid(column=1, row=1)
    numero9 = Button(janela, text="9", command=nove, height=1, width=7)
    numero9.grid(column=2, row=1)
    numero0 = Button(janela, text="0", command=zero, height=1, width=14)
    numero0.grid(column=0, columnspan=2, row=4)

    janela.mainloop()