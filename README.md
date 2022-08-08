# pyOpenBCI Reader

Este software objetiva a coleta de dados de EEG a partir do capacete Ultracortex Mark IV da OpenBCI.

## Arquivos fonte:

- `set_board.py` para configurar a placa corretamente
- `interface.py` interface temporária em terminal
- `main.py` para integrar tudo

## Arquivo `main.py`:

1. Inicializar a placa com `set_board.py`
2. Pegar os inputs do usuário (nome, número, ...), ainda a ser decidido
3. Inicializar a sessão e gravar no arquivo corretamente

## Features a serem trabalhadas

- Pré filtragem de dados com o próprio brainflow
- Executável do programa
- Programa em modo janela
