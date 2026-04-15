from flask import Flask, render_template, request, redirect
app = Flask(__name__)
eventos = []

@app.route("/")
def home():
    return render_template("index.html", eventos=eventos)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    data = request.form["data"]
    local = request.form["local"]
    desc = request.form["descricao"]
    evento = {
        "id": len(eventos),
        "nome": nome,
        "data": data,
        "local": local,
        "desc": desc
    }

@app.route("/editar/<int:id>")
def editar(id):
    evento = eventos[id]
    return render_template("editar.html", evento=evento)

    eventos.append(evento)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)