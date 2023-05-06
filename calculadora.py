import tkinter as tk

class aplication:
    def __init__(self):
        self.exp = ""
        self.valor = 1
        self.ventana1 = tk.Tk()
        self.ventana1.title("Calculadora")

        self.label1 = tk.Label(self.ventana1, text= "Calculadora")
        self.label1.grid(column = 0, row = 0)

        self.dato = tk.StringVar()

        self.entry1 = tk.Entry(self.ventana1, width = 10, textvariable = self.dato, state="readonly")
        self.entry1.grid(column=0,row=1)
    
        self.boton7 = tk.Button(self.ventana1, text = "7", command=lambda:self.press("7"))
        self.boton7.grid(column=1, row = 3)

        self.boton8 = tk.Button(self.ventana1, text = "8", command=lambda:self.press("8"))
        self.boton8.grid(column=2, row = 3)

        self.boton9 = tk.Button(self.ventana1, text = "9", command=lambda:self.press("9"))
        self.boton9.grid(column=3, row = 3)

        self.boton4 = tk.Button(self.ventana1, text = "4", command=lambda:self.press("4"))
        self.boton4.grid(column=1, row = 4)

        self.boton5 = tk.Button(self.ventana1, text = "5", command=lambda:self.press("5")) 
        self.boton5.grid(column=2, row = 4)

        self.boton6 = tk.Button(self.ventana1, text = "6", command=lambda:self.press("6"))
        self.boton6.grid(column=3, row = 4)

        self.boton1 = tk.Button(self.ventana1, text = "1", command=lambda:self.press("1"))
        self.boton1.grid(column=1, row = 5)

        self.boton2 = tk.Button(self.ventana1, text = "2", command=lambda:self.press("2"))
        self.boton2.grid(column=2, row = 5)

        self.boton3 = tk.Button(self.ventana1, text = "3", command=lambda:self.press("3"))
        self.boton3.grid(column=3, row = 5)

        self.boton0 = tk.Button(self.ventana1, text = "0", command=lambda:self.press("0"))
        self.boton0.grid(column=2, row = 6)

        self.suma = tk.Button(self.ventana1, text = "+", command=lambda: self.press("+"))
        self.suma.grid(column=4, row = 3)

        self.resta = tk.Button(self.ventana1, text = "-", command=lambda: self.press("-"))
        self.resta.grid(column=4, row = 4)

        self.multi = tk.Button(self.ventana1, text = "x", command=lambda: self.press("*"))
        self.multi.grid(column=4, row = 5)

        self.divi = tk.Button(self.ventana1, text = "/", command=lambda: self.press("/"))
        self.divi.grid(column=5, row = 3)

        self.borra = tk.Button(self.ventana1, text = "AC", command = self.clear)
        self.borra.grid(column=5, row = 4)

        self.igual = tk.Button(self.ventana1, text = "=", command = self.equalpress)
        self.igual.grid(column=5, row = 5)

        self.ventana1.mainloop()


    def press(self,num):
        self.exp += str(num)
        self.dato.set(self.exp)

    def equalpress(self):
        try:
            total = str(eval(self.exp))
            self.dato.set(total)
            self.exp = ""
        except:
            self.dato.set('Error')
            self.exp = ""

    def clear(self):
        self.exp = ""
        self.dato.set("")


aplicacion1 = aplication()


