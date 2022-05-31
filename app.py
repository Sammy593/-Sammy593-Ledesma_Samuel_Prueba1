#importar la libreria flask
from flask import Flask, redirect, request, render_template, url_for
app = Flask(__name__, template_folder='templates')


cliente = []
@app.route('/')
#contenedor para llamar a index.html
def index():
    return render_template('/index.html')

@app.route('/sesion')
def sesion():
    return render_template('/login.html')

@app.route('/registro', methods =["GET", "POST"])
def registro():
     if request.method == 'POST':
        return redirect(url_for('index'))
     return render_template('/registrar.html')
     

@app.route('/registrarC', methods =["GET", "POST"])
#contenedor para llamar a enviar.html
def registrarC():
    if request.method == 'POST':
        tituloT = request.form['titulo']
        correoT = request.form['correo']
        prioridadT = request.form['prioridad']


        cliente.append({'titulo': tituloT,'correo': correoT,'prioridad': prioridadT})
   
        return redirect(url_for('index'))

#ejecutar
if __name__ == '__main__':
    app.run(debug=True)
