from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html', titulo='Home', mensaje='Bienvenido a la página de inicio')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Estos son nuestros servicios')

@app.route('/contacto')
def contacto():
    return render_template('contactos.html', titulo='Contactos', mensaje='Bienvenido a nuestros contactos')

@app.route('/productos')
def productos():
    return render_template('productos.html', titulo='Productos', mensaje='Bienvenido al catálogo de productos')


if __name__ == '__main__':
    app.run(debug=True, port = 5050)