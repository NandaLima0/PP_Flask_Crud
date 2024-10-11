from flask import Flask, render_template, request, redirect

app = Flask(__name__)
contas = []

@app.route('/', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        contas.append({"nome": nome, "email": email})
    return render_template("index.html", contas=contas)

@app.route('/alterar', methods=["GET", "POST"])
def update():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        new_nome = request.form["new_nome"]
        new_email = request.form["new_email"]

        for conta in contas:
            if conta["nome"] == nome and conta["email"] == email:
                conta["nome"] = new_nome
                conta["email"] = new_email
                break
    return render_template("alterar.html", contas=contas)

@app.route('/deletar', methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        contas[:] = [conta for conta in contas if not (conta["nome"] == nome and conta["email"] == email)]
        mensagem = "Conta excluída com sucesso!"
    else:
        mensagem = None
    return render_template("excluir.html", contas=contas, mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
