from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cines")
@app.route("/cines/<id>")
def cines( id = None ):
    if id == None:
        response = requests.get('https://oaemdl.es/cinestar_sweb_php/cines')
        if response.status_code == 200:
            response = response.json()
            if response['success']:
                return render_template('cines.html', cines = response['data'] )
            else : return render_template('index.html')
        else : return render_template('index.html')

    return render_template('cine.html')

@app.route("/peliculas/<id>")
def peliculas(id):
    return render_template('peliculas.html')

if __name__ == "__main__":
    app.run( debug = False )