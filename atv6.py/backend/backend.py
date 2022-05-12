from config import *
from modelo import Pessoa

def pessoa_html(id, nome, email):
  return f"<tr style='display:flex; justify-content: space-between'><td>{id}</td><td>{nome}</td><td>{email}</td></tr>"

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/incluir_pessoa">Operação incluir pessoa</a>'

# teste da rota: curl -d '{"nome":"James Kirk", "telefone":"92212-1212", "email":"jakirk@gmail.com"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_pessoa
@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "oi"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: # tentar executar a operação
      nova = Pessoa(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!
    

@app.route("/mostrar_pessoas", methods=['get'])
def mostrar_pessoa():
  a = "<table style='display:flex; align-items:center; justify-content: center; border: 1px solid red; width: 30%'><th style='display:flex; align-items:center'><td>Id</td><td>Nome</td><td>Email</td>"
  for i in db.session.query(Pessoa).all():
    a+= pessoa_html(i.id, i.nome, i.email)
  a+="</table>"
  print(a)
  return a
    


app.run(debug=True)