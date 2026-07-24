# Desafio 3: Operações Matemáticas Simples 📐

def obter_numero_valido(mensagem):
    """Coleta uma entrada do usuário, garante que seja um número (int ou float) e trata vírgulas."""
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print("❌ Entrada inválida! Por favor, digite um número válido.\n")

def obter_operador_valido():
    """Garante que o usuário escolha apenas uma das operações aceitas."""
    operadores_validos = ['+', '-', '*', '/']
    while True:
        operador = input("Escolha a operação (+, -, *, /): ").strip()
        if operador in operadores_validos:
            return operador
        print(f"⚠️ Operador inválido! Escolha uma das opções: {', '.join(operadores_validos)}\n")

def calcular(num1, num2, operador):
    """Função pura responsável exclusivamente pela execução do cálculo matemático."""
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            raise ZeroDivisionError("Erro: Não é possível dividir por zero!")
        return num1 / num2

# Fluxo Principal
print("--- Calculadora Simples ---")
numero1 = obter_numero_valido("Digite o primeiro número: ")
operador = obter_operador_valido()

while True:
    numero2 = obter_numero_valido("Digite o segundo número: ")
    try:
        resultado = calcular(numero1, numero2, operador)
        
        # Formata a exibição para ocultar o .0 caso o resultado seja um número inteiro
        resultado_formatado = int(resultado) if resultado.is_integer() else round(resultado, 4)
        print(f"\nResultado de {numero1} {operador} {numero2} = {resultado_formatado}")
        break
    except ZeroDivisionError as e:
        print(f"💥 {e} Tente novamente com um segundo número diferente de zero.\n")