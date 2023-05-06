# Mata Prieto Varush 2020640317

# Se tiene una aseguradora que lleva el control de los seguros que se van vendiendo. Las
# acciones son:
# 1. Agregar Seguro
# – El seguro puede ser de dos tipos (usar herencia), puede ser un Seguro de Vida
# o un Seguro de Auto (usar encapsulamiento)
# 2. Obtener total de montos asegurados
# 3. Obtener total de ingresos mensuales
# 4. Imprimir seguros
opc=0
class Seguro:
    tipoCovertura=''
    montoPagoMensual=''
    montoAsegurado=0

    def __init__(self,montoAsegurado):
        self.montoAsegurado=montoAsegurado
    def solicitar(self):
        self.montoAsegurado=int(input('Ingrese el monto asegurado: '))
        self.tipoCovertura=input('Ingrese el tipo de cobertura: ')
    def imprimir(self):
        print('El tipo de cobertura es: ',self.tipoCovertura)
        print('El monto asegurado es: ',self.montoAsegurado)
        print('El monto de pago mensual es: ',self.montoPagoMensual)

class SeguroDeVida(Seguro):
    _edad = ''
    _nombreAsegurado = ''
    def __init__(self,montoAsegurado):
        Seguro.__init__(self, montoAsegurado)
    @property
    def nombreAsegurado(self):
        return self._nombreAsegurado
    @property
    def edad(self):
        return self._edad
    @nombreAsegurado.setter
    def nombreAsegurado(self,nombreAsegurado):
        self._nombreAsegurado=nombreAsegurado
    @edad.setter
    def edad(self,edad):
        self._edad=edad
    def solicitar(self):
        Seguro.solicitar(self)
        self._edad=int(input('Ingrese la edad: '))
        self._nombreAsegurado=input('Ingrese el nombre del asegurado: ')
    def imprimir(self):
        Seguro.imprimir(self)
        return print('El nombre es: ',self._nombreAsegurado,' la edad del asegurado es: ',self._edad)
    def calcularPagoMensual(self):
        if(self._edad<60):
            self.montoPagoMensual=self.montoAsegurado*0.005
        else:
            self.montoPagoMensual=self.montoAsegurado*0.02
    
class SeguroAutomovil(Seguro):
    modelo=''
    marca=''
    color=''

    def solicitar(self):
        Seguro.solicitar(self)
        self.modelo=int(input('Ingrese el modelo del automovil: '))
        self.marca=input('Ingrese la marca: ')
        self.color=input('Ingrese el color: ')
        
    def imprimir(self):
        Seguro.imprimir(self)
        return print('El modelo es: ',self.modelo,' La marca es: ',self.marca ,' El color es: ',self.color)
    def calcularPagoMensual(self):
        if(self.modelo<=2004):
            self.montoPagoMensual=(self.montoAsegurado*0.03)/12
        else:
            self.montoPagoMensual=(self.montoAsegurado*0.04)/12

def hacerImpresion(obj_seguro):
    obj_seguro.imprimir()
def hacerSolicitud(obj_seguro):
    obj_seguro.solicitar()
def calcPagoM(obj_seguro):
    obj_seguro.calcularPagoMensual()
u=0
n=0.00
m=0.00
print('Bienvenid@ a la compania de seguros.')      
lista=[]
while(opc != 5):
    opc=int(input("Seleccione el numero de lo que requiere: 1.-Agregar seguro, 2.-Obtener total de montos asegurados, 3.-Obtener el total de ingresos mensuales. 4.-Imprimir los seguros, 5.-Salir: "))
    if(opc == 1):
        u = int(input('Ingrese 1 si es un seguro de vida y 2 si es un seguro de automovil: '))
        if(u == 1):
            persona = SeguroDeVida(360000)
            hacerSolicitud(persona)
            calcPagoM(persona)
            lista.append(persona)
        else:
            carro=SeguroAutomovil(360000)
            hacerSolicitud(carro)
            calcPagoM(carro)
            lista.append(carro)
    elif(opc == 2):
        for i in lista:
            n += i.montoAsegurado
        print('La suma de los montos asegurados es: ',n)
    elif(opc == 3):
        for i in lista:
            m += i.montoPagoMensual
        print('El total de ingresos mensuales es: ',m)
    elif(opc == 4):
        for i in lista:
            hacerImpresion(i)
    elif(opc == 5):
        print('Hasta la proxima.')
    else:
        print('Por favor seleccione una opci�n correcta.')