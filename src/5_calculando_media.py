
##Descrição:** Recebe três notas do usuário e calcula a média aritmética simples.
##Conceitos:** Operadores aritméticos, precedência de operadores e manipulação de variáveis do tipo `float`.

def obter_nota_valida(mensagem):
    """Solicita ao usuário uma nota e garante que seja um número válido entre 0 e 10."""
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            print("⚠️ Nota inválida! Digite um valor entre 0 e 10.\n")
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite apenas números válidos (ex: 7.5).\n")

def calcular_media(notas):
    """Calcula a média aritmética simples de uma lista de notas."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

# Fluxo Principal

quantidade_notas = 3
notas_usuario = []

print(f"--- Calculadora de Média Aritmética ---\nDigite {quantidade_notas} notas (de 0 a 10):")
for i in range(1, quantidade_notas + 1):
    nota = obter_nota_valida(f"Nota {i}: ")
    notas_usuario.append(nota)

media = calcular_media(notas_usuario)

# Formata a exibição para ocultar o .0 caso a média seja um número inteiro
media_formatada = int(media) if media.is_integer() else round(media, 2)

print(f"\nA média das notas {notas_usuario} é: {media_formatada}")