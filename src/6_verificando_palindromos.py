##Descrição:** Testa se uma palavra ou frase é um palíndromo (se lida da mesma forma de trás para frente).
##Conceitos:** Fatiamento de strings em Python (`[::-1]`), remoção de espaços/caracteres e comparação condicional.

import unicodedata

def normalizar_texto(texto):
    """Remove acentos, espaços e caracteres especiais do texto, retornando apenas letras minúsculas."""
    # Decompõe caracteres acentuados (ex: 'á' vira 'a' + '´')
    texto_nfd = unicodedata.normalize('NFD', texto)
    # Filtra mantendo apenas caracteres alfanuméricos sem os acentos
    texto_limpo = ''.join(
        char.lower() for char in texto_nfd 
        if char.isalnum() and unicodedata.category(char) != 'Mn'
    )
    return texto_limpo

def eh_palindromo(texto):
    """Função pura que verifica se o texto fornecido é um palíndromo."""
    texto_limpo = normalizar_texto(texto)
    if not texto_limpo:
        return False  # Retorna False se o texto estiver vazio após a normalização
    return texto_limpo == texto_limpo[::-1]

def obter_texto_valido():
    """Solicita ao usuário um texto e garante que não seja vazio."""
    while True:
        texto = input("Digite uma palavra ou frase: ").strip()
        if normalizar_texto(texto):
            return texto
        print("⚠️ Entrada inválida! Digite uma palavra ou frase com letras ou números.\n")


# Fluxo Principal

print("--- Verificador de Palíndromos ---")
texto_usuario = obter_texto_valido()

# Processamento e Demonstração
texto_limpo = normalizar_texto(texto_usuario)
texto_invertido = texto_limpo[::-1]


if len(texto_limpo) < 2:
    print("\nℹ️  Aviso sobre o Conceito de Palíndromos:")
    print(f"• Você digitou: '{texto_usuario}' (apenas {len(texto_limpo)} caractere válido).")
    print("• Um palíndromo é uma sequência de 2 ou mais caracteres que, quando lida de trás para frente, permanece idêntica (ex: 'ovo', 'ana', '1221').")
    print("• Um único caractere não possui espelhamento para formar uma sequência palíndroma.")
else:
    # Demonstração e Verificação
    texto_invertido = texto_limpo[::-1]
    
    print("\n🔍 Demonstração da Análise:")
    print(f"• Original sanitizado: {texto_limpo}")
    print(f"• Leitura invertida:  {texto_invertido}")

    if eh_palindromo(texto_usuario):
        print(f"\n✅ A entrada '{texto_usuario}' é um palíndromo (considerando o termo '{texto_limpo}')!")
    else:
        print(f"\n❌ '{texto_usuario}' NÃO é um palíndromo.")