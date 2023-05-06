#Programa que recibe como entrada el peso de una sandía y muestra si se puede partir en números pares
kilos = int(input(''))
if kilos == 2 or kilos == 1 or kilos == 0:
    print('NO')
else:
    if kilos % 2 == 0:
        print('SI')
    else:
        print('NO')
# mitad = kilos/2
# lmitad = 0
# if kilos % 2 != 0:
#     print('NO')
# else:
#     for i in range(kilos):
#         lmitad += mitad - i
#         rmitad += mitad + i 
#         if lmitad + rmitad == kilos and lmitad % 2 == 0 and rmitad % 2 == 0 and lmitad != 0 and rmitad !=0:
#             print('SI')
#             break