# 🤖 Resolvendo Algoritmos em Python com Gemini IA

![Python](https://img.shields.io/badge/Python-306998?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

> Projeto desenvolvido como parte do desafio prático da **DIO (Digital Innovation One)**, com o objetivo de explorar o uso da **Gemini IA** no auxílio à resolução, otimização e documentação de algoritmos em Python.

---

## 💻 Sobre o Projeto

Este repositório reúne resoluções de desafios de código e algoritmos em Python desenvolvidos com suporte de Inteligência Artificial. O foco central não foi apenas obter a solução final, mas entender como a **Gemini IA** atua como uma assistente no dia a dia do desenvolvimento — desde a sugestão de trechos de código até o refatoramento e criação de testes simples.

---

## 🛠️ Tecnologias e Ferramentas

* **[Python 3.10+](https://www.python.org/)** — Linguagem de programação utilizada.
* **[Gemini IA](https://gemini.google.com/)** — Modelo de Inteligência Artificial para geração de código, auxílio no raciocínio lógico e sugestões contextuais.
* **[VS Code](https://code.visualstudio.com/)** — Ambiente de desenvolvimento integrado (IDE).
* **[Git & GitHub](https://github.com/)** — Versionamento de código e hospedagem do repositório.

---

## 🎯 Desafios Resolvidos

Abaixo estão os 6 desafios de código desenvolvidos e explorados no repositório com o auxílio da **Gemini IA**:

1. **[Concatenando Dados 🐾](./1_concatenando_dados.py)**
   * **Objetivo:** Receber duas entradas do usuário e exibi-las juntas em uma única string.
   * **Lógica e Conceitos Aplicados:**
     * Uso da função nativa `input()` para captura de dados (que no Python sempre chegam como o tipo `string`).
     * Utilização de **f-strings** (`f"{var1} {var2}"`) para fazer a interpolação de variáveis de forma mais legível e performática em comparação à concatenação com o operador `+`.
   * **Decisão Técnica:** Opção por um fluxo linear e direto, sem o encapsulamento em funções adicionais, mantendo o script focado na simplicidade do conceito trabalhado.

2. **[Repetindo Textos ✏️](./2_repetindo_textos.py)**
   * **Objetivo:** Receber uma string e um número inteiro, retornando o texto repetido a quantidade de vezes informada.
   * **Lógica e Conceitos Aplicados:**
     * Uso do operador de multiplicação (`*`) em strings para repetição nativa.
     * Formatação e remoção de espaços sobressalentes nas extremidades com `.strip()`.
     * Conversão explícita de tipos com `int()` e tratamento de erros com `try/except` para capturar falhas de conversão (`ValueError`).
     * Controle de fluxo com laço `while True` para validação contínua de entradas.

   * **Decisões de Arquitetura e Resiliência (Clean Code):**
     * **Separação de Responsabilidades (SRP):**
        * `obter_quantidade_valida()`: Cuida exclusivamente do input do usuário e da validação do tipo de dado.
        * `repetir_texto(texto, vezes)`: Função pura responsável apenas pela regra de negócio (multiplicação da string).
     * **Tratamento de Estouro de Memória (`MemoryError`):** Durante os testes de estresse, identificou-se que como o tipo `int` em Python possui precisão arbitrária (sem limite máximo fixo de tamanho), o input de números extremamente altos (ex: $500$ bilhões) não causava estouro de inteiro, mas alocava espaço excessivo de RAM ao tentar gerar a string, resultando em `MemoryError`. A execução principal foi envolvida em um bloco `try/except MemoryError` para capturar essa exceção do sistema e solicitar uma nova quantidade sem derrubar a aplicação.
     * **Remoção do `if __name__`:** Mantido o foco didático e direto para scripts de execução individual.

3. **[Operações Matemáticas Simples 📐](./3_operacoes_matematicas.py)**
   * **Descrição:** Solicita dois números e realiza uma operação matemática básica entre eles.
   * **Conceitos:** Operadores aritméticos (`+`, `-`, `*`, `/`), conversão para número e tratamento de entradas.

4. **[Verificando Números Pares e Ímpares 🧮](./4_par_ou_impar.py)**
   * **Descrição:** Recebe um número inteiro e identifica se ele é par ou ímpar utilizando estruturas condicionais.
   * **Conceitos:** Estruturas de controle (`if/else`), operador de módulo (`%`) e otimização de código com IA.

5. **[Calculando Média de Notas 📚](./5_calculando_media.py)**
   * **Descrição:** Recebe três notas do usuário e calcula a média aritmética simples.
   * **Conceitos:** Operadores aritméticos, precedência de operadores e manipulação de variáveis do tipo `float`.

6. **[Verificando Palíndromos 🔄](./6_verificando_palindromos.py)**
   * **Descrição:** Testa se uma palavra ou frase é um palíndromo (se lida da mesma forma de trás para frente).
   * **Conceitos:** Fatiamento de strings em Python (`[::-1]`), remoção de espaços/caracteres e comparação condicional.
---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3 instalado na sua máquina.
* Git instalado.

### Passo a Passo

1. **Clone este repositório:**
   ```bash git clone https://github.com/miguelAngeloChaves/DIO_CopilotPythonSolutions.git
