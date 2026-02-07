import math
from flask import Flask, render_template, request, flash
import forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "clave_secreta"
csrf = CSRFProtect()

@app.route('/')
def index():
    title = "IDGS804 -Intro Flask"
    listado = ['Juan', 'Ana', 'Pedro', 'Luisa']
    
    return render_template('index.html', title = title, listado = listado)

@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')

@app.route('/saludo2')
def saludo2():
    return render_template('saludo2.html')

@app.route("/hola")
def func():
    return '¡Hola, Mundo -- Hola!'

@app.route("/user/<string:user>")
def user(user):
    return f'¡Hola, {user}!'

@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Número: {n}</h1>'

@app.route("/username/<int:id>/<string:username>")
def username(id, username):
    return f'<h1>¡Hola, {username}! Tu ID es: {id}'

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'

@app.route("/default")
@app.route("/default/<string:param>")
def func2(param="juan"):
    return f'<h1>¡Hola, {param}!</h1>'

@app.route("/operas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="name">aPaterno:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <input type="submit" value="Submit">
    </form>
'''

@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    res = None
    if request.method == 'POST':
        n1 = float(request.form.get('num1'))
        n2 = float(request.form.get('num2'))
        operacion = request.form.get('operacion')

        if operacion == "sumar":
            res = n1 + n2
        elif operacion == "restar":
            res = n1 - n2
        elif operacion == "multiplicar":
            res = n1 * n2
        elif operacion == "division":
            res = n1 / n2

    return render_template('operasBas.html', res = res)

@app.route("/resultado", methods=["GET", "POST"])
def result():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f'<h1>La suma es: {float(n1) + float(n2)}</h1>'

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    resultado = None

    if request.method == "POST":
        x1 = float(request.form["x1"])
        x2 = float(request.form["x2"])
        y1 = float(request.form["y1"])
        y2 = float(request.form["y2"])

        resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template("distancia.html", resultado=resultado)

@app.route("/alumnos",methods=["GET", "POST"])
def alumnos():
    mat = 0
    nom = ''
    ape = ''
    email = ''
    alumno_clas = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data
    return render_template("alumnos.html", form = alumno_clas, mat = mat, nom = nom, ape = ape, email = email)

@app.route("/cinepolis", methods=["GET","POST"])
def cinepolis():
    nom=""
    cantiCom = 0
    isCineco=""
    cantiBol=0
    Total =0
    alert = ""
    cinepolis_class = forms.CinepolisForm(request.form)
    if request.method == "POST" and cinepolis_class.validate():
        nom = cinepolis_class.nombre.data
        cantiCom = cinepolis_class.compradores.data
        isCineco = cinepolis_class.cineco.data
        cantiBol = cinepolis_class.boletos.data
        limit = cantiCom * 7
        if cantiBol <= limit:
            Total = cantiBol*12
            if cantiBol == 3 or cantiBol == 4 or cantiBol == 5:
                Total *= 0.90
            if cantiBol > 5:
                Total *= 0.85
            if isCineco == "si":
                Total *= 0.90
        else:
            Total = 0
            alert = "Solo se permiten 7 boletos por comprador. La cantidad ingresada es incorrecta."
            flash(alert)
    return render_template("cinepolis.html",form=cinepolis_class ,nom = nom, cantiCom= cantiCom,isCineco=isCineco,cantiBol=cantiBol, Total=Total)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)