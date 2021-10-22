from config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome =  db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    def __str__(self) -> str:
        return f'(id={self.id}) {self.nome}, '+\
               f'{self.email}, {self.telefone}'
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all()

    p1 = Pessoa(nome = "Carlos", email = "carlosemail@gmail.com", 
        telefone = "+5547999999999")

    p2 = Pessoa(nome = "Carla", email = "carlaemail@gmail.com", 
        telefone = "+5547999999999")

    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()

    print(p1)