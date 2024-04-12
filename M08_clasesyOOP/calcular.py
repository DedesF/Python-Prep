class calcular:
    def __init__(self):
        pass      
        # self.valores = valores        

    def primos(num):
        primo = True
        if (num <= 1):
            primo = False
        else:
            for y in range(2, num):
                if (num%y == 0):
                    primo = False
                    break
        return primo
    
    def moda(lista):
        unicos = []
        repeticiones = []
        maximo = 0

        for elemento in lista:
            if elemento not in unicos:
                unicos.append(elemento)

        for elemento in unicos:
            contador = 0
            for repetido in lista:
                if (elemento == repetido):
                    contador += 1
            repeticiones.append(contador)

        for i, elemento in enumerate(repeticiones):
            
            if (maximo < repeticiones[i]):
                maximo = repeticiones[i]
                repetido = unicos[i]
                
        return repetido, maximo
    
    def convertir(valor, origen, destino):
        resultado = 0
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                resultado = valor
            elif (destino == 'farenheit'):
                resultado = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                resultado = valor + 273.15
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                resultado = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                resultado = valor
            elif (destino == 'kelvin'):
                resultado = ((valor - 32) * 5 / 9) + 273.15
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                resultado = valor - 273.15
            elif (destino == 'farenheit'):
                resultado = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                resultado = valor
        else:
            print(' El valor debe ser un número entero.\n',
                'Origen y destino deben ser celsius, farenheit o kelvin')
            return None
        
        return resultado
    
    def factorial(nro):
        if (type(nro) != int or nro < 0):
            print('Debe ingresar un número entero y mayor que 0')
            return None
        if (nro > 1):
            nro = nro * calcular.factorial(nro - 1)
        return nro