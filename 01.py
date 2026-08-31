# declaración de variables
cantidad_tarimas: int = 0
costo_por_tarima: float = 0.0     #note que el ejercicio no dice en ningún momento cuanto vale cada tarima, si ponemos un valor como 1000, estaríamos limitamdo a que el código solo funcione con ese valor
costo_fijo: float=0.0
descuento: float=0.0
subtotal: float=0.0
total_sin_descuento: float=0.0
costo_total: float= 0.0

# entradas
cantidad_tarimas=int(input("Digite la cantidad de tarimas almacenadas: "))
costo_por_tarima= float(input("digite el valor por tarima mensual: "))
descuento= float(input("digite el descuento por volumen: "))
costo_fijo= float(input("ingreso el costo fijo mensual: "))

# procesos
subtotal= cantidad_tarimas*costo_por_tarima
total_sin_descuento= subtotal+costo_fijo
costo_total= total_sin_descuento-descuento

#salidas
print("la variable subtotal es igual a: ", subtotal)
print("el total sin descuento es igual a: ",total_sin_descuento)
print("el costo_total es: ", costo_total)

