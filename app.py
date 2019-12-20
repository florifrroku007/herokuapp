from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    titolo="Welcome"
    testo="Home"
    bottone="More Info"
    return render_template("index.html",
        titolo=titolo,
        testo=testo,
        bottone=bottone)

@app.route('/contact')
def info():
    titolo="contact"
    testo="click here "
    bottone="Homepage"
    return render_template("info.html",
        titolo=titolo,
        testo=testo)

if __name__ == '__main__':
    app.run()