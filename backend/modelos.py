from enum import unique
from sqlalchemy.orm import backref, relationship
from config import *

class Carro(db.Model):
    __tablename__ = 'carro'
    id = db.Column(db.Integer, primary_key = True)
    marca =  db.Column(db.String(254))
    cor = db.Column(db.String(254))
    portas = db.Column(db.Integer)

    def __str__(self) -> str:
        return f'(id={self.id}) {self.marca} {self.cor} {self.portas}'
    
    def __init__(self, marca, cor, portas):
        self.marca = marca
        self.cor = cor
        self.portas = portas
        super(Carro,self).__init__()

    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "cor": self.cor,
            "portas": self.portas,
        }

class Moto(db.Model):
    __tablename__ = 'moto'
    id = db.Column(db.Integer, primary_key = True)
    marca =  db.Column(db.String(254))
    cor = db.Column(db.String(254))

    def __str__(self) -> str:
        return f'(id={self.id}) {self.marca} {self.cor}'
    
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        super(Moto,self).__init__()

    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "cor": self.cor,
        }

class Caminhao(db.Model):
    __tablename__ = 'caminhao'
    id = db.Column(db.Integer, primary_key = True)
    marca =  db.Column(db.String(254))
    cor = db.Column(db.String(254))
    eixos = db.Column(db.Integer)
    carga =  db.relationship("CargaCaminhao", backref="caminhao", uselist=False)

    def __str__(self) -> str:
        return f'(id={self.id}) {self.marca} {self.cor} {self.eixos}'
    
    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "cor": self.cor,
            "eixos": self.eixos,
        }

class CargaCaminhao(db.Model):
    __tablename__ = 'carga_caminhao'
    id = db.Column(db.Integer, primary_key = True)
    produto =  db.Column(db.String(254))
    preco = db.Column(db.Integer)
    caminhao_id = db.Column(db.Integer, db.ForeignKey('caminhao.id'), unique=True)

    def __str__(self) -> str:
        return f'(id={self.id}) {self.produto} {self.preco}'
    
    def json(self):
        return {
            "id": self.id,
            "produto": self.produto,
            "cor": self.preco,
        }

class Trator(db.Model):
    __tablename__ = 'trator'
    id = db.Column(db.Integer, primary_key = True)
    marca =  db.Column(db.String(254))
    cor = db.Column(db.String(254))
    chassi = db.Column(db.String(254)) # rígido ou articulado.

    def __str__(self) -> str:
        return f'(id={self.id}) {self.marca} {self.cor} {self.chassi}'
    
    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "cor": self.cor,
            "portas": self.chassi,
        }

class Onibus(db.Model):
    __tablename__ = 'onibus'
    id = db.Column(db.Integer, primary_key = True)
    marca =  db.Column(db.String(254))
    cor = db.Column(db.String(254))
    assentos = db.Column(db.Integer)

    def __str__(self) -> str:
        return f'(id={self.id}) {self.marca} {self.cor} {self.assentos}'
    
    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "cor": self.cor,
            "portas": self.assentos,
        }

class Trem(db.Model):
    __tablename__ = 'trem'
    id = db.Column(db.Integer, primary_key = True)
    marca =  db.Column(db.String(254))
    cor = db.Column(db.String(254))
    vagoes = db.relationship("Vagao", backref="vagao") #many to one

    def __str__(self) -> str:
        return f'(id={self.id}) {self.marca} {self.cor}'
    
    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "cor": self.cor,
        }

class Vagao(db.Model):
    __tablename__ = 'vagao'
    id = db.Column(db.Integer, primary_key = True)
    carga =  db.relationship("CargaVagao", backref="vagao", uselist=False) #one to one
    cor = db.Column(db.String(254))
    trem_id = db.Column(db.Integer, db.ForeignKey('trem.id')) #many to one

    def __str__(self) -> str:
        return f'(id={self.id}) {self.carga} {self.cor}'
    
    def json(self):
        return {
            "id": self.id,
            "marca": self.carga,
            "cor": self.cor,
        }
        
class CargaVagao(db.Model):
    __tablename__ = 'carga_vagao'
    id = db.Column(db.Integer, primary_key = True)
    produto =  db.Column(db.String(254))
    preco = db.Column(db.Integer)
    vagao_id = db.Column(db.Integer, db.ForeignKey('vagao.id'), unique=True) #one to one

    def __str__(self) -> str:
        return f'(id={self.id}) {self.produto} {self.preco}'
    
    def json(self):
        return {
            "id": self.id,
            "produto": self.produto,
            "cor": self.preco,
        }

class Barco(db.Model):
    __tablename__ = 'barco'
    id = db.Column(db.Integer, primary_key = True)
    marca =  db.Column(db.String(254))
    cor = db.Column(db.String(254))
    mastros = db.Column(db.Integer)
    carga =  db.relationship("CargaBarco", backref="barco", uselist=False)

    def __str__(self) -> str:
        return f'(id={self.id}) {self.marca} {self.cor} {self.mastros}'
    
    def __init__(self, marca, cor, mastros):
        self.marca = marca
        self.cor = cor
        self.mastros = mastros
        super(Barco,self).__init__()

    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "cor": self.cor,
            "mastros": self.mastros
        }

class CargaBarco(db.Model):
    __tablename__ = 'carga_barco'
    id = db.Column(db.Integer, primary_key = True)
    produto =  db.Column(db.String(254))
    preco = db.Column(db.Float)
    barco_id = db.Column(db.Integer, db.ForeignKey('barco.id'), unique=True)
    
    def __str__(self) -> str:
        return f'(id={self.id}) {self.produto} {self.preco} {self.barco_id}'
    
    def __init__(self, produto, preco, barcoId):
        self.produto = produto
        self.preco = preco
        self.barco_id = barcoId
        super(CargaBarco,self).__init__()

    def json(self):
        return {
            "id": self.id,
            "produto": self.produto,
            "cor": self.preco,
            "barco_id": self.barco_id
        }

if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all()

    carro = Carro("marca", "azul", 4)
    moto = Moto("marca", "vermelha")
    barco = Barco("marca", "rosa", 3)
    cargaBarco = CargaBarco("banana", 1500.00, barco)

    db.session.add(barco)
    db.session.add(cargaBarco)
    db.session.add(carro)
    db.session.add(moto)
    db.session.commit()

    print(barco)
    print(cargaBarco)
    print(carro)
    print(moto)