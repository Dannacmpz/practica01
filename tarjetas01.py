plastico1: str = "4444-5555-6666-7777"
plastico2: str = "4444555566667777"
plastico3: str = "4444-5555-6666-7"
plastico4: str = "4444-5555-6666-777a"
plastico5: str = "4444-5555-66"
plastico6: str = "7444-5555-6666-7777"


# si uno de los elementos, no es un numero perdimos
def son_numeros(plastico: str) -> bool:
    todos_son_numeros: bool = True

    for letra in plastico:
        if not es_numero(letra):
            salida = False
    return salida


# verificar que cada elemento es un numero
def es_numero(letra: str) -> bool:
    return (
        letra == "0"
        or letra == "1"
        or letra == "2"
        or letra == "3"
        or letra == "4"
        or letra == "5"
        or letra == "6"
        or letra == "7"
        or letra == "8"
        or letra == "9"
    )


def limpiar_plastico(plastico: str) -> str:
    return plastico[0:4] + plastico[5:9] + plastico[10:14] + plastico[15:19]


def validar_tarjeta_visa(plastico: str) -> bool:
    salida: bool = False
    if plastico[0] == "4" and (len(plastico) == 16 or len(plastico) == 19):
        salida = True
    if len(plastico) == "19":
        plastico = limpiar_plastico(plastico)

    salida=son_numeros(plastico)

    return salida


print("plastico1", validar_tarjeta_visa(plastico1))
print("plastico2", validar_tarjeta_visa(plastico2))
print("plastico3", validar_tarjeta_visa(plastico3))
print("plastico4", validar_tarjeta_visa(plastico4))
print("plastico5", validar_tarjeta_visa(plastico5))
print("plastico6", validar_tarjeta_visa(plastico6))
