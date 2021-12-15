from config import *
from flask import request
from modelo import EstudanteDaDisciplina

@app.route("/")
def inicio():
    return 'Sistema de cadastro de estudantes. '+\
        '<a href="/listar_estudantes">Operação listar</a>'

@app.route("/listar_estudantes")
def listar_estudantes():
    estudantes = db.session.query(EstudanteDaDisciplina).all()
    estudantes_em_json = [ x.json() for x in estudantes ]
    resposta = jsonify(estudantes_em_json)

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
  

@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa(): 
   resposta = jsonify({"resultado": "ok", "detalhes": "ok"}) 

   dados = request.get_json() 
   try: 
    nova = EstudanteDaDisciplina(**dados) 
    print(nova)
    db.session.add(nova) 
    db.session.commit() 
   except Exception as e: 
    resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta 
    
app.run(debug=False) 