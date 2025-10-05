from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app import alquimias

@app.route('/')
@login_required
def index():
    posts = alquimias.get_timeline() if current_user.is_authenticated else []
    return render_template('index.html', title='Página Inicial', user=current_user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()
        user = alquimias.validate_user_password(username, password)
        if user:
            print("\nLogin bem sucedido!\n")
            login_user(user, remember=user.remember)
            flash("Login bem sucedido!")
            return redirect(url_for('index'))
        else:
            print("\nUsuário ou senha inválidos\n")
            flash("Usuário ou senha inválidos")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username'].lower()
        if alquimias.user_exists(username):
            print("\nUsuário já existe!\n")
            flash("Usuário já existe!")
            return redirect(url_for('login'))
        else:
            password = request.form['password'].lower()
            remember = True if request.form.get('remember') == 'on' else False
            profile_pic = request.form.get('profile_pic', '')
            bio = request.form.get('bio', '')
            user = alquimias.create_user(username, password, remember, profile_pic=profile_pic, bio=bio)
            login_user(user, remember=remember)
            flash("Cadastro realizado com sucesso!")
            return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        alquimias.create_post(body, current_user)
        flash("Post criado com sucesso!")
        return redirect(url_for('index'))
    return render_template('post.html')