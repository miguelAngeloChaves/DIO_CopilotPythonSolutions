##Descrição:** Recebe um número inteiro e identifica se ele é par ou ímpar utilizando estruturas condicionais.
##Conceitos:** Estruturas de controle (`if/else`), operador de módulo (`%`) e otimização de código com IA.

def eh_par_ou_impar(numero):
    """Função pura que determina se um número é par ou ímpar."""
    return "par" if numero % 2 == 0 else "ímpar"

def obter_numero_inteiro():
    """Solicita ao usuário um número inteiro e garante que a entrada seja válida."""
    while True:
        entrada = input("Digite um número inteiro: ").strip()
        try:
            return int(entrada)
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite apenas números inteiros (sem casas decimais ou letras).\n")

# Fluxo Principal
numero_usuario = obter_numero_inteiro()
resultado = eh_par_ou_impar(numero_usuario)
print(f"\nO número {numero_usuario} é {resultado}.")

