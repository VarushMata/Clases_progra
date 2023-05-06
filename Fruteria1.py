# Mata Prieto Varush 2020640317
i=0
manzana={'Cantidad':18,'Vendidos': 0,'CostoP':496.98,'Costo':26.76}
uva={'Cantidad':16,'Vendidos': 0,'CostoP':509.92,'Costo':30.33}
mango={'Cantidad':30,'Vendidos': 0,'CostoP':369.9,'Costo':24.28}
zanahoria={'Cantidad':20,'Vendidos': 0,'CostoP':110,'Costo':9.81}
tomate={'Cantidad':13,'Vendidos': 0,'CostoP':219.96,'Costo':22.06}
print('Bienvenido a la frutería, estos son los precios por kg:')
print('Manzana: 26.76, en posesión: 18kg')
print('Uva: 30.33, en posesión: 16kg')
print('Mango: 24.28, en posesión: 30kg')
print('Zanahoria: 9.81, en posesión: 20kg')
print('Tomate: 22.06, en posesión: 13kg')
print('Seleccione la cantidad de kilogramos que va a comprar: ')
Compramzn=int(input('Kilogramos de manzana: '))
Comprauva=int(input('Kg de uvas: '))
Compraman=int(input('Kg de mango: ' ))
Comprazan=int(input('Kg de zanahoria: '))
Compratom=int(input('Kg de tomate: '))
manzana.update({'Cantidad':18-Compramzn}); manzana.update({'Vendidos':Compramzn})
uva.update({'Cantidad':16-Comprauva}); uva.update({"Vendidos":Comprauva})
mango.update({'Cantidad':30-Compraman}); mango.update({"Vendidos":Compraman})
zanahoria.update({'Cantidad':20-Comprazan}); zanahoria.update({"Vendidos":Comprazan})
tomate.update({'Cantidad':13-Compratom});  tomate.update({"Vendidos":Compratom})
print(manzana.values())
print(uva.values())
print(mango.values())
print(zanahoria.values())
print(tomate.values())
if(Compramzn>18 or Comprauva>16 or Compraman>30 or Comprazan>20 or Compratom>13):
    print("La cantidad de kilogramos que quiere es superior a la almcenada")
else:
    total={'Manzana':Compramzn*manzana.get('Costo'),'Uva':Comprauva*uva.get('Costo'),'Mango':Compraman*mango.get('Costo'),'Zanahoria':Comprazan*zanahoria.get('Costo'),'Tomates':Compratom*tomate.get('Costo')}
    print('Total: ')
    for k,v in total.items():
        print(k,v)
        i+=v
    print("Total a pagar: ", i)
    reporte={'Kg manzana vendidos: ':Compramzn,'Kg uva vendidos: ':Comprauva,'Kg mango vendidos: ':Compraman,'Kg zanahoria vendidos: ':Comprazan,'Kg tomate vendidos: ':Compratom}
    for k,v in reporte.items():
        print(k,v)
    CostoCompra=manzana.get('CostoP')+uva.get('CostoP')+mango.get('CostoP')+zanahoria.get('CostoP')+tomate.get('CostoP')
    Ganancia=i-CostoCompra
    print('La ganancia fue de: ', Ganancia)
