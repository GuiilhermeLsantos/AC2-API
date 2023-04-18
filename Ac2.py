from flask import Flask, jsonify

app = Flask(__name__)

funcionarios = [
    {"id": 1,
     "name": "Guilherme Lima",
     "Cargo": "Desenvolvedor Junior"},

    {"id": 2,
     "name": "Maria Santana",
        "Cargo": "Cordenadora Senior"},

    {"id": 3,
     "name": "Bianca Lima",
        "Cargo": "Desenvolvedora Junior"}
]


@app.route('/busca/<int:funcionarios_id>', methods=['GET'])
def busca(funcionarios_id):
    consulta = None
    for dados in funcionarios:
        if dados['id'] == funcionarios_id:
            consulta = dados
            break

    if consulta is not None:
        return jsonify(consulta), 200
    else:
        return jsonify({"mensagem": "Funcionario não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
