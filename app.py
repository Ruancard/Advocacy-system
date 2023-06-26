from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'SecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/advocacia'
app.config['UPLOAD_FOLDER'] = 'static/upload/'
db = SQLAlchemy(app)

class Advogados(db.Model):
    oab = db.Column(db.String(8), primary_key=True)
    usuario = db.Column(db.String(30), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    cpf = db.Column(db.String(15), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    tel = db.Column(db.String(15), nullable=False)
    estado = db.Column(db.String(3), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    bairro = db.Column(db.String(30), nullable=False)
    rua = db.Column(db.String(30), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    cep = db.Column(db.String(10), nullable=False)

class Clientes(db.Model):
    cpf = db.Column(db.String(15), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    tel = db.Column(db.String(15), nullable=False)
    estado = db.Column(db.String(3), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    bairro = db.Column(db.String(30), nullable=False)
    rua = db.Column(db.String(30), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    cep = db.Column(db.String(10), nullable=False)

class processos(db.Model):
    numero = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(300), nullable=False)
    observacao = db.Column(db.String(100))
    vara = db.Column(db.String(15), nullable=False)
    requerente = db.Column(db.String(50), nullable=False)
    reu = db.Column(db.String(50), nullable=False)
    acusacao = db.Column(db.String(50), nullable=False)
    defesa = db.Column(db.String(50), nullable=False)
    juiz = db.Column(db.String(50), nullable=False)
    dt_inicio = db.Column(db.Date, nullable=False)
    dt_att = db.Column(db.Date, nullable=False)

usernames = ['admin']
passwords = ['admin']

@app.route('/')
def home():
    if 'username' in session and session['username'] in usernames:
        process = processos.query.all()
        return render_template('home.html', processos = process)
    else:
        return redirect('/entrar')

@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
        return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in usernames and password in passwords:
            session['username'] = username
            return redirect('/')
        else:
            return redirect('/entrar')
    else:
        return redirect('/entrar')   

@app.route('/logout' , methods=['POST', 'GET'])
def logout():
    session.pop('username', None)
    return redirect('/entrar')


app.run(debug=True)