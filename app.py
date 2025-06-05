from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def cadastro():
    return render_template("cadastro.html")

@app.route("/submit", methods=["POST"])
def submit():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    senha_confirm = request.form.get("senha_confirm")

    if not (nome and email and senha and senha_confirm):
        return render_template("resposta.html", mensagem="Erro: Preencha todos os campos.")

    if senha != senha_confirm:
        return render_template("resposta.html", mensagem="Erro: As senhas não conferem.")

    return render_template("resposta.html", mensagem="Usuário cadastrado com sucesso!")

if __name__ == "__main__":
    app.run(debug=True)


