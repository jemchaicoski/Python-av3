from config import *
from modelo import Pessoa

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_pessoas">Operação listar</a>'

@app.route("/listar_pessoas")
def listar_pessoas():
    pessoas = db.session.query(Pessoa).all()
    pessoas_em_json = [ x.json() for x in pessoas ]
    resposta = jsonify(pessoas_em_json)

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)    
