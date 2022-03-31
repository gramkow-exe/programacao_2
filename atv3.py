from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# flask
app = Flask(__name__)
# sqlalchemy com sqlite
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'pessoas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

class Casa(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    formato = db.Column(db.String(254))

    quartos = db.relationship("Quarto", backref = "Casa")

    def __str__(self) -> str:
        return f"{self.id}, {self.formato}"

class Quarto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254))
    dimensoes = db.Column(db.String(254))
    casa_id = db.Column(db.Integer, db.ForeignKey(Casa.id), nullable= False)

    mobilias = db.relationship("Mobilia", backref = "Quarto")

    def __str__(self) -> str:
        mobilias_list = []
        for i in self.mobilias:
            mobilias_list.append(str(i))
        return f"{self.id}, {self.nome},{self.dimensoes}, {str(self.Casa)}, {mobilias_list}"

    #casa = db.relationship("Casa")

class Mobilia(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254))
    funcao = db.Column(db.String(254))
    material = db.Column(db.String(254))
    quarto_id = db.Column(db.Integer, db.ForeignKey(Quarto.id), nullable = True)

    def __str__(self) -> str:
        return f"{self.id}, {self.nome}, {self.funcao}, {self.material}"

db.create_all()


c1 = Casa(formato ="Russa")
db.session.add(c1)
db.session.commit()
print(c1)

q1 = Quarto(nome="Cozinha", dimensoes = "10x10", Casa=c1)
db.session.add(q1)
db.session.commit()
print(q1)

m1 = Mobilia(nome = "Espelho", funcao = "Refletir", material = "Areia", Quarto = q1)
db.session.add(m1)
db.session.commit()

"""for q in db.session.query(Quarto).all():
    print(q)

for q in db.session.query(Quarto).filter(casa_id = c1.id).all():
    print(q)
"""
for q in c1.quartos:
    print(q)



