from flask import Flask, request, jsonify

app = Flask(__name__)

# Banco de dados fictício (armazenamento em memória)
pessoas = [
    {"id": 1, "nome": "João Silva", "idade": 30},
    {"id": 2, "nome": "Maria Souza", "idade": 25},
]

# Função auxiliar para encontrar pessoa pelo ID
def encontrar_pessoa(id):
    return next((pessoa for pessoa in pessoas if pessoa["id"] == id), None)

# Rota para ler todas as pessoas (READ)
@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    return jsonify(pessoas), 200

# Rota para ler uma única pessoa por ID (READ)
@app.route('/pessoas/<int:id>', methods=['GET'])
def obter_pessoa(id):
    pessoa = encontrar_pessoa(id)
    if pessoa:
        return jsonify(pessoa), 200
    return jsonify({"error": "Pessoa não encontrada"}), 404

# Rota para criar uma nova pessoa (CREATE)
@app.route('/pessoas', methods=['POST'])
def criar_pessoa():
    nova_pessoa = request.get_json()
    if "nome" not in nova_pessoa or "idade" not in nova_pessoa:
        return jsonify({"error": "Dados inválidos"}), 400

    nova_pessoa["id"] = len(pessoas) + 1
    pessoas.append(nova_pessoa)
    return jsonify(nova_pessoa), 201

# Rota para atualizar uma pessoa existente (UPDATE)
@app.route('/pessoas/<int:id>', methods=['PUT'])
def atualizar_pessoa(id):
    pessoa = encontrar_pessoa(id)
    if pessoa is None:
        return jsonify({"error": "Pessoa não encontrada"}), 404

    dados_atualizados = request.get_json()
    pessoa["nome"] = dados_atualizados.get("nome", pessoa["nome"])
    pessoa["idade"] = dados_atualizados.get("idade", pessoa["idade"])

    return jsonify(pessoa), 200

# Rota para deletar uma pessoa (DELETE)
@app.route('/pessoas/<int:id>', methods=['DELETE'])
def deletar_pessoa(id):
    pessoa = encontrar_pessoa(id)
    if pessoa is None:
        return jsonify({"error": "Pessoa não encontrada"}), 404

    pessoas.remove(pessoa)
    return jsonify({"message": "Pessoa removida com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)