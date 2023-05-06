# Mata Prieto Varush 2020640317
# El costo de envíos nacionales de paquetería depende de varios factores. Suponga que se requiere un
# programa que permita cotizar envíos dependiendo de dos factores: el peso físico/cúbico y si es local o
# nacional.
# El peso que se considera de un paquete es el mayor del peso físico y del peso cúbico. El peso físico
# corresponde al peso en kg del paquete. Mientras que el peso cúbico se obtiene al multiplicar el largo,
# ancho y alto del paquete y lo divide por 6000; por ejemplo, si hay un paquete con peso físico de 11kg y
# unas dimensiones de 40 cm de largo, 35 de ancho y 50 de alto, el cálculo sería: 40x35x50/6000=11.66, de
# tal forma que en este caso el costo del envío se calcularía sobre 11.66 en lugar de los 11kg.
# Para paquetes de 20gr a 1kg (ya sean de peso físico o cúbico), el costo por kilo local es de $8.03 y por kilo
# nacional de $24.24.
# Para paquetes de 1kg a 25kg (ya sean de peso físico o cúbico), el costo por kilo local es de $5.32 y nacional
# de $18.92.
class Paqueteria:

    dim1=''
    dim2=''
    dim3=''

    def __init__(self, pesoF):
        self.pesoF=pesoF

    def pesoCubico(self):
        pesoCub=(self.dim1*self.dim2*self.dim3)/6000
        print('Las dimensiones son: ',self.dim1,self.dim2,self.dim3 )
        print('El peso cubico del paquete es: ',pesoCub)

    def costoEnvio(self,destino):
        if (destino=='local' and self.pesoF>=20 and self.pesoF<=1000):
            n=(self.pesoF*8.03)/1000

        elif(destino=='local' and self.pesoF>1000 and self.pesoF<=25000):
            n=(self.pesoF*5.32)/1000

        elif(destino=='nacional'and self.pesoF>=20 and self.pesoF<=1000):
            n=(self.pesoF*24.24)/1000

        elif(destino=='nacional' and self.pesoF>1000 and self.pesoF<=25000):
            n=(self.pesoF*18.92)/1000

        return print('El costo de envio sera de $',n) 


print('Bienvenido a la paqueteria.')
paqueteA=Paqueteria(int(input('Ingrese el peso del paquete en gramos (de 20 hasta 25000): ')))
paqueteA.dim1=int(input('Ingrese las dimensiones del paquete (alto, largo y ancho) '))
paqueteA.dim2=int(input(' '))
paqueteA.dim3=int(input(' '))
pesoCubico=paqueteA.pesoCubico()
Envio=paqueteA.costoEnvio(input('Sera envio local o nacional? '))
print('Gracias por usar el servicio de paqueteria.')
