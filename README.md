# Cyton Board Manager

Este software objetiva a coleta de dados de EEG a partir do capacete Ultracortex Mark IV da OpenBCI.

## Arquivos fonte:

- `set_board.py` para configurar a placa corretamente
- `get_data.py` para coletar dados
- `interface.py` interface temporária em terminal
- `main.py` para integrar tudo

## Arquivo `main.py`:

1. Inicializar a placa com `set_board.py`
2. Pegar os inputs da sessão (nome e número) e do usuário (nome e número) com `interface.py`
3. Inicializar a sessão e coletar os dados utilizando o `get_data.py`
4. Gravar os dados em um arquivo cvs formatado e com cabeçalho

## Features a serem trabalhadas

- Pré filtragem de dados com o próprio brainflow
- Executável do programa
- Programa em modo janela
