# 🎮 Aventura no Labirinto

Um jogo interativo em Python onde você explora labirintos, coleta itens e busca a saída! Desenvolvido com interface rica no terminal usando bibliotecas modernas.

## 🎯 Características

- **Interface Rica**: Terminal colorido e formatado com Rich
- **Controle por Teclado**: Movimentação fluida com setas do teclado
- **Múltiplas Dificuldades**: 3 níveis de labirinto (fácil, médio, difícil)
- **Sistema de Pontuação**: Colete itens para ganhar pontos
- **Resolução Automática**: Algoritmo recursivo para resolver labirintos
- **Efeitos Sonoros**: Sons opcionais para melhor experiência
- **CLI Completa**: Interface de linha de comando com múltiplas opções

## 🚀 Como Executar

### 1. Preparar Ambiente
```bash
# Clone o repositório
git clone <seu-repositorio>
cd aventura_no_labirinto

# Crie e ative um ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar o Jogo
```bash
# Execução básica (nome é obrigatório)
python main.py --name SeuNome

# Com opções personalizadas
python main.py --name João --color green --dificuldade 2

# Com resolução automática habilitada
python main.py --name Maria --color red --dificuldade 3 --auto-solve

# Sem som
python main.py --name Pedro --disable-sound
```

## 🎮 Como Jogar

### Controles
- **Setas do Teclado**: Mover o jogador (J)
- **ESC**: Voltar ao menu principal

### Elementos do Jogo
- **J** (verde) = Jogador (você!)
- **#** (cinza) = Paredes
- **\*** (amarelo) = Itens coletáveis (10 pontos cada)
- **S** (vermelho) = Saída (objetivo)

### Objetivo
Navegue pelo labirinto, colete o máximo de itens possível e chegue à saída!

## 🛠️ Opções da CLI

| Opção | Tipo | Descrição | Padrão |
|-------|------|-----------|---------|
| `--name` | **Obrigatório** | Nome do jogador | - |
| `--color` | Opcional | Cor do tema (cyan, yellow, green, red, blue, magenta) | cyan |
| `--dificuldade` | Opcional | Nível de dificuldade (1, 2, 3) | 1 |
| `--disable-sound` | Flag | Desabilita efeitos sonoros | Habilitado |
| `--auto-solve` | Flag | Habilita opção de resolução automática | Desabilitado |

## 📁 Estrutura do Projeto

```
aventura_no_labirinto/
├── aventura_pkg/           # Pacote principal
│   ├── __init__.py         # Inicialização do pacote
│   ├── labirinto.py        # Criação e exibição de labirintos
│   ├── jogador.py          # Controle do jogador e movimentação
│   └── utils.py            # Funções utilitárias e interface
├── main.py                 # Script principal com CLI
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
└── aventura_pkg.html      # Documentação HTML gerada
```

## 🔧 Tecnologias Utilizadas

- **Python 3.11+**
- **Rich**: Interface rica no terminal
- **Pynput**: Captura de teclas do teclado
- **Playsound**: Efeitos sonoros (opcional)
- **Argparse**: Interface de linha de comando

## 🎯 Funcionalidades Técnicas

### Recursão
- Algoritmo recursivo para resolver labirintos automaticamente
- Animação recursiva de vitória

### Match-Case
- Menu principal implementado com match-case (Python 3.10+)

### Programação Modular
- Código organizado em módulos especializados
- Separação clara de responsabilidades

### Documentação
- Docstrings completas em todos os módulos e funções
- Documentação HTML exportada

## 🎮 Exemplos de Uso

```bash
# Jogo rápido para iniciantes
python main.py --name Iniciante --dificuldade 1

# Desafio avançado com tema personalizado
python main.py --name Expert --color red --dificuldade 3 --auto-solve

# Jogo silencioso
python main.py --name Ninja --disable-sound --color blue
```

## 🏆 Níveis de Dificuldade

- **Nível 1 (Fácil)**: Labirinto 5x5, poucos obstáculos
- **Nível 2 (Médio)**: Labirinto 6x6, complexidade moderada  
- **Nível 3 (Difícil)**: Labirinto 7x7, máxima complexidade

## 🎵 Recursos de Som

O jogo inclui efeitos sonoros opcionais:
- Som de coleta de itens
- Celebração de vitória
- Use `--disable-sound` para jogar em silêncio

## 🐛 Solução de Problemas

### Erro de Permissão de Som
Se houver problemas com áudio, use `--disable-sound`

### Problemas de Teclado
Certifique-se de que o terminal está em foco ao jogar

### Dependências
Se houver erro de importação, reinstale: `pip install -r requirements.txt`

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso de Python Intermediário.

---

**Divirta-se explorando os labirintos! 🎮✨**