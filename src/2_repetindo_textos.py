# Desafio 2: Repetindo Textos ✏️ (Versão Técnica)

def repetir_texto():
    texto = input("Digite o texto que deseja repetir: ")
    
    # Tratamento para garantir que o usuário digite um número inteiro válido
    try:
        numero = int(input("Digite a quantidade de vezes que deseja repetir: "))
        
        if numero <= 0:
            print("Por favor, digite um número inteiro maior que zero.")
            return

        # Multiplicação da string e remoção do espaço sobressalente no final (.strip)
        resultado = (texto + " ") * numero
        print(f"\nResultado:\n{resultado.strip()}")

    except ValueError:
        print("Erro: Entrada inválida. Você precisa digitar um número inteiro.")

if __name__ == "__main__":
    repetir_texto()