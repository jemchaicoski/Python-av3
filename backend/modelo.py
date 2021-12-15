from sqlalchemy.orm import backref, relationship
from config import *

class Pessoa(db.Model):
    __tablename__ = 'pessoa'
    id = db.Column(db.Integer, primary_key = True)
    nome =  db.Column(db.String(254))
    email = db.Column(db.String(254))
    cpf = db.Column(db.String(254))
    estudante_id = db.Column(db.Integer, db.ForeignKey('estudanteDaDisciplina.id'))


    def __str__(self) -> str:
        return f'(id={self.id}) {self.nome}, '+\
               f'{self.email}, {self.cpf}, {self.estudante_id}'
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "estudante": self.estudante_id
        }

class Disciplina(db.Model):
    __tablename__ = 'disciplina'
    id = db.Column(db.Integer, primary_key = True)
    nome =  db.Column(db.String(254))
    cargaHoraria = db.Column(db.Integer())
    ementa = db.Column(db.String(254))
    estudante_id = db.Column(db.Integer, db.ForeignKey('estudanteDaDisciplina.id'))


    def __str__(self) -> str:
        return f'(id={self.id}) {self.nome}, '+\
               f'{self.cargaHoraria}, {self.ementa}, {self.estudante_id}'
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cargaHoraria": self.cargaHoraria,
            "ementa": self.ementa,
            "estudante": self.estudante_id
        }

class EstudanteDaDisciplina(db.Model):
    __tablename__ = 'estudanteDaDisciplina'
    id = db.Column(db.Integer, primary_key = True)
    semestre = db.Column(db.Integer())
    pessoa =  db.relationship("Pessoa", backref="estudante", uselist = False)
    disciplina = db.relationship("Disciplina", backref="estudanteDaDisciplina", uselist = False)
    mediaFinal = db.Column(db.Integer())
    frequencia = db.Column(db.Integer())



    def __str__(self) -> str:
        return f'(id={self.id}) {self.semestre}, {self.pessoa}'+\
               f'{self.disciplina},{self.mediaFinal}, {self.frequencia}, '
    
    def json(self):
        return {
            "id": self.id,
            "semestre": self.semestre,
            "pessoa": self.pessoa,
            "disciplina": self.disciplina,
            "mediaFinal": self.mediaFinal,
            "frequencia": self.frequencia
        }
        
if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all()

    p1 = Pessoa()
    d1 = Disciplina(nome = "PDSP", cargaHoraria = 80, ementa = "uma materia")
    e1 = EstudanteDaDisciplina(semestre = 1, pessoa = p1, disciplina = d1, mediaFinal = 80, frequencia = 75)
    p1 = Pessoa(nome = "Carlos",email = "carlosemail@gmail.com", 
        cpf = "12345678900", estudante = e1)

    db.session.add(p1)
    db.session.add(e1)
    db.session.add(d1)
    db.session.commit()

    print(p1)
    print(e1)
    print(d1)