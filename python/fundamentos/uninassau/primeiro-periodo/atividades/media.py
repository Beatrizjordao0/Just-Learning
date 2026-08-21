v1 = 5.9
v2 = 8.4

def media(value1, value2):
    media = 0
    sum = value1 + value2
    media = sum / 2
    return f"{media:.1f}"


print(media(v1, v2))