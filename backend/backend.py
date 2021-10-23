from config import *
from flask import request
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
  

@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa(): 
   resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 

   dados = request.get_json() 
   try: 
    nova = Pessoa(**dados) 
    print(nova)
    db.session.add(nova) 
    db.session.commit() 
   except Exception as e: 
    resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta 
    
app.run(debug=False) 