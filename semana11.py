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
    salida=list[int]=[]
    for i in plastico: #toma el string y recorre cada una de las letras y las guarda en una variable llamada i
        try:
            n=int(i)
            salida.append(n)
        except:
            pass

    return salida



if __name__=="__main__":
    #x:int=leer_entero("digite un numero: ")
    #print(x)
    print(limpiar_convertir_lista("4444-5555-7890-1234"))