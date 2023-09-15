# Usamos un bucle for para imprimir los números del 1 al 100
for numero in range(1, 101):
    print(numero)
    


# Usamos un bucle for para imprimir los números del 1 al 100 que son divisibles por 3
for numero in range(1, 101):
    if numero % 3 == 0:
        print(numero)



# Calcular la suma de los dos números
resultado = numero1 + numero2

# Comprobar las condiciones y mostrar los mensajes apropiados
if resultado < 100:
    print("El resultado es menor a 100")
elif resultado <= 150:
    print("El resultado es mayor a 100, pero menor o igual a 150")
else:
    print("El resultado es mayor a 150")



    def evaluar_gastos(presupuesto_mensual, gastos_prendas, gastos_accesorios):
    gastos_totales = gastos_prendas + gastos_accesorios
    
    if gastos_totales > presupuesto_mensual:
        exceso_gastos = gastos_totales - presupuesto_mensual
        return f"Has gastado ${exceso_gastos:.2f} más de tu presupuesto mensual en prendas de vestir y accesorios. ¡Necesitas administrar mejor tus gastos!"
    else:
        return "Estás dentro de tu presupuesto mensual. ¡Buena administración!"
    
# Solicitar al usuario su presupuesto mensual y los gastos en prendas de vestir y accesorios
presupuesto_mensual = float(input("Ingresa tu presupuesto mensual: $"))
gastos_prendas = float(input("¿Cuánto has gastado en prendas de vestir este mes? $"))
gastos_accesorios = float(input("¿Cuánto has gastado en accesorios este mes? $"))

# Llamar a la función y mostrar el mensaje correspondiente
mensaje = evaluar_gastos(presupuesto_mensual, gastos_prendas, gastos_accesorios)
print(mensaje)