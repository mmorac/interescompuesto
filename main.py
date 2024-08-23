monedas = {
    "usd": "$",
    "eur": "€",
    "crc": ""
}

def calcular_interes_compuesto(moneda, inicial, aporte, periodo, interes, plazo):
    simbolo = monedas[moneda]
    final = inicial

    if(periodo == "mensual"):
        for i in range(0, plazo):
            for j in range(0, 12):
                final += aporte
            final *= 1+(interes/100)
        if(moneda == "eur"):
            return f"{round(final, 2)}{simbolo}"
        else:
            return f"{simbolo}{round(final, 2)}"
    elif(periodo == "anual"):
        for i in range(0, plazo):
            final += aporte
            final *= 1+(interes/100)
        if(moneda == "eur"):
            return f"{round(final, 2)}{simbolo}"
        else:
            return f"{simbolo}{round(final, 2)}"
    else:
        return "Error"


def ejecutar():
    moneda = input("Digite Moneda: ")
    inicial = float(input("Digite el saldo inicial: "))
    aporte = float(input("Digite el aporte: "))
    periodo = input("Digite cada cuánto aportará: ")
    interes = float(input("Digite la tasa de interés: "))
    plazo = int(input("Digite el plazo en años al que invertirá: "))
    print("Recibirás: ", calcular_interes_compuesto(moneda, inicial, aporte, periodo, interes, plazo))

ejecutar()
