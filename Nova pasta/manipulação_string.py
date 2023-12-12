def inverter(texto):
    return texto [::-1]

def contar(texto:str):
    quantidade = 1
    for letra in texto.strip():
        if letra == " ":
            quantidade +=1
    return quantidade

def palindomo(texto:str):
    texto_sem_espaço = texto.replace(" ", "")
    texto_invertido = inverter(texto_sem_espaço)
    if texto_sem_espaço == texto_invertido:
        return "é palídromo"
    else:
        return "nao é um palídromo"