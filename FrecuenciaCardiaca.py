# Mata Prieto Varush 2020640317
# Monitorización de frecuencia cardiaca. El uso de monitores nos permite controlar las funciones vitales y
# complementan nuestra función, suponga se evaluará la frecuencia cardiaca que mide la cantidad de veces
# por minuto que el corazón se contrae o late. El programa permitirá ingresar datos del paciente, ingresar
# frecuencias cardiacas o analizar:
#  - Del paciente nos interesa saber edad, sexo y peso.
#  - En ingresar se requiere guardar las frecuencias cardiacas recopiladas (ingresadas por el usuario) en
#    una lista.
#  - Analizar despliega la medición que salió del rango normal y se determinará si el paciente muestra
#    más anomalías excediendo el máximo o por debajo del mínimo.

class FrecuenciaCardiaca:

    _numLatidos=''
    _hora=''
    _estado=''
    _peso=''
    _edad=''

    def __init__(self,genero):
        self.genero = genero

    @property
    def numLatidos(self):
        return self._numLatidos

    @numLatidos.setter
    def numLatidos(self,valor):
        self._numLatidos = valor

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,valor):
        self._edad = valor

    @property 
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self,peso):
        self._peso = peso

    @property
    def hora(self):
        return self._hora
    @hora.setter
    def hora(self,hora):
        self._hora=hora

    def ObtenerEstado(self,latidos):
        if(self.genero == 'Femenino'):
            FrecMax=(210-(0.5*self._edad)-(0.01*self._peso))
            if(latidos>=40 and latidos<=FrecMax):
                self._estado='Estado normal'

            elif(latidos<40):
                self._estado='Por debajo de la presion normal'

            else:
                self._estado='Por encima de la presion normal'

        elif(self.genero == 'Masculino'):
            FrecMax=(210-(0.5*self._edad)-(0.01*self._peso))+4
            if(latidos>=40 and latidos<=FrecMax):
                self._estado='Estado normal'

            elif(latidos<40):
                self._estado='Por debajo de la presion normal'

            else:
                self._estado='Por encima de la presion normal'

        print(self._estado)

Paciente = FrecuenciaCardiaca(input('Ingrese el genero. '))
Paciente._edad = int(input('Ingrese la edad: '))
Paciente._peso = int(input('Ingrese el peso: '))
Paciente._hora = int(input('Ingrese la hora en formato 24hrs: '))
lista=[]
c=0
u=0

while(c<5):
    Paciente.numLatidos = int(input('Ingrese el no. de latidos registrado: '))
    lista.append(Paciente._numLatidos)  
    c+=1
    
print('Edad: ', Paciente._edad)
print("Peso: ", Paciente._peso)
print('Hora: ', Paciente._hora)
x = 0

while(x<5):
   print(lista[x])
   Paciente.ObtenerEstado(lista[x])
   x += 1
