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

* **<a href="https://www.python.org/" target="_blank" rel="noopener noreferrer">Python 3.10+</a>** — Linguagem de programação utilizada.
* **<a href="https://gemini.google.com/" target="_blank" rel="noopener noreferrer">Gemini IA</a>** — Modelo de Inteligência Artificial para geração de código, auxílio no raciocínio lógico e sugestões contextuais.
* **<a href="https://code.visualstudio.com/" target="_blank" rel="noopener noreferrer">VS Code</a>** — Ambiente de desenvolvimento integrado (IDE).
* **<a href="https://github.com/" target="_blank" rel="noopener noreferrer">Git & GitHub</a>** — Versionamento de código e hospedagem do repositório.
  
## 🎯 Desafios Resolvidos

Abaixo estão os 6 desafios de código desenvolvidos e explorados no repositório com o auxílio da **Gemini IA**:

1. **[Concatenando Dados 🐾](src/1_concatenando_dados.py)**
   * **Objetivo:** Receber duas entradas do usuário e exibi-las juntas em uma única string.
   * **Lógica e Conceitos Aplicados:**
     * Uso da função nativa `input()` para captura de dados (que no Python sempre chegam como o tipo `string`).
     * Utilização de **f-strings** (`f"{var1} {var2}"`) para fazer a interpolação de variáveis de forma mais legível e performática em comparação à concatenação com o operador `+`.
   * **Decisão Técnica:** Opção por um fluxo linear e direto, sem o encapsulamento em funções adicionais, mantendo o script focado na simplicidade do conceito trabalhado.

2. **[Repetindo Textos ✏️](src/2_repetindo_textos.py)**
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

3. **[Operações Matemáticas Simples 📐](src/3_operacoes_matematicas.py)**
   * **Objetivo:** Solicitar dois números e um operador aritmético ao usuário para realizar e exibir o cálculo.
   * **Lógica e Conceitos Aplicados:**
     * Uso de conversão de tipos para ponto flutuante (`float()`) com suporte à substituição de vírgula por ponto (`.replace(',', '.')`).
     * Tratamento do erro de divisão por zero (`ZeroDivisionError`) e erros de conversão (`ValueError`).
     * Formatação de saída com `round()` e verificação de números inteiros com `.is_integer()`.

   * **Decisões de Arquitetura e Resiliência (Clean Code):**
     * **Separação de Responsabilidades (SRP):**
       * `obter_numero_valido()`: Valida e converte a entrada numérica.
       * `obter_operador_valido()`: Restringe e valida a seleção dos operadores aceitos (`+`, `-`, `*`, `/`).
       * `calcular()`: Função pura focada apenas nas quatro operações fundamentais.
     * **Tratamento de Divisão por Zero:** A função de cálculo lança a exceção e o fluxo principal captura, impedindo o *crash* e permitindo ao usuário re-digitar apenas o segundo número.
  
4. **[Verificando Números Pares e Ímpares 🧮](src/4_par_ou_impar.py)**
   * **Objetivo:** Receber um número inteiro do usuário e verificar se ele é par ou ímpar utilizando o operador de módulo (`%`).
   * **Lógica e Conceitos Aplicados:**
     * Uso da operação matemática de resto da divisão (`numero % 2 == 0`) para determinar paridade.
     * Estrutura de operador ternário para atribuição condicional direta (`"par" if ... else "ímpar"`).
     * Validação de entrada para garantir a conversão segura com `int()` e tratamento do erro de conversão (`ValueError`).

   * **Decisões de Arquitetura e Resiliência (Clean Code):**
     * **Análise de Matemática Computacional:** O operador `%` em Python lida de forma nativa com números inteiros negativos e o número `0`, mantendo o comportamento consistente sem a necessidade de condicionais extras.
     * **Separação de Responsabilidades (SRP):**
       * `obter_numero_inteiro()`: Responsável exclusivamente por coletar e garantir a entrada válida no terminal.
       * `eh_par_ou_impar()`: Função pura focada unicamente no cálculo da regra de paridade.
  
5. **[Calculando Média de Notas 📚](src/5_calculando_media.py)**
   * **Objetivo:** Receber três notas de um aluno, calcular a média aritmética simples e exibir o resultado formatado.
   * **Lógica e Conceitos Aplicados:**
     * Coleta e conversão de entradas para o tipo `float` com tratamento de vírgulas (`.replace(',', '.')`).
     * Validação de escala de negócio para restringir entradas ao intervalo de notas $[0.0, 10.0]$.
     * Processamento de coleções com as funções nativas `sum()` e `len()`.
     * Formatação condicional da saída utilizando `.is_integer()` e `round(media, 2)`.

   * **Decisões de Arquitetura e Resiliência (Clean Code):**
     * **Função de Validação Agnóstica:** A função `obter_nota_valida(mensagem)` recebe a string de prompt pronta, mantendo-se $100\%$ desacoplada do laço de repetição e pronta para reutilização em qualquer contexto.
     * **Generalização do Cálculo:** A função `calcular_media(notas)` opera sobre uma lista genérica, tornando a regra de negócio extensível para qualquer quantidade de avaliações sem necessidade de alteração de código.
     * **Programação Defensiva:** Inclusão de verificação contra listas vazias (`if not notas`) para evitar o lançamento de erro de divisão por zero (`ZeroDivisionError`).

6. **[Verificando Palíndromos 🔄](src/6_verificando_palindromos.py)**
   * **Objetivo:** Receber uma palavra ou frase e verificar se ela é um palíndromo, desconsiderando espaços, acentos, pontuações e símbolos de ruído.
   * **Lógica e Conceitos Aplicados:**
     * Uso de fatiamento (*slicing*) `[::-1]` para inversão nativa e eficiente de strings.
     * Normalização de texto via módulo `unicodedata` (decomposição NFD) para remoção de acentos e diacríticos.
     * Filtragem com `.isalnum()` para descartar ruídos, espaços e caracteres especiais (ex: `_`, `-`, `!`).

   * **Decisões de Arquitetura e Resiliência (Clean Code):**
     * **Validação Conceitual de Tamanho Mínimo:** Exigência de no mínimo 2 caracteres alfanuméricos válidos para a análise. Caso informado apenas 1 caractere, o sistema exibe uma mensagem educativa sobre o conceito de espelhamento em palíndromos.
     * **Demonstração Transparente (UX):** Exibição do termo sanitizado lado a lado com sua versão invertida, permitindo ao usuário entender o processo de higienização do dado.
     * **Separação de Responsabilidades (SRP):** Isolamento entre sanitização de dados (`normalizar_texto`), regra de paridade (`eh_palindromo`) e controle de entrada (`obter_texto_valido`).---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3 instalado na sua máquina.
* Git instalado.

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/miguelAngeloChaves/DIO_CopilotPythonSolutions.git](https://github.com/miguelAngeloChaves/DIO_CopilotPythonSolutions.git)
   ```