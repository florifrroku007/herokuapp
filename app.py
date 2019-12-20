from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    titolo="Pagina Iniziale"
    testo="Ciao mondo!"
    bottone="piu Info"
    return render_template("base.html",
	tittolo=tittolo,
    testo=testo,
    bottone=bottone)

if __name__ == '__main__':
    app.run()

@app.route('/info')
def info():
    titolo"Pagina Info"
    testo="Informazioni"
    bottone="Homepage"
    return render_template("base.html",
	tittolo=tittolo,
    testo=testo,
    bottone=bottone)

if __name__ == '__main__':
    app.run()