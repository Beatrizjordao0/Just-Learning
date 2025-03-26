def minMax(temperature):
    return (f"A menor temperatura é: {minimum(temperature)}\n"
            f"A maior temperatura é: {maximum(temperature)}")

def minimum(temps):
    min_value = temps[0]
    for temperatures in temps:
        if temperatures < min_value:
            min_value = temperatures
    return min_value

def maximum(temps):
    max_value = temps[0]
    for temperatures in temps:
        if temperatures > max_value:
            max_value = temperatures
    return max_value

lista_ = [39, 47, 22, 57, 89, 36, 75, 90, 11, 23, 90, 45, 99, 99, -9]

print(minMax(lista_))