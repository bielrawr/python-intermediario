import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Define o caminho base como o diretório raiz do projeto
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'microblog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'PD12345678'

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'  # Define a rota de login para redirecionamento

# Importa os módulos da aplicação
from app import routes, models, alquimias

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()