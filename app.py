from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [
    {
        'id': 1, 
        'nome': 'Guilherme Silva',
        'serie': 'Segundo ano do Ensino Médio',
        'turma': 'B'
    },
    {
        'id': 2, 
        'nome': 'Flavio Noim',
        'serie': 'Primeiro ano do Ensino Médio',
        'turma': 'F'
    },
    {
        'id': 3, 
        'nome': 'Pedro Henrique',
        'serie': ' Nono Ano do Ensino Fundamental II',
        'turma': 'D'
    },
    {
        'id': 4, 
        'nome': 'Rafael Teixeira',
        'serie': 'Terceiro Ano do Fundamemtal I',
        'turma': 'A'
    },
]


#Consultar Alunos Matriculados
@app.route('/alunos',methods=['GET'])
def obter_alunos():
    return jsonify(alunos)


#Consultar Alunos por Nome ( Como Pesquisar no Postman: http://localhost:5000/alunos/nome/Flavio%20Noim)
@app.route('/alunos/nome/<string:nome>', methods=['GET'])
def obter_aluno_por_nome(nome):
    for aluno in alunos:
        if aluno.get('nome').lower() == nome.lower():
            return jsonify(aluno)
    return jsonify({'erro': 'Aluno não encontrado'}), 404
       

#Consultar (Id)
@app.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno_por_id(id):
    for aluno in alunos:    
        if aluno.get('id') == id:
            return jsonify(aluno)

#Adicionar Novo Aluno
@app.route('/alunos', methods = ['POST'])
def incluir_novo_aluno():
    novo_aluno = request.get_json()
    alunos.append(novo_aluno)

    return jsonify(
        mensagem = 'Novo Aluno Matriculado!',
        alunos = novo_aluno) 

#Editar Classe ou Série
@app.route('/alunos/<int:id>', methods = ['PUT'])
def editar_aluno(id):
    aluno_editado = request.get_json()
    for indice,aluno in enumerate(alunos):
        if aluno.get('id') == id:
            alunos [indice].update(aluno_editado)
            return jsonify(alunos[indice])

#Expulsar Aluno 
@app.route('/alunos/<int:id>', methods = ['DELETE'])
def expulsar_aluno(id):
    for indice,aluno in enumerate(alunos):
        if aluno.get('id') == id:
            del alunos [indice]

            return jsonify(alunos)
        

#Total de Alunos
@app.route('/alunos/quantidade', methods=['GET'])
def contar_alunos():
    total = len(alunos)
    return jsonify({'mensagem': f'Atualmente há {total} aluno(s) matriculado(s).'})



app.run(port=5000,host='localhost',debug=True)