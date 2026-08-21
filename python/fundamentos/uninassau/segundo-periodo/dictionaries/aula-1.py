'''
Você está ajudando a equipe do curso a organizar uma batalha de robôs.
Cada robô tem vários componentes (motor, sensor, bateria) e cada componente 
possui características próprias.

Crie um programa em Python que:
Armazene as informações de 3 componentes de um robô usando um dicionário, 
onde:
A chave é o nome do componente

O valor é outro dicionário contendo:
Peso (float, em kg)
consumo (int, em watts)
categoria (string: “defesa”, “ataque” ou “suporte”)

O usuário deve conseguir:

Listar todos os componentes com seus atributos

Buscar um componente pelo nome

Calcular o consumo total do robô somando todos os consumos

Desafio opcional: ordenar os componentes do menor para o maior peso
'''

# Dicionário para armazenar os componentes do robô
di = {
    "motor": {
        "peso": 5.0,
        "consumo": 150, 
        "categoria": "ataque"},
    "sensor": {
        "peso": 1.5, 
        "consumo": 50, 
        "categoria": "suporte"},
    "bateria": {
        "peso": 3.0, 
        "consumo": 200, 
        "categoria": "defesa"}
}

# Listagem dos componentes
print("Motor: ",di["motor"])
print("Sensor: ",di["sensor"])
print("Bateria: ",di["bateria"])


# Buscar pelo nome
def buscar_pelo_nome():
    componente = input("Digite um componente entre motor, sensor e bateria: ")
    while True:
        if componente.lower() == "motor" or componente.lower() == "sensor" or componente.lower() == "bateria":
            print(di[componente.lower()])
            break
        else:
            componente = input("Por favor, insira dados válidos.\n")

buscar_pelo_nome()

# Consumo Total

def calculo_consumo_total():
    consumos = [item["consumo"] for item in di.values()]
    print(consumos)
    consumo_total = sum(consumos)
    print(f"O consumo total do robô é de: {consumo_total}watts")


calculo_consumo_total()
