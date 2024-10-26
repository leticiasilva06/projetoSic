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

@app.route("/imagens")
def imagens():
    return render_template("imagens.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar 
if __name__ == "__main__":
    app.run(debug=True)
    
    # servidor do heroku
   