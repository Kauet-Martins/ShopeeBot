
# ShopeeBot - Automação de Seguidores

Este projeto é uma automação feita com Selenium e interface gráfica em Tkinter para seguir e deixar de seguir usuários na Shopee a partir do ID de uma loja.

## Funcionalidades

- Login manual com persistência de sessão.
- Interface gráfica intuitiva com botões de ação.
- Seguir usuários de uma loja específica.
- Deixar de seguir perfis seguidos.
- Exportação de resultados em `.csv` com nomes dos usuários.
- Geração de executável para uso final (sem terminal).

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/shopee-bot.git
   cd shopee-bot
   ```

2. Instale os requisitos:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

> Para gerar o executável:
```bash
pyinstaller --onefile --noconsole --icon=icon.ico main.py
```

## Estrutura do Projeto

```
shopee-bot/
│
├── main.py                  # Interface principal com menu
├── login.py                 # Controle de sessão com cookies
├── seguidores.py            # Lógica para seguir usuários
├── deixar_de_seguir.py      # Lógica para deixar de seguir
├── utils/
│   ├── arquivos.py          # Funções para salvar CSV
│   └── diretorios.py        # Funções para manipular diretórios
├── assets/
│   └── icon.ico             # Ícone do executável
└── README.md
```

## Observações

- O login é feito manualmente para garantir segurança.
- Os arquivos `.csv` são salvos na Área de Trabalho por padrão.
- Compatível com Windows 10+ e Python 3.10+.

## Licença

Este projeto está licenciado sob a licença MIT.
