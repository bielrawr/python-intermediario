# Microblog

Microblog é uma aplicação web simples desenvolvida em Flask como parte do Trabalho Prático do curso de Programação em Python. A aplicação permite que usuários se cadastrem, façam login, publiquem posts textuais e visualizem uma timeline com os posts mais recentes. O projeto foi estilizado com CSS moderno para oferecer uma interface amigável e acessível.

## Funcionalidades

- **Cadastro de Usuários**: Crie uma conta com nome de usuário, senha, foto de perfil (URL) e bio.
- **Login e Logout**: Autenticação segura com suporte a "Lembrar de mim".
- **Posts**: Usuários autenticados podem criar posts textuais e visualizar os 5 mais recentes na timeline.
- **Perfil**: Exibição de foto de perfil e bio na página inicial.
- **Estilização**: Interface moderna com navegação fixa, cards, sombras e transições.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `flask`
  - `flask-sqlalchemy`
  - `flask-login`
  - `python-dotenv`

## Instalação

1.	**Clone o repositório**

2. **Crie e ative um ambiente virtual**:
   - 'python -m venv flask_env'
   - 'source flask_env/bin/activate  # Linux/Mac'
   - 'flask_env\Scripts\activate     # Windows'

3. **Instale as dependências**

   	pip install flask flask-sqlalchemy flask-login python-dotenv


## Execução
1.	Inicie o servidor: 
flask run
2.	Acesse a aplicação: 
o	Abra o navegador em http://127.0.0.1:5000/.
o	Você será redirecionado para a página de login se não estiver autenticado.


## Uso
•	Cadastro: Acesse /cadastro, preencha os campos e clique em "Cadastrar".
•	Login: Acesse /login, insira suas credenciais e clique em "Login".
•	Criar Post: Na página inicial, clique em "Escrever post", digite seu texto e clique em "Publicar".
•	Logout: Clique em "Logout" na navegação para sair.
	
