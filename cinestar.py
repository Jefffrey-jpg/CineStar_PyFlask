from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

def page_no_found(error) :
    return render_template('index.html'), 404

@app.route("/")
def index() :
    return render_template('index.html')

@app.route("/cines")
@app.route("/cines/<id>")
def cines(id = None) :
    if id == None :
        response = requests.get('https://oaemdl.es/cinestar_sweb_php/cines')
        if response.status_code == 200 :
            response = response.json()
            if response['success'] :
                return render_template('cines.html', cines = response['data'])
            else : return redirect( url_for('index') )
        else: return redirect( url_for('index') )
        
    #Completar cine
    return render_template('cine.html')

@app.route("/peliculas")
def peliculas():
    response = requests.get("https://oaemdl.es/cinestar_sweb_php/peliculas")
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            return render_template('peliculas.html', peliculas=data['data'])
    return redirect(url_for('index'))

if __name__ == "__main__" :
    app.register_error_handler( 404, page_no_found )
    app.run( debug=False )