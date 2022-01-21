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
        return f'(Carro: id={self.id} marca={self.marca} cor={self.cor} portas={self.portas})'
    
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
        return f'(Moto: id={self.id} marca={self.marca} cor={self.cor}'
    
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
        return f'(Caminhao: id={self.id}) marca={self.marca} cor={self.cor} eixos={self.eixos}'
    
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
    preco = db.Column(db.Float)
    caminhao_id = db.Column(db.Integer, db.ForeignKey('caminhao.id'), unique=True)

    def __str__(self) -> str:
        return f'(CargaCaminhao: id={self.id} produto={self.produto} preco={self.preco})'
    
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
        return f'(Trator: id={self.id} marca={self.marca} cor={self.cor} chassi={self.chassi})'
    
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
        return f'(Onibus: id={self.id} marca={self.marca} cor={self.cor} assentos={self.assentos})'
    
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
    vagoes = db.relationship("Vagao", backref="trem") #many to one

    def __str__(self) -> str:
        return f'(Trem: id={self.id} marca={self.marca} cor={self.cor} vagões={self.vagoes})'
    
    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "cor": self.cor,
            "vagoes": self.vagoes
        }

class Vagao(db.Model):
    __tablename__ = 'vagao'
    id = db.Column(db.Integer, primary_key = True)
    carga =  db.relationship("CargaVagao", backref="vagao", uselist=False) #one to one
    cor = db.Column(db.String(254))
    trem_id = db.Column(db.Integer, db.ForeignKey('trem.id')) #many to one

    def __str__(self) -> str:
        return f'(Vagao: id={self.id} carga={self.carga} cor={self.cor} trem_id={self.trem_id})'
    
    def json(self):
        return {
            "id": self.id,
            "marca": self.carga,
            "cor": self.cor,
            "carga": self.carga,
            "trem_id": self.trem_id
        }
        
class CargaVagao(db.Model):
    __tablename__ = 'carga_vagao'
    id = db.Column(db.Integer, primary_key = True)
    produto =  db.Column(db.String(254))
    preco = db.Column(db.Float)
    vagao_id = db.Column(db.Integer, db.ForeignKey('vagao.id'), unique=True) #one to one

    def __str__(self) -> str:
        return f'(CargaVagao: id={self.id} produto={self.produto} preço={self.preco} vagãoID={self.vagao_id})'
    
    def json(self):
        return {
            "id": self.id,
            "produto": self.produto,
            "cor": self.preco,
            "vagao_id": self.vagao_id
        }

class Barco(db.Model):
    __tablename__ = 'barco'
    id = db.Column(db.Integer, primary_key = True)
    marca =  db.Column(db.String(254))
    cor = db.Column(db.String(254))
    mastros = db.Column(db.Integer)
    carga =  db.relationship("CargaBarco", backref="barco", uselist=False)

    def __str__(self) -> str:
        return f'(Barco: id={self.id} marca={self.marca} cor={self.cor} mastros={self.mastros})'
    
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
        return f'(CargaBarco: id={self.id} produto={self.produto} preço={self.preco} barcoID={self.barco_id}'

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
    cargaBarco = CargaBarco(produto = "banana", preco = 1500.00, barco = barco)

    trem = Trem(marca="marca", cor="verde")
    vagao1 = Vagao(cor = "verde", trem = trem)
    vagao2 = Vagao(cor = "verde", trem = trem)
    cargaVagao1 = CargaVagao(produto = "coco", preco = 1000.00, vagao = vagao1)
    cargaVagao2 = CargaVagao(produto = "macarrão", preco = 2000.00, vagao = vagao2)

    onibus = Onibus(marca = "marca", cor = "amarelo", assentos = 40)

    trator = Trator(marca = "marca", cor = "Roxo", chassi = "rígido")

    caminhao = Caminhao(marca = "marca", cor = "laranja", eixos = 4)
    cargaCaminhao = CargaCaminhao(produto = "camisetas", preco = 4000.00, caminhao = caminhao) 


    db.session.add(caminhao)
    db.session.add(cargaCaminhao)
    db.session.add(trator)
    db.session.add(onibus)
    db.session.add(trem)
    db.session.add(vagao1)
    db.session.add(vagao2)
    db.session.add(cargaVagao1)
    db.session.add(cargaVagao2)
    db.session.add(barco)
    db.session.add(cargaBarco)
    db.session.add(carro)
    db.session.add(moto)
    db.session.commit()


    print("<::::-----------------------------------------------::::>")
    print(caminhao)
    print(cargaCaminhao)
    print("------------------------------------------------")
    print(trator)
    print("------------------------------------------------")
    print(onibus)
    print("------------------------------------------------")
    print(trem)
    print("------------------------------------------------")
    print(vagao1)
    print(vagao2)
    print("------------------------------------------------")
    print(cargaVagao1)
    print(cargaVagao2)
    print("------------------------------------------------")
    print(barco)
    print(cargaBarco)
    print("------------------------------------------------")
    print(carro)
    print("------------------------------------------------")
    print(moto)
    print("<::::------------------------------------------------::::>")