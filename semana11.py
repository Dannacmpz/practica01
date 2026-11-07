def leer_entero(etiqueta:str)-> int:
    salida:int=0
    bandera:bool=True

    while bandera:
        try:
            salida= int(input(etiqueta))
            bandera=False
        except:
            print("Numero invalido, intente de nuevo")


    return salida

#recibe un string y devuelve una lista de enteros sin guiones
def limpiar_convertir_lista(plastico:str)->list [int]: #forma de quitar los guiones sin slicing
    salida:list[int]=[]
    for i in plastico: #toma el string y recorre cada una de las letras y las guarda en una variable llamada i
        try:
            n=int(i)
            salida.append(n)
        except:
            pass

    return salida

def invertir_lista(lista:list[int])-> list [int]:
    return lista[::-1]

def sumar_impares_simples(lista:list[int])->list [int]:
    return lista [::-1]

def ajustar (n:int) -> int:
    n=n*2
    if n>=9:
        n= n-9
    return n   

def sumar_pares_dobles(lista:list[int])->int:
    temp:list[int]= lista [::2]
    doble=[ ajustar(i) for i in temp   ]
    return sum(doble)


if __name__=="__main__":
    #x:int=leer_entero("digite un numero: ")
    #print(x)
    valores:list[int]=limpiar_convertir_lista("4455-6666-7890-1234")
    print(valores)
    valores_inv=invertir_lista(valores)
    print(valores_inv)
    print(sumar_impares_simples(valores_inv))
    print(sumar_pares_dobles(valores_inv))

  