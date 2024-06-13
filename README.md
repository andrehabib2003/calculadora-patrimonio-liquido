# Calculadora de Patrimônio Líquido

Este repositório contém um código Python que cria uma calculadora de patrimônio líquido utilizando a biblioteca Tkinter para a interface gráfica.

## Descrição

A calculadora de patrimônio líquido é uma ferramenta simples que permite calcular o patrimônio líquido de um indivíduo com base nos ativos e passivos inseridos. A interface gráfica foi construída com Tkinter, e o aplicativo permite a entrada dos valores dos ativos e passivos, calcula o patrimônio líquido e exibe o resultado na tela.

## Funcionalidades

- Entrada dos valores dos ativos, como imóveis, poupança, veículos, investimentos e outros ativos.
- Entrada dos valores dos passivos, como hipotecas, empréstimos, financiamentos e outras dívidas.
- Cálculo do patrimônio líquido com base nos valores fornecidos.
- Exibição do resultado na tela.

## Requisitos

- Python 3.x
- Tkinter
- Pillow

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/calculadora-patrimonio-liquido.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd calculadora-patrimonio-liquido
    ```
3. Instale as dependências:
    ```bash
    pip install Pillow
    ```

## Como Usar

1. Coloque a imagem `patrimonio.png` no diretório do projeto.
2. Execute o script:
    ```bash
    python calculadora_patrimonio_liquido.py
    ```
3. Insira os valores dos ativos e passivos nos campos correspondentes.
4. Clique no botão "Calcular" para obter o patrimônio líquido.

## Estrutura do Código

O código é dividido em várias seções:

- **Configuração de Cores**: Define as cores utilizadas na interface.
- **Criação da Janela**: Configura a janela principal do aplicativo.
- **Criação dos Frames**: Divide a janela em diferentes seções para organizar os elementos da interface.
- **Função de Cálculo**: Realiza o cálculo do patrimônio líquido com base nos valores fornecidos.
- **Entradas e Labels**: Define os campos de entrada e labels para os ativos e passivos.
- **Botão de Calcular**: Define o botão que aciona a função de cálculo.
