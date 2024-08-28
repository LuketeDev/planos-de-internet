consumo = float(input())

def recomendar_plano(consumo):
    return "Plano Essencial Fibra - 50Mbps" if consumo < 10 else \
        "Plano Prata Fibra - 100Mbps" if 10 <= consumo < 20 else "Plano Premium Fibra - 300Mbps"
print(recomendar_plano(consumo))