# Exemplo de entrada
n = 12
def makeChange(n):
   #inicialização do set, para armazenamento
    result_set = set()

    # Loop para encontrar todas as combinações possíveis
    for quarters in range(n // 25 + 1):
        for dimes in range((n - quarters * 25) // 10 + 1):
            for nickels in range((n - quarters * 25 - dimes * 10) // 5 + 1):
                pennies = n - quarters * 25 - dimes * 10 - nickels * 5
                # Converta a lista em uma tupla antes de adicionar ao conjunto
                result_set.add((pennies, dimes, nickels, quarters))

    return result_set



# Chamada da função e impressão do resultado
print(makeChange(n))