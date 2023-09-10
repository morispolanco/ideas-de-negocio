import random

def negocio_ideal(capital_inicial, tiempo_retorno):
    negocios = [
        "Invertir en bienes raíces",
        "Abrir una tienda en línea",
        "Empezar un negocio de consultoría",
        "Crear una aplicación móvil",
        "Montar un restaurante",
        "Iniciar un negocio de dropshipping",
        "Crear una tienda de ropa",
        "Empezar un negocio de marketing digital",
        "Montar una empresa de alquiler de bicicletas",
        "Crear una agencia de viajes"
    ]

    negocio_sugerido = random.choice(negocios)

    print(f"Según tu capital inicial de {capital_inicial} y el tiempo de retorno esperado de {tiempo_retorno} años, te sugiero considerar el negocio de: {negocio_sugerido}.")

# Prueba del chatbot dado el capital inicial y el tiempo de retorno
capital = int(input("Ingresa tu capital inicial: "))
tiempo = int(input("Ingresa el tiempo de retorno esperado (en años): "))

negocio_ideal(capital, tiempo)
