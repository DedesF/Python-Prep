class calcular:
    def __init__(self):
        pass   

    def primoslist(lista):
        for elemento in lista:
            primo = True
            if (elemento <= 1):
                primo = False
                print('El número', elemento, 'no es primo')
                
            else:                
                for y in range(2, elemento):
                    if (elemento%y == 0):
                        primo = False
                if (primo == True):
                    print('El número', elemento, 'es primo')
                else:
                    print('El número', elemento, 'no es primo')
    
    def convertirlist(lista, origen, destino):
        for valor in lista:
            if (origen == 'celsius'):
                if (destino == 'celsius'):
                    print(valor,'grados celcius son', valor, 'grados celsius')
                elif (destino == 'farenheit'):
                    print(valor,'grados celcius son',(valor * 9 / 5) + 32, 'grados farenheit')
                elif (destino == 'kelvin'):
                    print(valor,'grados celcius son',valor + 273.15, 'grados kelvin')
            elif (origen == 'farenheit'):
                if (destino == 'celsius'):
                    print(valor,'grados farenheit son',(valor - 32) * 5 / 9, 'grados celsius')
                elif (destino == 'farenheit'):
                    print(valor,'grados farenheit son',valor, 'grados farenheit')
                elif (destino == 'kelvin'):
                    print(valor,'grados farenheit son',((valor - 32) * 5 / 9) + 273.15, 'grados kelvin')
            elif (origen == 'kelvin'):
                if (destino == 'celsius'):
                    print(valor,'grados kelvin son',valor - 273.15, 'grados celcius')
                elif (destino == 'farenheit'):
                    print(valor,'grados kelvin son',((valor - 273.15) * 9 / 5) + 32, 'grados farenheit')
                elif (destino == 'kelvin'):
                    print(valor,'grados kelvin son',valor, 'grados kelvin')
            else:
                print(' El valor debe ser un número entero.\n',
                    'Origen y destino deben ser celsius, farenheit o kelvin')                
    
    def factoriallist(lista):
        for i, nro in enumerate(lista):
            if (type(nro) != int or nro < 0):
                print('Debe ingresar un número entero y mayor que 0')
                
            elif (lista[i] == 0):
                print('El factorial de 0 es 1')
                
            elif (nro > 1):                
                nro = nro * calcular.factorial(nro - 1)
                print('el factorial de', lista[i], 'es', nro)
        
    
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