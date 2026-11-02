plastico1:str= "4444-5555-6666-7777"
plastico2:str= "4444555566667777"
plastico3:str= "4444-5555-6666-7"
plastico4:str= "4444-5555-6666-777a"
plastico5:str= "4444-5555-66"
plastico6:str= "7444-5555-6666-7777"

def validar_tarjeta_visa(plastico:str)->bool:
    salida:bool=False
    if plastico [0]=="4" and (len(plastico)==16 or len(plastico)==19):
        salida=True

    return salida