#importar la libreria flask
from flask import Flask, redirect, request, render_template, url_for
app = Flask(__name__, template_folder='templates')


registrado = []
""""
class Cliente:
    # Constructor de clase
    def __init__(self, nombre, telefono, estado):
        self.nombre = nombre
        self.telefono = telefono
        self.estado = estado
        print('Se ha creado cliente:',self.nombre)
    def __str__(self):
        return '{} ({})'.format(self.nombre, self.telefono, self.estado)

"""
@app.route('/')
#contenedor para llamar a index.html
def index():
    return render_template('/index.html', registrado = registrado)

@app.route('/sesion')
def sesion():
    return render_template('/login.html')

@app.route('/registro', methods =["GET", "POST"])
def registro():
     if request.method == 'POST':
        return redirect(url_for('index'))
     return render_template('/registrar.html')
     

@app.route('/registrarC', methods =["GET", "POST"])
#contenedor
def registrarC():
    if request.method == 'POST':
        return redirect(url_for('index'))



#contenedor para agregar registro
@app.route('/regcliente_tienda', methods =["GET", "POST"])
def regcliente_tienda():
    if request.method == 'POST':
        Cnombre = request.form['cliente']
        Tnombre = request.form['tienda']
        registrado.append({'cliente': Cnombre,'tienda': Tnombre})
        return redirect(url_for('index'))
        

#ejecutar
if __name__ == '__main__':
    app.run(debug=True)
