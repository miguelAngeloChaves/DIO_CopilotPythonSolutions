# Desafio 2: Repetindo Textos ✏️

def obter_quantidade_valida():
    while True:
        try:
            qtd = int(input("Digite a quantidade de repetições: "))
            if qtd > 0:
                return qtd
            print("⚠️ Digite um número maior que zero.\n")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.\n")

def repetir_texto(texto, vezes):
    return (texto + " ") * vezes

# Execução do fluxo
texto_usuario = input("Digite o texto que deseja repetir: ")


while True:
    vezes_usuario = obter_quantidade_valida()
    try:
        resultado = repetir_texto(texto_usuario, vezes_usuario)
        print(f"\nResultado:\n{resultado.strip()}")
        break  # Sucesso: exibe o resultado e sai do programa
    except MemoryError:
        print("💥 Erro de Memória: A quantidade pedida gera um texto grande demais para a RAM do seu computador!")
        print("Tente novamente com um número menor.\n")