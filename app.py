from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import re
from config import Configuracion  # Configuración externa

app = Flask(__name__)
app.config.from_object(Configuracion)

mysql = MySQL(app)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/mostrarRegistro')
def mostrarRegistro():
    return render_template('signup.html')

@app.route('/registrarse', methods=['POST'])
def registrarse():
    conexion = None
    cursor = None
    try:
        nombre = request.form.get('inputName')
        correo = request.form.get('inputEmail')
        contrasena = request.form.get('inputPassword')

        if not (nombre and correo and contrasena):
            return render_template('signup.html', mensaje='Todos los campos son requeridos')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            return render_template('signup.html', mensaje='Correo electrónico inválido')

        contrasena_hash = generate_password_hash(contrasena)

        conexion = mysql.connection
        cursor = conexion.cursor()
        cursor.callproc('sp_createUser', (nombre, correo, contrasena_hash))
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            conexion.commit()
            return redirect(url_for('mostrarLogin'))
        else:
            return render_template('signup.html', mensaje=resultado[0][0])

    except Exception as e:
        print(f"Error en registro: {e}")
        return render_template('signup.html', mensaje='Ocurrió un error inesperado.')
    finally:
        if cursor:
            cursor.close()


@app.route('/mostrarLogin')
def mostrarLogin():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    correo = request.form.get('inputEmail')
    contrasena = request.form.get('inputPassword')

    if not (correo and contrasena):
        return render_template('login.html', mensaje='Todos los campos son requeridos')

    try:
        conexion = mysql.connection
        cursor = conexion.cursor()
        cursor.callproc('sp_loginUser', (correo,))
        resultado = cursor.fetchone()
        cursor.close()

        if resultado and check_password_hash(resultado[2], contrasena):
            return redirect(url_for('inicio'))
        else:
            return render_template('login.html', mensaje='Correo o contraseña incorrectos')

    except Exception as e:
        print(f"Error en login: {e}")
        return render_template('login.html', mensaje='Error al iniciar sesión')

if __name__ == "__main__":
    app.run(debug=True, port=5003)
