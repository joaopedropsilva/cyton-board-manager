# pyOpenBCI Reader

Este software objetiva a coleta de dados de EEG a partir do capacete Ultracortex Mark IV da OpenBCI.

## Arquivos fonte:

- `set_board.py` para configurar a placa corretamente
- `interface.py` interface temporária em terminal
- `get_data.py` para pegar os dados da placa e gravá-los em arquivos
- `main.py` para integrar tudo

## Arquivo `main.py`:

1. Inicializar a placa com `set_board.py`
2. Pegar os inputs do usuário (nome, número, email, ...), ainda a ser decidido
3. Usar o `get_data.py` para coletar os dados
