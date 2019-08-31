from model import *
from bottle import *

datoteka = 'views/datoteka_z_potezami.json'
trivvrsto=TriVVrsto(datoteka)

@get("/img/<file>")
def img(file):
    return static_file(file, root='img')

@get('/')
def hello():
    return template("views/index.tpl")

@post("/nova_igra/")
def nova_igra():
    trivvrsto.nova_igra()
    redirect("/igra/")

@get("/igra/")
def igra():
    return template("views/igra.tpl", trivvrsto=trivvrsto, text="Na vrsti je križec")

@post("/igra/")
def igra():
    poteza = request.forms.getunicode("vrsticaStolpec")
    c  = trivvrsto.dodajKrizecAliKrozec(poteza)
    trivvrsto.dodajKrizecAliKrozec(poteza)
    return template("views/igra.tpl", trivvrsto=trivvrsto, text=c)
    

run(debug=True, reloader=True)
