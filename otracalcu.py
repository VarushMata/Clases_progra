#06/05/2023 Calculadora con interfaz gráfica
import tkinter as tk #Librería para interfaz gráfica

class aplication:
    def __init__(self):
        self.exp = "" #Variable que almacenarán los datos introducidos por los botones
        self.valor = 1
        self.ventana1 = tk.Tk()
        self.ventana1.title("Calculadora")

        self.label1 = tk.Label(self.ventana1, text= "Calculadora")
        self.label1.grid(column = 0, row = 0)

        self.dato = tk.StringVar() #Variable de texto para mostrar el resultado y los datos introducidos

        #Cuadro de texto que mustra los datos presionados así como el resultado, gracias al el state readonly no se puede modificar 
        self.entry1 = tk.Entry(self.ventana1, textvariable = self.dato, font = ("Verdana", 15 ), bd = 12,
                    insertwidth = 4, width = 14, justify = 'right', state="readonly")
        self.entry1.grid(columnspan=6) #Ajusta la barra para quedar centrada

        for idx, digit in enumerate("123456789.0+-*/"): #Ciclo for para crear botones con el texto "enumerate" que cumplen el mismo comando
            cmd = lambda arg=digit: self.press(arg)
            btn = tk.Button(self.ventana1, text=digit, command=cmd, bg="gainsboro",
                 bd=3, padx=12, pady=5, font=('Helvetica', 14,'bold'))
            btn.grid(row = 2 + idx // 3, column = idx % 3)

        #Los dos botones restantes son para ejecutar los métodos de limpiar y de hacer la operación
        self.borra = tk.Button(self.ventana1, text = "C", command = self.clear, bg="gainsboro",
                 bd=3, padx=12, pady=5, font=('Helvetica', 14,'bold'))
        self.borra.grid(column=5, row = 2)

        self.igual = tk.Button(self.ventana1, text = "=", command = self.equalpress, bg="gainsboro",
                 bd=3, padx=12, pady=5, font=('Helvetica', 14,'bold'))
        self.igual.grid(column=5, row = 3)

        self.ventana1.mainloop()

    #Método que almacena los datos presionados por los botones
    def press(self,num):
        self.exp += str(num)
        self.dato.set(self.exp)

    #Método para evaluar lo introducido
    def equalpress(self):
        try:
            total = str(eval(self.exp)) #eval("") hace la operación de una string como si fueran números
            self.dato.set(total)
            self.exp = ""
        except:
            self.dato.set('Error') #Si no arroja nada entonces se manda el texto de "Error"
            self.exp = ""

    #Método para borrar la selección
    def clear(self): 
        self.exp = ""
        self.dato.set("")

#Inicialización de la interfaz
calcuchida = aplication()


