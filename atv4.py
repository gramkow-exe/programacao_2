from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# flask
app = Flask(__name__)
# sqlalchemy com sqlite
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'trabalhadores.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    tipo = db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_identity": 'pessoa', #identidade da tabela
        "polymorphic_on" : tipo #identidade de herança

    }
    

    def __str__(self) -> str:
        return f"Id: {self.id}, Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}*"


class Vendedor(Pessoa):
    comissao = db.Column(db.String(254))
    id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), primary_key=True) #liga-se a tabela pessoa

    __mapper_args__ = {
        "polymorphic_identity" : 'vendedor' 
    }
    
    def __str__(self) -> str:
        return super().__str__() + f", Comissão {self.comissao}" #utiliza a função str pai em super().__str__()

db.create_all() #cria as tabelas, iniciando o arquivo
        
pedro =Vendedor(nome="Pedro", email="pe@gmail.com", comissao = 10)
db.session.add(pedro) #Adiciona pedro
db.session.commit() #comita o mesmo (junto ao de cima criam a primary key)


class Motorista(Pessoa):
    cnh = db.Column(db.String(254))

    __mapper_args__ = {
        "polymorphic_identity" : 'motorista' 
    }

    def __str__(self) -> str:
        return super().__str__() + f", Cnh: {self.cnh}"



if __name__ == "__main__":   

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
        

    pedro =Vendedor(nome="Pedro", email="pe@gmail.com", comissao = 10)
    db.session.add(pedro)
    db.session.commit()

    teresa = Motorista(nome="Teresa", cnh="1234-5")
    db.session.add(teresa)
    db.session.commit()

    print(teresa)
