# importar o Flask
from flask import Flask, render_template

#criaçao da pagina (padrão)
app = Flask(__name__)
# route -> salvacaodeimagens.com/
# função -> é oq eu quero exibir na pagina
#template

# criar a 1° pagina do site
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/teste")
def imagens():
    return render_template("teste.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@app.route("/sobre")
def sobre():
    return render_template("quemSomos.html")

# colocar o site no ar 
if __name__ == "__main__":
    app.run(debug=True)
    
    # servidor do heroku
   